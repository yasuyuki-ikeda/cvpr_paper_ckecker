"""Build trial/out/report.md: every variant's 【課題】【方法】【従来からの進化】 side by side.

English answers are translated with the collector's translation service, as the
production version would do.
"""
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from collect_arxiv_cv import translate  # noqa: E402

FIELDS = [("problem", "課題"), ("method", "方法"), ("advance", "従来からの進化")]


def main():
    papers = json.load(open(HERE / "papers.json", encoding="utf-8"))
    runs = [json.load(open(path, encoding="utf-8")) for path in sorted((HERE / "out").glob("*.json"))]
    runs.sort(key=lambda run: (run["model"] != "extractive", run["model"], run["lang"]))

    # Translate every English answer once.
    texts = {s for run in runs if run["lang"] == "en" for r in run["results"]
             for s in (r["summary"].get(k, "") for k, _ in FIELDS) if s and s != "Not stated"}
    with ThreadPoolExecutor(max_workers=4) as pool:
        ja = dict(zip(texts, pool.map(translate, texts)))

    def show(run, value):
        if not value:
            return "（空欄）"
        if value == "Not stated":
            return "記載なし"
        return ja.get(value, value) if run["lang"] == "en" else value

    lines = ["# 要約の試験結果", "",
             "| 方式 | 言語 | 1 本あたり | モデル読み込み | 形式どおりの答え |", "|---|---|---|---|---|"]
    for run in runs:
        ok = sum(all(k in r["summary"] for k, _ in FIELDS) for r in run["results"])
        lines.append(f"| {run['model']} | {run['lang']} | {run.get('sec_per_paper', 0)} 秒 "
                     f"| {run.get('load_sec', '-')} 秒 | {ok}/{len(run['results'])} |")
    lines.append("")
    for index, paper in enumerate(papers, 1):
        lines += [f"## {index}. {paper['title']}", "",
                  f"https://arxiv.org/abs/{paper['id']}", "",
                  "<details><summary>要旨（原文）</summary>", "", paper["summary"], "", "</details>", ""]
        for run in runs:
            result = next(r for r in run["results"] if r["id"] == paper["id"])
            summary = result["summary"]
            sec = f"（{result['sec']} 秒）" if "sec" in result else ""
            lines.append(f"**{run['model']} / {run['lang']}**{sec}")
            if not all(k in summary for k, _ in FIELDS):
                lines += ["", f"- 失敗: `{json.dumps(summary, ensure_ascii=False)[:300]}`", ""]
                continue
            lines += [""] + [f"- 【{label}】{show(run, summary[key])}" for key, label in FIELDS] + [""]
    (HERE / "out" / "report.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
