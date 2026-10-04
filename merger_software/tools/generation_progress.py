#!/usr/bin/env python3
"""Where the top-5 generation stopped, derived from disk rather than bookkeeping.

State is recomputed by scanning ast_merger_sonent_sols, so it stays correct even
if a batch is interrupted halfway. Each problem is in exactly one state:

  complete  five candidates + merged.py + uast_input.json
  partial   some candidates written, not all five, or no merged.py yet
  fetched   problem.json fetched, no candidates yet
  todo      nothing on disk

Order follows codeforces_data/problems_meta.json, which is the order the batches
walk, so "next" is simply the first problem that is not complete.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ast_merger_sonent_sols"
STATE = OUT / "GENERATION_PROGRESS.json"


def classify(pid: str) -> str:
    pdir = OUT / pid
    if not pdir.is_dir():
        return "todo"
    cands = [i for i in range(1, 6) if (pdir / f"candidate_{i}.py").exists()]
    if len(cands) == 5 and (pdir / "merged.py").exists() and (pdir / "uast_input.json").exists():
        return "complete"
    if cands:
        return "partial"
    if (pdir / "problem.json").exists():
        return "fetched"
    return "todo"


def build() -> dict:
    meta = json.loads((ROOT / "codeforces_data" / "problems_meta.json").read_text())
    order = [f"{q['contestId']}{q['index']}" for q in meta]
    ratings = {f"{q['contestId']}{q['index']}": q.get("rating") for q in meta}
    states = {pid: classify(pid) for pid in order}
    complete = [p for p in order if states[p] == "complete"]
    partial = [p for p in order if states[p] == "partial"]
    fetched = [p for p in order if states[p] == "fetched"]
    remaining = [p for p in order if states[p] != "complete"]
    return {
        "total_problems": len(order),
        "complete_count": len(complete),
        "remaining_count": len(remaining),
        "next_problem": remaining[0] if remaining else None,
        "next_index": order.index(remaining[0]) if remaining else None,
        "next_batch_of_10": remaining[:10],
        "partial_needs_finishing": partial,
        "fetched_awaiting_candidates": fetched,
        "complete": complete,
        "ratings": {p: ratings[p] for p in remaining[:10]},
    }


def main() -> int:
    state = build()
    STATE.write_text(json.dumps(state, indent=2))
    print(f"complete {state['complete_count']}/{state['total_problems']}"
          f"   remaining {state['remaining_count']}")
    if state["partial_needs_finishing"]:
        print(f"PARTIAL (finish these first): {' '.join(state['partial_needs_finishing'])}")
    if state["fetched_awaiting_candidates"]:
        print(f"fetched, no candidates yet: {' '.join(state['fetched_awaiting_candidates'])}")
    print(f"next: {state['next_problem']} (meta index {state['next_index']})")
    print("next batch of 10: " + " ".join(
        f"{p}({state['ratings'].get(p)})" for p in state["next_batch_of_10"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
