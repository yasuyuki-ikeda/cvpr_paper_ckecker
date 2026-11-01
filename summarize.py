"""Summarize papers into problem / method / advance (English) with a local LLM.

Runs llama-server (llama.cpp) on a small open model on the CPU; no paid API.
Each answer is checked: an item that contains a number the abstract does not
have is replaced by the abstract's own sentence for that item (the model
sometimes invents results). The collector translates the items into Japanese.

usage:
    python summarize.py --server llama-server --model Qwen3-4B-Q4_K_M.gguf \
        --papers papers.json --shard 0 --shards 6 --out summaries-0.json
"""
import argparse
import json
import re
import subprocess
import time
import urllib.request

FIELDS = ("problem", "method", "advance")
NOT_STATED = "Not stated"
SCHEMA = {
    "type": "object",
    "properties": {field: {"type": "string"} for field in FIELDS},
    "required": list(FIELDS),
    "additionalProperties": False,
}
PROMPT = (
    "Summarize this computer vision paper using only its title and abstract.\n"
    "problem: the problem, or the limitation of existing work, that it addresses (one short sentence).\n"
    "method: what the paper proposes and how it works (one short sentence).\n"
    "advance: how it improves over prior work (one short sentence). Use only numbers that appear "
    "in the abstract; if it gives none, do not add any.\n"
    f'If the abstract does not say it, write "{NOT_STATED}". At most 30 words each. Answer in JSON.'
    " /no_think"  # turns off Qwen3's thinking mode
)

# Sentence picker used when the model's item cannot be trusted. Abstracts
# usually run problem -> method -> results, so the method sentence anchors the rest.
METHOD = re.compile(
    r"\b(?:we|this (?:paper|work|study)|in this (?:paper|work)|our (?:method|approach|framework|model))\b"
    r"[^.]{0,60}?\b(?:propose|present|introduce|develop|design|build|construct|curate|release)\w*", re.I)
PROBLEM = re.compile(
    r"\b(?:however|but|yet|despite|although|challeng\w*|limit\w*|struggl\w*|fail\w*|suffer\w*|"
    r"remain\w*|lack\w*|costly|expensive|difficult\w*|bottleneck\w*|gap|issue\w*|problem\w*|"
    r"hinder\w*|unclear|insufficient|underexplored|overlook\w*|bias\w*)\b", re.I)
ADVANCE = re.compile(
    r"\b(?:outperform\w*|surpass\w*|state-of-the-art|sota|improv\w*|better than|compared (?:to|with)|"
    r"gains?|faster|speed-?up|reduc\w*|achiev\w*|exceed\w*|superior|unlike|competitive|"
    r"while (?:using|requiring))\b|\d+(?:\.\d+)?\s?(?:%|x\b|×|times)", re.I)


def sentences(text):
    """Split on sentence ends, keeping abbreviations like "e.g." together."""
    text = re.sub(r"\b(e\.g|i\.e|et al|vs|etc)\.", lambda m: m.group(0).replace(".", "\0"), text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(\[])", text)
    return [part.replace("\0", ".").strip() for part in parts if part.strip()]


def extract(abstract):
    """The abstract's own problem / method / advance sentences ("" when not found)."""
    sents = sentences(abstract)
    method_at = next((i for i, s in enumerate(sents) if METHOD.search(s)), None)
    if method_at is None:
        return dict.fromkeys(FIELDS, "")
    before, after = sents[:method_at], sents[method_at + 1:]
    problem = next((s for s in reversed(before) if PROBLEM.search(s)), before[-1] if before else "")
    # Prefer a result sentence with numbers; else the first comparative one.
    advance = next((s for s in after if ADVANCE.search(s) and re.search(r"\d", s)),
                   next((s for s in after if ADVANCE.search(s)), ""))
    return {"problem": problem, "method": sents[method_at], "advance": advance}


def numbers(text):
    """Standalone figures ("14.2", "30"); digits inside names like F1, 3D, v2 or I$^2$ do not count."""
    return set(re.findall(r"(?<![\w.^$])\d+(?:\.\d+)?(?![\w$])", text))


def without_numbers(text, invented):
    """Drop the invented figures ("by 14.2%", "of 30 points") from the model's sentence."""
    for number in invented:
        text = re.sub(
            r"\s*\b(?:by|of|to|up to|about|around|nearly|over)?\s*(?<![\w.^$])" + re.escape(number)
            + r"\s*(?:%|percentage points?|points?|pp\b|x\b|×|times)?", "", text)
    return re.sub(r"\s+([,.])", r"\1", text).strip()


def checked(answer, paper):
    """Replace items with invented numbers, or missing items, by the abstract's sentences."""
    source = numbers(f"{paper['title']} {paper['summary']}")
    fallback = None
    result = {}
    for field in FIELDS:
        text = str(answer.get(field, "")).strip()
        invented = numbers(text) - source
        if not text or invented:
            fallback = fallback or extract(paper["summary"])
            # The abstract's sentence if one was found, else the model's without the figures.
            text = fallback[field] or (without_numbers(text, invented) if text else "") or NOT_STATED
        result[field] = text
    return result


def post(url, body, timeout=900):
    request = urllib.request.Request(url, json.dumps(body).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read())


def summarize(port, paper):
    body = {
        "messages": [
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": f"Title: {paper['title']}\n\nAbstract: {paper['summary']}"},
        ],
        "temperature": 0,
        "max_tokens": 400,
        "response_format": {"type": "json_schema", "json_schema": {"name": "summary", "schema": SCHEMA}},
    }
    try:
        reply = post(f"http://127.0.0.1:{port}/v1/chat/completions", body)
        answer = json.loads(reply["choices"][0]["message"]["content"])
    except Exception as error:  # a failed paper falls back to the sentence picker
        print(f"  model failed: {error!r}", flush=True)
        answer = {}
    return checked(answer, paper)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--server", required=True, help="llama-server executable")
    parser.add_argument("--model", required=True, help="GGUF model file")
    parser.add_argument("--papers", required=True, help="papers JSON from collect_arxiv_cv.py --save-papers")
    parser.add_argument("--out", required=True)
    parser.add_argument("--shard", type=int, default=0)
    parser.add_argument("--shards", type=int, default=1)
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--port", type=int, default=8091)
    args = parser.parse_args()

    papers = json.load(open(args.papers, encoding="utf-8"))[args.shard::args.shards]
    server = subprocess.Popen(
        [args.server, "-m", args.model, "-t", str(args.threads), "-c", "4096",
         "--port", str(args.port), "-np", "1"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    summaries = {}
    try:
        for _ in range(300):
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{args.port}/health", timeout=2)
                break
            except Exception:
                time.sleep(1)
        start = time.time()
        for number, paper in enumerate(papers, 1):
            summaries[paper["id"]] = summarize(args.port, paper)
            if number % 10 == 0 or number == len(papers):
                rate = (time.time() - start) / number
                print(f"Summarized {number}/{len(papers)} ({rate:.1f} s/paper)", flush=True)
    finally:
        server.terminate()
        json.dump(summaries, open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
