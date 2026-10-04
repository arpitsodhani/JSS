#!/usr/bin/env python3
"""Run one candidate file against the samples in problem.json (checker-aware)."""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from verify_sonnet_candidates import samples_for  # noqa: E402

PY = ROOT / ".venv" / "bin" / "python"


def run(pid, fname="candidate_1.py"):
    path = ROOT / "ast_merger_sonent_sols" / pid / fname
    ok = True
    for idx, (stdin, check) in enumerate(samples_for(pid), 1):
        res = subprocess.run([str(PY), str(path)], input=stdin, text=True,
                             capture_output=True, timeout=120)
        if res.returncode != 0:
            print(f"  {pid} {fname} sample {idx}: CRASH\n{res.stderr[-1200:]}")
            ok = False
            continue
        try:
            check(res.stdout)
        except AssertionError as exc:
            print(f"  {pid} {fname} sample {idx}: {exc}")
            ok = False
    print(("PASS " if ok else "FAIL ") + pid + " " + fname)
    return ok


if __name__ == "__main__":
    args = sys.argv[1:]
    fname = "candidate_1.py"
    if args and args[-1].endswith(".py"):
        fname = args.pop()
    raise SystemExit(0 if all([run(p, fname) for p in args]) else 1)
