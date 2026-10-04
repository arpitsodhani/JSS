#!/usr/bin/env python3
"""Re-merge problems with the null-distribution/p-value adaptive theta,
without touching candidate_1..5.py. Reuses uast_input.json already on disk
(rebuilt fresh from the untouched candidates, same as run_sonnet_merge.py
would) and calls ast_merger_lang_agnostic/adaptive_theta.py merge with a
per-clause-role threshold instead of the fixed 0.60.

The old fixed-theta merged.py is preserved by the caller as
merged_theta060.py before this runs; this script writes merged.py fresh.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sonnet_clauses import split_clauses_full

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ast_merger_sonent_sols"
ADAPTIVE = ROOT / "ast_merger_lang_agnostic" / "adaptive_theta.py"
NULL_THETA = OUT / "null_theta.json"
PYTHON = ROOT / ".venv" / "bin" / "python"
if not PYTHON.exists():
    PYTHON = Path(sys.executable)


def build_uast_input(pid: str) -> Path:
    pdir = OUT / pid
    programs = []
    for i in range(1, 6):
        includes, clauses = split_clauses_full(pdir / f"candidate_{i}.py")
        programs.append({
            "id": f"P{i}",
            "includes": includes,
            "clauses": [
                {"clause_id": cid, "signature": sig or "python_block", "code": code}
                for cid, sig, code in clauses
            ],
        })
    path = pdir / "uast_input.json"
    path.write_text(json.dumps({"programs": programs}, indent=2))
    return path


def merge_one(pid: str, alpha_key: str) -> dict:
    pdir = OUT / pid
    inp = build_uast_input(pid)
    merged = pdir / "merged.py"
    report = pdir / "adaptive_theta_report.json"
    res = subprocess.run(
        [str(PYTHON), str(ADAPTIVE), "merge",
         "--input", str(inp), "--out", str(merged),
         "--null-theta", str(NULL_THETA), "--alpha-key", alpha_key,
         "--report", str(report)],
        cwd=str(ADAPTIVE.parent), text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, check=False,
    )
    ok = res.returncode == 0 and merged.exists()
    if ok:
        chk = subprocess.run([str(PYTHON), "-m", "py_compile", str(merged)],
                              text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ok = chk.returncode == 0
    row = {"problem": pid, "status": "merged" if ok else "merge-failed", "log": res.stdout}
    if report.exists():
        row["report"] = json.loads(report.read_text())
    return row


def main() -> int:
    args = sys.argv[1:]
    alpha_key = "alpha_0.02"
    if args and args[0].startswith("--alpha-key="):
        alpha_key = args[0].split("=", 1)[1]
        args = args[1:]
    pids = args
    rows = []
    for pid in pids:
        row = merge_one(pid, alpha_key)
        rows.append(row)
        avg = None
        if "report" in row:
            confs = [c["confidence"] for c in row["report"]["clauses"].values()]
            avg = sum(confs) / len(confs) if confs else None
        print(f"{row['status']:14s} {pid:8s} avg_confidence={avg}")
        if "report" in row:
            for cid, info in row["report"]["clauses"].items():
                print(f"    {cid:20s} role={info['role']:12s} theta={info['theta_used']:.3f} "
                      f"conf={info['confidence']:.2f} agree={info['agreement']:.3f} "
                      f"p={info['p_value_vs_null']}")
    return 0 if all(r["status"] == "merged" for r in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
