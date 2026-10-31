"""Trial A: summarize abstracts into problem / method / advance with a local LLM.

Starts llama-server (llama.cpp) on the model, asks for JSON constrained by a schema,
and records the answer and the time per paper.

usage: python trial/llm_summary.py SERVER_BIN MODEL.gguf OUT.json [--ja]
"""
import argparse
import json
import subprocess
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent

SCHEMA = {
    "type": "object",
    "properties": {
        "problem": {"type": "string"},
        "method": {"type": "string"},
        "advance": {"type": "string"},
    },
    "required": ["problem", "method", "advance"],
    "additionalProperties": False,
}
PROMPT_EN = (
    "Summarize this computer vision paper using only its title and abstract.\n"
    "problem: the problem, or the limitation of existing work, that it addresses (one short sentence).\n"
    "method: what the paper proposes and how it works (one short sentence).\n"
    "advance: how it improves over prior work, with concrete numbers if the abstract gives them "
    "(one short sentence).\n"
    'If the abstract does not say it, write "Not stated". At most 30 words each. Answer in JSON.'
)
PROMPT_JA = (
    "次のコンピュータビジョン論文を、タイトルと要旨だけを根拠に日本語で要約してください。\n"
    "problem: 既存手法の課題・解決したい問題（短い1文）\n"
    "method: 提案する方法とその仕組み（短い1文）\n"
    "advance: 従来手法からの進化・改善点。数値があれば含める（短い1文）\n"
    "要旨に書かれていない項目は「記載なし」。各60字以内。JSONで答えてください。"
)


def post(url, body, timeout=900):
    request = urllib.request.Request(url, json.dumps(body).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("server")
    parser.add_argument("model")
    parser.add_argument("out")
    parser.add_argument("--ja", action="store_true")
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--port", type=int, default=8091)
    args = parser.parse_args()

    papers = json.load(open(HERE / "papers.json", encoding="utf-8"))
    server = subprocess.Popen(
        [args.server, "-m", args.model, "-t", str(args.threads), "-c", "4096",
         "--port", str(args.port), "-np", "1"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    load_start = time.time()
    try:
        for _ in range(300):
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{args.port}/health", timeout=2)
                break
            except Exception:
                time.sleep(1)
        load_sec = time.time() - load_start
        results, start = [], time.time()
        for paper in papers:
            began = time.time()
            body = {
                "messages": [
                    # "/no_think" turns off Qwen3's thinking mode; other models ignore it.
                    {"role": "system", "content": (PROMPT_JA if args.ja else PROMPT_EN) + " /no_think"},
                    {"role": "user", "content": f"Title: {paper['title']}\n\nAbstract: {paper['summary']}"},
                ],
                "temperature": 0,
                "max_tokens": 400,
                "response_format": {"type": "json_schema", "json_schema": {"name": "summary", "schema": SCHEMA}},
            }
            try:
                reply = post(f"http://127.0.0.1:{args.port}/v1/chat/completions", body)
                text = reply["choices"][0]["message"]["content"]
                usage = reply.get("usage", {})
                try:
                    summary = json.loads(text)
                except ValueError:
                    summary = {"raw": text}
            except Exception as error:  # keep going; the report shows the failure
                summary, usage = {"error": repr(error)}, {}
            results.append({
                "id": paper["id"],
                "summary": summary,
                "sec": round(time.time() - began, 1),
                "prompt_tokens": usage.get("prompt_tokens"),
                "completion_tokens": usage.get("completion_tokens"),
            })
            print(f"{results[-1]['sec']:6.1f}s {paper['title'][:70]}", flush=True)
        total = time.time() - start
    finally:
        server.terminate()
    json.dump({
        "model": Path(args.model).name,
        "lang": "ja" if args.ja else "en",
        "threads": args.threads,
        "load_sec": round(load_sec, 1),
        "sec_per_paper": round(total / len(papers), 1),
        "results": results,
    }, open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{Path(args.model).name} {'ja' if args.ja else 'en'}: {total / len(papers):.1f} s/paper")


if __name__ == "__main__":
    main()
