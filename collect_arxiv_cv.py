"""Create a Japanese CSV (and a matching .xlsx) survey of recent arXiv cs.CV papers.

Examples:
    python collect_arxiv_cv.py
    python collect_arxiv_cv.py --start 2026-10-14 --end 2026-10-16
"""

import argparse
import csv
import html
import json
import re
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from email.utils import parsedate_to_datetime
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter


JST = ZoneInfo("Asia/Tokyo")
RESULT_DIR = Path(__file__).resolve().parent / "result"
USER_AGENT = "arXiv-csCV-survey/1.0 (research CSV generator)"
COMPANIES = {
    "Google DeepMind": r"\bgoogle\s+deepmind\b",
    "Google": r"\bgoogle\b",
    "Microsoft": r"\bmicrosoft\b",
    "Amazon": r"\bamazon\b|\baws\b",
    "NVIDIA": r"\bnvidia\b",
    "Adobe": r"\badobe\b",
    "OpenAI": r"\bopenai\b",
    "ByteDance": r"\bbytedance\b",
    "Tencent": r"\btencent\b",
    "Alibaba": r"\balibaba\b",
    "Huawei": r"\bhuawei\b",
    "Samsung": r"\bsamsung\b",
    "Sony": r"\bsony\b",
    "Qualcomm": r"\bqualcomm\b",
    "IBM": r"\bibm\b",
    "Salesforce": r"\bsalesforce\b",
    "Tesla": r"\btesla\b",
    "Toyota": r"\btoyota\b",
    "Bosch": r"\bbosch\b",
    "Siemens": r"\bsiemens\b",
    "NAVER": r"\bnaver\b",
    "Kakao": r"\bkakao\b",
    "SenseTime": r"\bsensetime\b",
    "Megvii": r"\bmegvii\b",
    "Xiaomi": r"\bxiaomi\b",
    "OPPO": r"\boppo\b",
    "Kuaishou": r"\bkuaishou\b",
    "Stability AI": r"\bstability ai\b",
    "Magic Leap": r"\bmagic leap\b",
    "Waymo": r"\bwaymo\b",
    "Zoox": r"\bzoox\b",
    "Mobileye": r"\bmobileye\b",
    "Mistral AI": r"\bmistral ai\b",
}
# Common English words / short names: match case-sensitively and only with a
# corporate form to avoid false positives (e.g. "meta-learning", "runway").
AMBIGUOUS_COMPANIES = {
    "Meta": r"\bMeta(?: AI| Platforms| Reality Labs)?\b(?![-\w])|\bFAIR\b",
    "Apple": r"\bApple(?: Inc\.?)?\b",
    "Intel": r"\bIntel(?: Corporation| Labs)?\b",
    "Snap": r"\bSnap(?: Inc\.?| Research)\b",
    "Cruise": r"\bCruise(?: LLC| Automation)\b",
    "Runway": r"\bRunway(?: ML| AI)\b",
    "vivo": r"\bvivo(?: AI| Mobile)\b|\bVivo\b",
    "Oracle": r"\bOracle(?: Corporation| Labs)?\b",
    "Uber": r"\bUber(?: ATG| AI| Technologies)?\b",
}
HEADERS = [
    "発表日", "英文タイトル", "和訳タイトル", "著者の所属する企業名", "ソースコードの開示有無",
    "物体検出・追跡", "画素単位セグメンテーション", "画像・動画編集", "画像・動画生成",
    "画像・動画から3D・深度", "3D物体検出・セグメンテーション", "3D生成・編集",
    "画像・動画・3Dからテキスト", "高速化・軽量化・学習効率化", "非RGBセンサー使用",
    "ロボット動作", "自動運転", "医療画像", "産業画像", "人物",
    "arXiv ID", "URL", "alphaXiv URL",
]
VIEWPOINT_COUNT = 15  # the ● columns, right after the code-status column
HTML_COLUMNS = 5 + VIEWPOINT_COUNT  # the HTML page hides the ID and URL columns


_rate_lock = threading.Lock()
_next_slot = {}


def throttle(host, interval):
    """Space requests to one host at least `interval` seconds apart (all threads)."""
    with _rate_lock:
        now = time.monotonic()
        slot = max(now, _next_slot.get(host, 0.0))
        _next_slot[host] = slot + interval
    if slot > now:
        time.sleep(slot - now)


def fetch(url, params=None, timeout=90, retries=4, interval=0.0):
    """GET with retry on transient errors (406/429/5xx/network). 404 etc. raise at once."""
    if params:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    host = urllib.parse.urlsplit(url).netloc
    for attempt in range(retries + 1):
        if interval:
            throttle(host, interval)
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code not in (406, 429, 500, 502, 503, 504) or attempt == retries:
                raise
        except OSError:
            if attempt == retries:
                raise
        time.sleep(5 * (attempt + 1))


def clean(value):
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def parse_date(value):
    return datetime.strptime(value, "%Y-%m-%d").date()


OAI_URL = "https://oaipmh.arxiv.org/oai"
OAI_NS = {
    "oai": "http://www.openarchives.org/OAI/2.0/",
    "raw": "http://arxiv.org/OAI/arXivRaw/",
}


def collect_entries(start, end):
    """Harvest cs.CV papers whose first version (v1) was submitted in [start, end] JST.

    OAI-PMH selects by datestamp (last metadata change, UTC date), which is on or
    after the v1 submission. So harvest from the day before `start` (JST midnight is
    the previous day in UTC) up to today, then filter on the exact v1 timestamp.
    """
    harvest_from = start - timedelta(days=1)
    harvest_until = datetime.now(JST).date()
    params = {
        "verb": "ListRecords",
        "metadataPrefix": "arXivRaw",
        "set": "cs",
        "from": harvest_from.isoformat(),
        "until": harvest_until.isoformat(),
    }
    papers, seen = [], set()
    while params:
        # arXiv's terms for OAI-PMH: one request per 3 seconds.
        root = ET.fromstring(fetch(OAI_URL, params, timeout=180, interval=3.0))
        error = root.find("oai:error", OAI_NS)
        if error is not None:
            if error.get("code") == "noRecordsMatch":
                break
            raise OSError(f"OAI-PMH error {error.get('code')}: {clean(error.text)}")
        for record in root.iterfind("oai:ListRecords/oai:record", OAI_NS):
            meta = record.find("oai:metadata/raw:arXivRaw", OAI_NS)
            if meta is None:  # deleted record
                continue
            categories = (meta.findtext("raw:categories", "", OAI_NS)).split()
            if "cs.CV" not in categories:
                continue
            v1 = meta.find("raw:version[@version='v1']/raw:date", OAI_NS)
            if v1 is None:
                continue
            submitted = parsedate_to_datetime(v1.text).astimezone(JST)
            paper_id = meta.findtext("raw:id", "", OAI_NS).strip()
            if not start <= submitted.date() <= end or paper_id in seen:
                continue
            seen.add(paper_id)
            papers.append(
                {
                    "id": paper_id,
                    "submitted": submitted,
                    "title": clean(meta.findtext("raw:title", "", OAI_NS)),
                    "summary": clean(meta.findtext("raw:abstract", "", OAI_NS)),
                }
            )
        token = root.findtext("oai:ListRecords/oai:resumptionToken", "", OAI_NS).strip()
        params = {"verb": "ListRecords", "resumptionToken": token} if token else None
    papers.sort(key=lambda paper: paper["submitted"], reverse=True)
    return papers


def translate(title):
    """Translate with the publicly available Project Segfault API."""
    for attempt in range(5):
        try:
            data = json.loads(fetch(
                "https://translate.projectsegfau.lt/api/translate",
                {"engine": "all", "from": "en", "to": "ja", "text": title},
                timeout=60,
            ).decode("utf-8"))
            for result in data:
                translated = clean(result.get("translated-text"))
                if translated:
                    return translated
        except (OSError, ValueError, json.JSONDecodeError):
            pass
        time.sleep(2 * (attempt + 1))
    return ""  # Keep the row and visibly report an unavailable translation.


def fetch_html(paper_id, interval):
    try:
        return paper_id, fetch(
            f"https://arxiv.org/html/{paper_id}", interval=interval
        ).decode("utf-8", errors="replace")
    except OSError:  # includes HTTPError, e.g. 404 when no HTML version exists
        return paper_id, ""


def strip_tags(fragment):
    return clean(re.sub(r"<[^>]+>", " ", fragment))


def author_block(page):
    """Affiliation text: explicit affiliation spans, else the whole author block."""
    affiliations = re.findall(
        r'<span[^>]*class="[^"]*ltx_role_affiliation[^"]*"[^>]*>(.*?)</span>\s*</span>',
        page,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if affiliations:
        return " ".join(strip_tags(a) for a in affiliations)
    match = re.search(
        r'<div[^>]*class="[^"]*ltx_authors[^"]*"[^>]*>(.*?)</div>\s*(?:<div[^>]*class="[^"]*ltx_abstract|<section|<h[1-6])',
        page,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return strip_tags(match.group(1)) if match else ""


def companies_from_html(page):
    text = author_block(page)
    found = [
        name for name, pattern in COMPANIES.items()
        if re.search(pattern, text, re.IGNORECASE)
    ]
    found += [
        name for name, pattern in AMBIGUOUS_COMPANIES.items()
        if re.search(pattern, text)
    ]
    if "Google DeepMind" in found and "Google" in found:
        found.remove("Google")  # the generic hit is redundant
    return "; ".join(dict.fromkeys(found))


def code_status(summary):
    """Abstract only (avoids GitHub links cited in the body): あり / 公開予定 / なし."""
    if re.search(
        r"(?:github\.com|github\.io|gitlab\.com|bitbucket\.org|codeberg\.org|huggingface\.co)/",
        summary,
        flags=re.IGNORECASE,
    ):
        return "あり"
    if re.search(
        r"\b(?:code|codes|models?|implementation|source code)\b.{0,60}\b(?:will be|to be)\b.{0,30}\b(?:released?|available|open-sourced?|public)"
        r"|\bwill (?:release|open-source|make)\b.{0,50}\b(?:code|models?|implementation)",
        summary,
        flags=re.IGNORECASE,
    ):
        return "公開予定"
    if re.search(
        r"\b(?:code|source code|implementation)\b.{0,40}\b(?:is|are)\b.{0,20}\b(?:available|released|publicly)"
        r"|\bproject page\b|\bopen-source[d]?\b",
        summary,
        flags=re.IGNORECASE,
    ):
        return "あり"
    return "なし"


def mark(condition):
    return "●" if condition else ""


def classify(paper):
    text = f"{paper['title']} {paper['summary']}".lower()
    rgb = r"(?:image|images|video|visual|rgb|frame|frames|photograph)"
    three_d = r"(?:3d|three-dimensional|point cloud|pointcloud|mesh|voxel|nerf|gaussian splat)"
    return [
        mark(bool(re.search(r"\b(object detection|object tracking|multi-object tracking|visual tracking|bounding box)\b", text))),
        mark(bool(re.search(r"\b(segmentation|semantic segmentation|instance segmentation|panoptic|matting)\b", text))),
        mark(bool(re.search(r"\b(image|video).{0,35}\b(edit|restor|enhanc|inpaint|super.resol|deblur|denois|coloriz|retouch|styliz)|\b(edit|restor|enhanc|inpaint|super.resol|deblur|denois|coloriz|retouch|styliz).{0,35}\b(image|video)", text))),
        mark(bool(re.search(r"\b(diffusion|generative|generate|generation|synthesi[sz]\w*|text-to-image|text-to-video|image synthesis|video synthesis)\b", text) and re.search(rgb, text))),
        mark(bool(re.search(rgb, text) and re.search(r"\b(depth|depth estimation|monocular depth|3d reconstruction|novel view|nerf|gaussian splatt\w*|visual odometry|slam)\b", text))),
        mark(bool(re.search(three_d, text) and re.search(r"\b(object detection|detection|segmentation|semantic|instance|panoptic)\b", text))),
        mark(bool(re.search(three_d, text) and re.search(r"\b(generate|generation|synthesi[sz]\w*|create|editing|edit|text-to-3d)\b", text))),
        mark(bool(re.search(rgb + "|" + three_d, text) and re.search(r"\b(caption\w*|image-to-text|video-to-text|visual question|vqa|ocr|text recognition|document understanding|report generation)\b", text))),
        mark(bool(re.search(r"\b(efficient|efficiency|accelerat\w*|faster|speedup|lightweight|compression|compress\w*|prun\w*|quantiz\w*|distill\w*|low-rank|token merg\w*|caching|kv cache|parameter-efficient|compute-efficient|memory-efficient)\b", text))),
        mark(bool(re.search(r"\b(event camera|event-based|lidar|radar|infrared|thermal|hyperspectral|multispectral|computed tomography|mri|x-ray|ultrasound|sonar)\b", text))),
        # Robot motion: manipulation, locomotion, embodied agents, VLA policies.
        mark(bool(re.search(r"\b(robot\w*|(?:robotic|object|dexterous|bimanual) manipulation|manipulation (?:tasks?|polic(?:y|ies))|grasp(?:ing|s)?|humanoid\w*|locomotion|embodied|vision-language-action|vla|visuomotor|teleoperat\w*|end-effector|legged|quadruped\w*)\b", text))),
        # Autonomous driving.
        mark(bool(re.search(r"\b(autonomous driving|self-driving|autonomous vehicles?|driving scenes?|end-to-end driving|driving policy|adas|bird's-eye.view|bev|nuscenes|waymo|argoverse|carla|motion forecasting|trajectory prediction|traffic|pedestrians?)\b", text))),
        # Medical imaging.
        mark(bool(re.search(r"\b(medical|clinical|clinic\w*|radiolog\w*|patholog\w*|histopatholog\w*|whole.slide|computed tomography|ct scans?|mri|x-ray|chest|ultrasound|endoscop\w*|colonoscop\w*|fundus|retina\w*|dermatolog\w*|skin lesion\w*|lesions?|tumou?rs?|cancer|patients?|surgical|surgery|mammograph\w*)\b", text))),
        # Industrial imaging: inspection, defects, manufacturing.
        mark(bool(re.search(r"\b(industrial|manufactur\w*|factory|factories|defect detection|defect inspection|defect segmentation|defective|surface defects?|(?:visual|optical|automated|product) inspection|mvtec\w*|pcb|printed circuit|production line|assembly line|weld\w*|steel)\b", text))),
        # People in images, video or 3D: bodies, faces, hands, motion, avatars.
        # Bare "human", "person", "people" and "face" are avoided: they mostly mean
        # human evaluation, "people often ...", or "faces challenges".
        mark(bool(re.search(r"\b(person (?:re-?identification|re-?id|detection|tracking|search|images?|videos?|poses?|segmentation)|(?:multi|single)-person|pedestrians?|human faces?|(?:talking|partial|full)[- ]faces?|faces? (?:recognition|detection|images?|videos?|generation|editing|forgery|anti-spoofing|reenactment|animation|attributes?|landmarks?|parsing|verification|identit(?:y|ies)|reconstruction|forensics|morphing|super-resolution|restoration|swap\w*)|crowd (?:counting|scenes?|analysis|localization)|humans? (?:body|bodies|poses?|motions?|mesh(?:es)?|avatars?|faces?|hands?|actions?|activit(?:y|ies)|videos?|images?|reconstruction|rendering|generation|digitization|subjects?|parsing|detection|tracking|keypoints?|interactions?)|human-object|human-scene|full-body|whole-body|body (?:pose|shape|mesh|motion)|hand[- ]object|hand (?:pose|mesh|reconstruction|tracking|gestures?)|facial|talking[- ]heads?|portraits?|avatars?|smpl\w*|gait|gestures?|sign language|re-identification|reid|motion capture|mocap|dance|dancing|garments?|clothing|clothed|virtual try-on|try-on|deepfakes?|face swap\w*|lip[- ]sync\w*)\b", text))),
    ]


#             発表日 英題 和訳 企業 コード  観点×14  ID  URL  alphaXiv
XLSX_WIDTHS = [11, 60, 50, 24, 10] + [9] * VIEWPOINT_COUNT + [12, 32, 36]


def write_xlsx(rows, path):
    """Same table as the CSV, with a frozen header row, filters and clickable URLs."""
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "cs.CV"
    sheet.append(HEADERS)
    for row in rows:
        sheet.append(row)

    header_fill = PatternFill("solid", fgColor="DDEBF7")
    for cell in sheet[1]:
        cell.font = Font(bold=True)
        cell.fill = header_fill
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    for row in sheet.iter_rows(min_row=2):
        row[0].number_format = "yyyy-mm-dd"
        for cell in row[4:5 + VIEWPOINT_COUNT]:  # code status and the ● columns
            cell.alignment = Alignment(horizontal="center")
        for cell in row[-2:]:  # arXiv and alphaXiv URLs
            cell.hyperlink = cell.value
            cell.style = "Hyperlink"
        row[1].hyperlink = row[-1].value  # English title opens the alphaXiv page
        row[1].style = "Hyperlink"
    for index, width in enumerate(XLSX_WIDTHS, 1):
        sheet.column_dimensions[get_column_letter(index)].width = width
    sheet.row_dimensions[1].height = 45

    sheet.freeze_panes = "A2"
    sheet.auto_filter.ref = sheet.dimensions
    workbook.save(path)


HTML_TEMPLATE = r"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
:root {
  --bg: #ffffff; --fg: #1f2328; --muted: #656d76; --line: #d0d7de;
  --head: #ddebf7; --stripe: #f6f8fa; --hover: #fff8c5; --link: #0969da;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0d1117; --fg: #e6edf3; --muted: #8d96a0; --line: #30363d;
    --head: #1c2d41; --stripe: #161b22; --hover: #2d2a16; --link: #4493f8;
  }
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--fg);
  font: 13px/1.45 system-ui, "Segoe UI", "Yu Gothic UI", "Meiryo", sans-serif; }
header { display: flex; flex-wrap: wrap; gap: 8px 16px; align-items: baseline;
  padding: 10px 16px; border-bottom: 1px solid var(--line); }
h1 { margin: 0; font-size: 16px; }
#count { color: var(--muted); }
button { font: inherit; padding: 2px 10px; border: 1px solid var(--line);
  border-radius: 4px; background: var(--bg); color: var(--fg); cursor: pointer; }
.wrap { height: calc(100vh - 46px); overflow: auto; }
table { border-collapse: separate; border-spacing: 0; min-width: 100%; }
thead { position: sticky; top: 0; z-index: 1; }
th { background: var(--head); font-weight: 600; text-align: center; vertical-align: middle;
  padding: 4px 6px; border-right: 1px solid var(--line); border-bottom: 1px solid var(--line); }
th.sort { cursor: pointer; user-select: none; }
th.sort::after { content: " \2195"; color: var(--muted); }
th.asc::after { content: " \25B2"; color: var(--fg); }
th.desc::after { content: " \25BC"; color: var(--fg); }
tr.filters th { font-weight: normal; padding: 3px 4px; }
th input, th select { width: 100%; font: inherit; padding: 1px 3px; color: var(--fg);
  background: var(--bg); border: 1px solid var(--line); border-radius: 3px; }
td { padding: 3px 6px; border-right: 1px solid var(--line); border-bottom: 1px solid var(--line);
  vertical-align: top; }
tbody tr:nth-child(even) td { background: var(--stripe); }
tbody tr:hover td { background: var(--hover); }
td.c { text-align: center; white-space: nowrap; }
td.nw { white-space: nowrap; }
a { color: var(--link); }
.w-title { min-width: 360px; } .w-ja { min-width: 280px; } .w-co { min-width: 140px; }
.w-flag { min-width: 64px; max-width: 80px; }
</style>
</head>
<body>
<header>
  <h1>__TITLE__</h1>
  <span id="count"></span>
  <button id="reset" type="button">絞り込みを解除</button>
</header>
<div class="wrap">
  <table>
    <thead><tr id="heads"></tr><tr class="filters" id="filters"></tr></thead>
    <tbody id="rows"></tbody>
  </table>
</div>
<script id="data" type="application/json">__DATA__</script>
<script>
const {headers, rows} = JSON.parse(document.getElementById("data").textContent);
// Column kinds: date, text (free-text filter), code, flag (●). Each row carries
// one extra, hidden element at the end: the alphaXiv URL for the title link.
const kinds = ["date", "text", "text", "text", "code"]
  .concat(Array(headers.length - 5).fill("flag"));
const widths = {1: "w-title", 2: "w-ja", 3: "w-co"};
const filters = [];
let sortCol = 0, sortDir = -1;

const headRow = document.getElementById("heads");
const filterRow = document.getElementById("filters");
headers.forEach((name, i) => {
  const th = document.createElement("th");
  th.textContent = name;
  th.className = "sort " + (widths[i] || (kinds[i] === "flag" ? "w-flag" : ""));
  th.addEventListener("click", () => {
    sortDir = sortCol === i ? -sortDir : (kinds[i] === "flag" ? -1 : 1);
    sortCol = i;
    render();
  });
  headRow.appendChild(th);

  const cell = document.createElement("th");
  let control = null;
  if (kinds[i] === "text") {
    control = document.createElement("input");
    control.type = "search";
    control.placeholder = "含む文字";
  } else {
    const values = kinds[i] === "flag" ? ["●", ""]
      : [...new Set(rows.map(r => r[i]))].sort().reverse();
    control = document.createElement("select");
    control.add(new Option("すべて", "\u0000"));
    values.forEach(v => control.add(new Option(v === "" ? "(空欄)" : v, v)));
  }
  if (control) {
    control.addEventListener("input", render);
    cell.appendChild(control);
  }
  filters[i] = control;
  filterRow.appendChild(cell);
});

function matches(row) {
  return filters.every((control, i) => {
    if (!control) return true;
    if (control.tagName === "SELECT") return control.value === "\u0000" || row[i] === control.value;
    const query = control.value.trim().toLowerCase();
    return !query || row[i].toLowerCase().includes(query);
  });
}

function link(href, text) {
  const a = document.createElement("a");
  a.href = href; a.textContent = text; a.target = "_blank"; a.rel = "noopener";
  return a;
}

function render() {
  const shown = rows.filter(matches).sort((a, b) =>
    sortDir * a[sortCol].localeCompare(b[sortCol], "ja", {numeric: true}));
  const body = document.createElement("tbody");
  body.id = "rows";
  for (const row of shown) {
    const tr = body.insertRow();
    headers.forEach((_, i) => {
      const td = tr.insertCell();
      if (i === 1) td.appendChild(link(row[row.length - 1], row[i]));  // title opens alphaXiv
      else td.textContent = row[i];
      if (kinds[i] === "code" || kinds[i] === "flag") td.className = "c";
      else if (kinds[i] === "date") td.className = "nw";
    });
  }
  document.getElementById("rows").replaceWith(body);
  headRow.querySelectorAll("th").forEach((th, i) => {
    th.classList.toggle("asc", i === sortCol && sortDir > 0);
    th.classList.toggle("desc", i === sortCol && sortDir < 0);
  });
  document.getElementById("count").textContent = `${rows.length} 件中 ${shown.length} 件を表示`;
}

document.getElementById("reset").addEventListener("click", () => {
  filters.forEach(control => { if (control) control.value = control.tagName === "SELECT" ? "\u0000" : ""; });
  render();
});
render();
</script>
</body>
</html>
"""


def write_html(rows, path, title):
    """Single self-contained page: sticky header, per-column filters, sorting, links."""
    data = json.dumps(
        {
            "headers": HEADERS[:HTML_COLUMNS],
            "rows": [
                [row[0].isoformat(), *row[1:HTML_COLUMNS], row[-1]] for row in rows
            ],
        },
        ensure_ascii=False,
    ).replace("</", "<\\/")  # keep "</script>" inside titles from closing the tag
    page = HTML_TEMPLATE.replace("__TITLE__", html.escape(title)).replace("__DATA__", data)
    path.write_text(page, encoding="utf-8")


INDEX_TEMPLATE = """<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>arXiv cs.CV 論文一覧</title>
<style>
:root { --bg: #ffffff; --fg: #1f2328; --muted: #656d76; --line: #d0d7de; --link: #0969da; }
@media (prefers-color-scheme: dark) {
  :root { --bg: #0d1117; --fg: #e6edf3; --muted: #8d96a0; --line: #30363d; --link: #4493f8; }
}
body { margin: 0 auto; max-width: 720px; padding: 24px 16px; background: var(--bg); color: var(--fg);
  font: 15px/1.6 system-ui, "Segoe UI", "Yu Gothic UI", "Meiryo", sans-serif; }
h1 { font-size: 20px; margin: 0 0 4px; }
p { color: var(--muted); margin: 0 0 20px; }
h2 { font-size: 16px; margin: 20px 0 6px; padding-bottom: 4px; border-bottom: 1px solid var(--line); }
ul { margin: 0; padding-left: 20px; }
a { color: var(--link); }
.n { color: var(--muted); }
</style>
</head>
<body>
<h1>arXiv cs.CV 論文一覧</h1>
<p>実行日ごとの収集結果です。リンク先の表で絞り込みと並べ替えができます。</p>
__ITEMS__
</body>
</html>
"""


def write_index(result_dir):
    """result/index.html: links to every result page, grouped by run date (newest first)."""
    sections = []
    for day_dir in sorted((d for d in result_dir.iterdir() if d.is_dir()), reverse=True):
        items = []
        for page in sorted(day_dir.glob("*.html"), reverse=True):
            match = re.fullmatch(r"arxiv_csCV_(\d{4}-\d\d-\d\d)_to_(\d{4}-\d\d-\d\d)", page.stem)
            label = f"{match[1]} 〜 {match[2]} の投稿" if match else page.stem
            csv_path = page.with_suffix(".csv")
            if csv_path.exists():
                with csv_path.open(encoding="utf-8-sig", newline="") as stream:
                    count = max(sum(1 for _ in csv.reader(stream)) - 1, 0)
                label += f' <span class="n">（{count} 件）</span>'
            href = urllib.parse.quote(f"{day_dir.name}/{page.name}")
            items.append(f'  <li><a href="{href}">{label}</a></li>')
        if items:
            sections.append(f"<h2>{html.escape(day_dir.name)} 実行</h2>\n<ul>\n"
                            + "\n".join(items) + "\n</ul>")
    body = "\n".join(sections) or "<p>まだ結果がありません。</p>"
    (result_dir / "index.html").write_text(
        INDEX_TEMPLATE.replace("__ITEMS__", body), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=parse_date, help="JST start date: YYYY-MM-DD")
    parser.add_argument("--end", type=parse_date, help="JST end date: YYYY-MM-DD (inclusive)")
    parser.add_argument("--days", type=int, default=3,
                        help="Days to collect, ending at --end, when --start is omitted (default 3)")
    parser.add_argument("--output", type=Path,
                        help="Output CSV path (default: result/<run date>/arxiv_csCV_<start>_to_<end>.csv "
                             "next to this script); the .xlsx and .html are written alongside")
    parser.add_argument("--no-translate", action="store_true",
                        help="Do not send titles to the external translation API")
    parser.add_argument("--html-interval", type=float, default=3.0,
                        help="Minimum seconds between arXiv HTML requests (default 3.0)")
    parser.add_argument("--index-only", action="store_true",
                        help="Only rebuild result/index.html from the existing results")
    args = parser.parse_args()
    if args.index_only:
        RESULT_DIR.mkdir(exist_ok=True)
        write_index(RESULT_DIR)
        print(f"Updated {(RESULT_DIR / 'index.html').resolve()}")
        return
    end = args.end or datetime.now(JST).date()
    if args.days < 1:
        parser.error("--days must be 1 or more")
    start = args.start or (end - timedelta(days=args.days - 1))
    if start > end:
        parser.error("--start must be on or before --end")
    run_date = datetime.now(JST).date()
    output = args.output or RESULT_DIR / str(run_date) / f"arxiv_csCV_{start}_to_{end}.csv"
    output.parent.mkdir(parents=True, exist_ok=True)

    try:
        papers = collect_entries(start, end)
    except OSError as error:
        parser.exit(1, f"arXiv OAI-PMH request failed ({error}). "
                       "If this is HTTP 429/503, wait several minutes and retry.\n")
    print(f"Found {len(papers)} cs.CV papers from {start} through {end} (JST).")
    if args.no_translate:
        for paper in papers:
            paper["ja_title"] = ""
    else:
        with ThreadPoolExecutor(max_workers=4) as pool:
            translations = {pool.submit(translate, p["title"]): p for p in papers}
            for future in as_completed(translations):
                translations[future]["ja_title"] = future.result()
    # arXiv asks for a single connection at a time, so fetch HTML pages sequentially.
    html_pages = {}
    for number, paper in enumerate(papers, 1):
        html_pages.update([fetch_html(paper["id"], args.html_interval)])
        if number % 50 == 0 or number == len(papers):
            print(f"Fetched HTML {number}/{len(papers)}", flush=True)

    rows = [
        [
            paper["submitted"].date(),  # v1 submission date (JST)
            paper["title"],
            paper["ja_title"],
            companies_from_html(html_pages[paper["id"]]),
            code_status(paper["summary"]),
            *classify(paper),
            paper["id"],
            f"https://arxiv.org/abs/{paper['id']}",
            f"https://www.alphaxiv.org/abs/{paper['id']}",
        ]
        for paper in papers
    ]
    with output.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(HEADERS)
        writer.writerows([[row[0].isoformat(), *row[1:]] for row in rows])
    print(f"Wrote {len(rows)} papers to {output.resolve()}")
    xlsx_output = output.with_suffix(".xlsx")
    write_xlsx(rows, xlsx_output)
    print(f"Wrote {len(rows)} papers to {xlsx_output.resolve()}")
    html_output = output.with_suffix(".html")
    write_html(rows, html_output, f"arXiv cs.CV {start} – {end}")
    print(f"Wrote {len(rows)} papers to {html_output.resolve()}")
    if RESULT_DIR.is_dir():
        write_index(RESULT_DIR)
        print(f"Updated {(RESULT_DIR / 'index.html').resolve()}")


if __name__ == "__main__":
    main()
