"""Trial B: pick the abstract's own sentences for problem / method / advance.

No model: each sentence is classified by cue words. Abstracts usually run
problem -> method -> results, so the method sentence anchors the other two.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent

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
    return [p.replace("\0", ".").strip() for p in parts if p.strip()]


def extract(abstract):
    sents = sentences(abstract)
    method_at = next((i for i, s in enumerate(sents) if METHOD.search(s)), None)
    if method_at is None:
        return {"problem": "", "method": "", "advance": ""}
    before, after = sents[:method_at], sents[method_at + 1:]
    problem = next((s for s in reversed(before) if PROBLEM.search(s)), before[-1] if before else "")
    # Prefer a result sentence with numbers; else the first comparative one.
    advance = next((s for s in after if ADVANCE.search(s) and re.search(r"\d", s)),
                   next((s for s in after if ADVANCE.search(s)), ""))
    return {"problem": problem, "method": sents[method_at], "advance": advance}


def main():
    papers = json.load(open(HERE / "papers.json", encoding="utf-8"))
    results = [{"id": p["id"], "summary": extract(p["summary"])} for p in papers]
    json.dump({"model": "extractive", "lang": "en", "results": results},
              open(HERE / "out" / "extractive.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
