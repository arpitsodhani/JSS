#!/usr/bin/env python3
"""Print the next problems to work on, in problems_meta.json order.

A problem is skipped when it already has merged.py or when it appears in the
deferred list kept in the scratchpad, so the batches march forward without
retrying the ones that were set aside.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFERRED = pathlib.Path("/tmp/claude-1000/-home-arpit-Desktop/5cebe473-e277-4837-b5ff-9beb14623b63/scratchpad/deferred.txt")

meta = json.loads((ROOT / "codeforces_data" / "problems_meta.json").read_text())
skip = set(DEFERRED.read_text().split())
out = ROOT / "ast_merger_sonent_sols"
want = int(sys.argv[1]) if len(sys.argv) > 1 else 12
picked = []
for q in meta:
    pid = f"{q['contestId']}{q['index']}"
    if pid in skip or (out / pid / "merged.py").exists():
        continue
    picked.append((pid, q.get("rating")))
    if len(picked) == want:
        break
print(" ".join(p for p, _ in picked))
print(" ".join(f"{p}({r})" for p, r in picked))
print("done:", sum(1 for d in out.iterdir() if (d / "merged.py").exists()))
