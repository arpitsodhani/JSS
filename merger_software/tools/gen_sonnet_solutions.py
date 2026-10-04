#!/usr/bin/env python3
"""Generate Python solutions for Codeforces problems with a Sonnet model.

Each problem statement (from codeforces_data/statements) is handed to the
`claude` CLI running the requested model with no tools, and the fenced Python
block in the reply is written to sonnet_gen/<problem-id>/solution.py.

The reference solutions in codeforces_sols/ are deliberately never shown to the
model: this measures what the model produces from the statement alone.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATEMENTS = ROOT / "codeforces_data" / "statements"
OUT_DIR = ROOT / "sonnet_gen"

PRINT_LOCK = threading.Lock()

PROMPT_TEMPLATE = """You are solving a Codeforces problem. Write a complete, correct, efficient Python 3 solution.

Problem id: {pid}
Title: {title}
Rating: {rating}
Tags: {tags}
Time limit: {time_limit}
Memory limit: {mem_limit}

--- STATEMENT ---
{statement}
--- END STATEMENT ---

Sample tests (NOTE: newlines inside each sample input were lost during dataset
scraping, so the input lines appear concatenated; infer the intended line
structure from the statement):
{samples}

Requirements:
- Read from standard input, write to standard output. No prompts, no extra text.
- Plain Python 3 standard library only. It will run on PyPy 3 on Codeforces.
- Use fast I/O (sys.stdin.buffer.read()) and keep within the time limit for the
  maximum constraints stated in the problem.
- Set a higher recursion limit or use an iterative formulation if recursion is deep.
- Handle multiple test cases if the problem has them.

Reply with ONLY one fenced code block containing the full program:

```python
<your solution>
```
"""


def load_problems(limit: int) -> list[dict]:
    meta = json.loads((ROOT / "codeforces_data" / "problems_meta.json").read_text())
    return meta[:limit]


def statement_path(problem: dict) -> Path:
    return STATEMENTS / f"{problem['contestId']}_{problem['index']}.json"


def build_prompt(problem: dict) -> str:
    pid = f"{problem['contestId']}{problem['index']}"
    data = json.loads(statement_path(problem).read_text())
    samples = []
    for i, sample in enumerate(data.get("samples", []), 1):
        samples.append(
            f"Sample {i} input:\n{sample.get('input', '')}\n"
            f"Sample {i} output:\n{sample.get('output', '')}"
        )
    return PROMPT_TEMPLATE.format(
        pid=pid,
        title=data.get("title") or problem["name"],
        rating=problem.get("rating", "unknown"),
        tags=", ".join(problem.get("tags", [])),
        time_limit=data.get("time_limit", "unknown"),
        mem_limit=data.get("mem_limit", "unknown"),
        statement=data.get("statement", ""),
        samples="\n\n".join(samples) if samples else "(none available)",
    )


CODE_BLOCK = re.compile(r"```(?:python|py)?\s*\n(.*?)```", re.DOTALL)


def extract_code(reply: str) -> str | None:
    blocks = CODE_BLOCK.findall(reply)
    if not blocks:
        return None
    return max(blocks, key=len).strip() + "\n"


def call_model(prompt: str, model: str, timeout: int) -> str:
    result = subprocess.run(
        [
            "claude",
            "-p",
            prompt,
            "--model",
            model,
            "--allowedTools",
            "",
            "--output-format",
            "text",
        ],
        cwd=str(ROOT),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )
    if result.returncode != 0:
        detail = (result.stderr.strip() or result.stdout.strip())[:400]
        raise RuntimeError(f"exit {result.returncode}: {detail or 'no output'}")
    return result.stdout


def compiles(path: Path) -> tuple[bool, str]:
    result = subprocess.run(
        [sys.executable, "-m", "py_compile", str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return result.returncode == 0, result.stderr.strip()[:300]


def generate(problem: dict, model: str, timeout: int, force: bool) -> dict:
    pid = f"{problem['contestId']}{problem['index']}"
    out_dir = OUT_DIR / pid
    solution = out_dir / "solution.py"
    if solution.exists() and not force:
        return {"problem": pid, "status": "cached"}

    out_dir.mkdir(parents=True, exist_ok=True)
    prompt = build_prompt(problem)
    last_error = ""
    for attempt in range(1, 5):
        if attempt > 1:
            time.sleep(min(15 * 2 ** (attempt - 2), 120))
        try:
            reply = call_model(prompt, model, timeout)
        except Exception as exc:  # noqa: BLE001 - report and retry with backoff
            last_error = f"model call failed: {exc}"
            continue
        (out_dir / f"raw_attempt{attempt}.md").write_text(reply)
        code = extract_code(reply)
        if not code:
            last_error = "no fenced code block in reply"
            continue
        solution.write_text(code)
        ok, err = compiles(solution)
        if ok:
            return {"problem": pid, "status": "ok", "attempt": attempt, "bytes": len(code)}
        last_error = f"syntax error: {err}"
        solution.unlink(missing_ok=True)

    (out_dir / "error.txt").write_text(last_error)
    return {"problem": pid, "status": "failed", "error": last_error}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--model", default="claude-sonnet-4-5-20250929")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--only", nargs="*", help="Restrict to these problem ids")
    args = parser.parse_args()

    problems = load_problems(args.limit)
    if args.only:
        wanted = set(args.only)
        problems = [p for p in problems if f"{p['contestId']}{p['index']}" in wanted]

    missing = [p for p in problems if not statement_path(p).exists()]
    for problem in missing:
        print(f"WARN missing statement for {problem['contestId']}{problem['index']}")
    problems = [p for p in problems if statement_path(p).exists()]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results: list[dict] = []
    done = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [
            pool.submit(generate, problem, args.model, args.timeout, args.force)
            for problem in problems
        ]
        for future in futures:
            record = future.result()
            results.append(record)
            done += 1
            with PRINT_LOCK:
                print(f"[{done}/{len(problems)}] {record['problem']}: {record['status']} "
                      f"{record.get('error', '')}".rstrip(), flush=True)

    summary = OUT_DIR / "generation_summary.json"
    summary.write_text(json.dumps({"model": args.model, "results": results}, indent=2))
    failed = [r for r in results if r["status"] == "failed"]
    print(f"\nGenerated {len(results) - len(failed)}/{len(results)}; failed: "
          f"{[r['problem'] for r in failed]}")
    print(f"Summary: {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
