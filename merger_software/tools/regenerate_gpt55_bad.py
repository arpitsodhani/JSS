#!/usr/bin/env python3
"""Regenerate contaminated gpt_5.5_sol solutions from statements only.

This script never reads codeforces_sols or sonnet_gen as solution sources. It
only uses sonnet_gen for byte-comparison rejection, so outputs cannot remain
borrowed from the Sonnet folder.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "codeforces" / "codeforces_data" / "problems_meta.json"
STATEMENTS = ROOT / "codeforces" / "codeforces_data" / "statements"
OUT = ROOT / "gpt_5.5_sol"
SONNET = ROOT / "sonnet_gen"
PROGRESS = OUT / "_gpt55_regen_progress.json"

CODE_BLOCK = re.compile(r"```(?:python|py)?\s*\n(.*?)```", re.DOTALL | re.I)
PLACEHOLDER = re.compile(
    r"(?i)(#\s*todo|todo\b|fixme\b|stub\b|placeholder\b|"
    r"left\s+to\s+implement|implement\s+me|not\s+implemented)"
)
PRINT_LOCK = threading.Lock()


def pid(problem: dict) -> str:
    return f"{problem['contestId']}{problem['index']}"


def same_bytes(a: Path, b: Path) -> bool:
    if not a.exists() or not b.exists() or a.stat().st_size != b.stat().st_size:
        return False
    return a.read_bytes() == b.read_bytes()


def load_meta() -> list[dict]:
    return json.loads(META.read_text())


def bad_pids(problems: list[dict]) -> list[str]:
    bad: list[str] = []
    for problem in problems:
        name = pid(problem)
        path = OUT / name / "solution.py"
        sonnet = SONNET / name / "solution.py"
        if not path.exists():
            bad.append(name)
            continue
        text = path.read_text(errors="replace")
        if PLACEHOLDER.search(text) or same_bytes(path, sonnet):
            bad.append(name)
    return bad


def load_done() -> set[str]:
    if not PROGRESS.exists():
        return set()
    try:
        data = json.loads(PROGRESS.read_text())
    except json.JSONDecodeError:
        return set()
    return {name for name, rec in data.get("problems", {}).items() if rec.get("status") == "ok"}


def record(name: str, status: str, **extra: object) -> None:
    with PRINT_LOCK:
        try:
            data = json.loads(PROGRESS.read_text()) if PROGRESS.exists() else {}
        except json.JSONDecodeError:
            data = {}
        problems = data.setdefault("problems", {})
        problems[name] = {"status": status, "updated": time.strftime("%Y-%m-%d %H:%M:%S"), **extra}
        tmp = PROGRESS.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, indent=2, sort_keys=True))
        tmp.replace(PROGRESS)


def statement_for(problem: dict) -> str:
    data = json.loads((STATEMENTS / f"{problem['contestId']}_{problem['index']}.json").read_text())
    samples = "\n\n".join(
        f"Sample {i} input:\n{s.get('input', '')}\nSample {i} output:\n{s.get('output', '')}"
        for i, s in enumerate(data.get("samples", []), 1)
    )
    return f"""Problem id: {pid(problem)}
Title: {data.get("title") or problem["name"]}
Rating: {problem.get("rating", "unknown")}
Tags: {", ".join(problem.get("tags", []))}
Time limit: {data.get("time_limit", "unknown")}
Memory limit: {data.get("mem_limit", "unknown")}

Statement:
{data.get("statement", "")}

Input:
{data.get("input_spec", "")}

Output:
{data.get("output_spec", "")}

Samples:
{samples or "(none)"}
"""


def prompt(problem: dict) -> str:
    return f"""Solve this Codeforces problem from the statement only.

Write a complete, correct, efficient Python 3 program.

Rules:
- Use only standard input and standard output.
- No prompts, comments, markdown explanation, TODOs, stubs, placeholders, or omitted parts.
- Implement the full algorithm required by the problem description.
- Do not inspect or copy any existing solution files in this repository.
- Reply with ONLY one fenced python code block containing the full program.

{statement_for(problem)}
"""


def extract_code(text: str) -> str:
    blocks = CODE_BLOCK.findall(text)
    if not blocks:
        raise RuntimeError("no fenced python code block")
    return max(blocks, key=len).strip() + "\n"


def compiles(path: Path) -> tuple[bool, str]:
    result = subprocess.run(
        [sys.executable, "-m", "py_compile", str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return result.returncode == 0, result.stderr.strip()[:400]


def generate_one(problem: dict, model: str, timeout: int, attempts: int) -> dict:
    name = pid(problem)
    out_dir = OUT / name
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "solution.py"
    sonnet = SONNET / name / "solution.py"
    last_error = ""
    for attempt in range(1, attempts + 1):
        with tempfile.NamedTemporaryFile(prefix=f"gpt55_{name}_", suffix=".md", delete=False) as fh:
            last_msg = Path(fh.name)
        try:
            result = subprocess.run(
                [
                    "codex",
                    "exec",
                    "--model",
                    model,
                    "--cd",
                    str(ROOT),
                    "--sandbox",
                    "read-only",
                    "--dangerously-bypass-approvals-and-sandbox",
                    "--output-last-message",
                    str(last_msg),
                    prompt(problem),
                ],
                cwd=str(ROOT),
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
                check=False,
            )
            if result.returncode != 0:
                detail = (result.stderr.strip() or result.stdout.strip())[-800:]
                raise RuntimeError(f"codex exit {result.returncode}: {detail}")
            code = extract_code(last_msg.read_text(errors="replace"))
            if PLACEHOLDER.search(code):
                raise RuntimeError("generated code contains placeholder marker")
            tmp = dest.with_suffix(".tmp.py")
            tmp.write_text(code)
            ok, err = compiles(tmp)
            if not ok:
                tmp.unlink(missing_ok=True)
                raise RuntimeError(f"syntax error: {err}")
            tmp.replace(dest)
            if same_bytes(dest, sonnet):
                dest.unlink(missing_ok=True)
                raise RuntimeError("generated code is still identical to sonnet_gen")
            record(name, "ok", attempt=attempt, bytes=len(code))
            return {"problem": name, "status": "ok", "attempt": attempt, "bytes": len(code)}
        except Exception as exc:  # noqa: BLE001 - retry and persist error
            last_error = str(exc)
            record(name, "pending", attempt=attempt, error=last_error[:800])
            time.sleep(min(10 * attempt, 60))
        finally:
            last_msg.unlink(missing_ok=True)
    record(name, "failed", error=last_error[:800])
    return {"problem": name, "status": "failed", "error": last_error}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="gpt-5.5")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--only", nargs="*")
    parser.add_argument("--force", action="store_true", help="Regenerate selected pids even if progress says ok")
    args = parser.parse_args()

    problems = load_meta()
    by_pid = {pid(problem): problem for problem in problems}
    targets = args.only or bad_pids(problems)
    if args.limit:
        targets = targets[: args.limit]
    done = set() if args.force else load_done()
    targets = [name for name in targets if name not in done]

    print(f"targets: {len(targets)}; model: {args.model}; workers: {args.workers}", flush=True)
    if not targets:
        return 0

    completed = 0
    failed: list[str] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(generate_one, by_pid[name], args.model, args.timeout, args.attempts) for name in targets]
        for future in as_completed(futures):
            rec = future.result()
            completed += 1
            if rec["status"] != "ok":
                failed.append(rec["problem"])
            with PRINT_LOCK:
                print(
                    f"progress: {completed}/{len(targets)} regenerated; "
                    f"{rec['problem']}: {rec['status']}",
                    flush=True,
                )
    if failed:
        print(f"failed: {failed}", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
