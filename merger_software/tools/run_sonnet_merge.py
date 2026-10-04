#!/usr/bin/env python3
"""Build uast_input.json for each problem and run the clause-wise UAST merger."""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sonnet_clauses import split_clauses_full

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ast_merger_sonent_sols"
MERGER = ROOT / "ast_merger_lang_agnostic" / "evaluate_clauses.py"
PYTHON = ROOT / ".venv" / "bin" / "python"
if not PYTHON.exists():
    PYTHON = Path(sys.executable)


def build_uast_input(pid: str) -> Path:
    pdir = OUT / pid
    programs = []
    for i in range(1, 6):
        includes, clauses = split_clauses_full(pdir / f"candidate_{i}.py")
        programs.append(
            {
                "id": f"P{i}",
                "includes": includes,
                "clauses": [
                    {"clause_id": cid, "signature": sig or "python_block", "code": code}
                    for cid, sig, code in clauses
                ],
            }
        )
    path = pdir / "uast_input.json"
    path.write_text(json.dumps({"programs": programs}, indent=2))
    return path


def merge_one(pid: str, timeout: int = 900) -> dict:
    pdir = OUT / pid
    inp = build_uast_input(pid)
    merged = pdir / "merged.py"
    started = time.monotonic()
    try:
        res = subprocess.run(
            [str(PYTHON), str(MERGER), "--lang", "python", "--input", str(inp),
             "--out", str(merged), "--out-trees", str(pdir / "trees.txt")],
            cwd=str(MERGER.parent), text=True, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, timeout=timeout, check=False,
        )
        log = res.stdout
        rc = res.returncode
    except subprocess.TimeoutExpired as exc:
        log = (exc.stdout or "") if isinstance(exc.stdout, str) else ""
        log += f"\nmerge timed out after {timeout}s\n"
        rc = -1
    elapsed = round(time.monotonic() - started, 2)
    (pdir / "merge.log").write_text(log)
    status = "merged" if rc == 0 and merged.exists() else "merge-failed"
    if status == "merged":
        chk = subprocess.run([str(PYTHON), "-m", "py_compile", str(merged)],
                             text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if chk.returncode != 0:
            status = "merge-uncompilable"
    average = ""
    per_clause = []
    for line in log.splitlines():
        stripped = line.strip()
        if stripped.startswith("Average Confidence:"):
            average = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Clause "):
            per_clause.append(stripped)
    return {
        "problem": pid,
        "status": status,
        "seconds": elapsed,
        "clauses": len(per_clause),
        "average_confidence": average,
        "per_clause": per_clause,
    }


def main() -> int:
    # A directory with a fetched problem.json but no candidates yet is a problem
    # that is still to be written; skip it instead of aborting the whole run.
    pids = sys.argv[1:] or sorted(
        p.name for p in OUT.iterdir()
        if p.is_dir() and p.name != "codeforces_data" and (p / "candidate_1.py").exists()
    )
    rows = []
    for pid in pids:
        row = merge_one(pid)
        rows.append(row)
        print(f"{row['status']:16s} {pid:8s} {row['clauses']} clauses  "
              f"avg confidence {row['average_confidence']}  {row['seconds']:.2f}s", flush=True)
        for line in row["per_clause"]:
            print(f"    {line}", flush=True)
    (OUT / "merge_summary.json").write_text(json.dumps(rows, indent=2))
    return 0 if all(r["status"] == "merged" for r in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
