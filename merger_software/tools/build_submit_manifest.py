#!/usr/bin/env python3
"""Build a submission manifest for the batch Codeforces submitter."""
from __future__ import annotations

import argparse
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://codeforces.com/api/user.status?handle={handle}&from=1&count=10000"


def attempted_problems(handle: str) -> set[str]:
    """Every problem this account has already submitted to, at least once."""
    with urllib.request.urlopen(API.format(handle=handle), timeout=60) as fh:
        payload = json.load(fh)
    if payload.get("status") != "OK":
        raise SystemExit(f"Codeforces API error: {payload.get('comment')}")
    return {
        f"{s['problem']['contestId']}{s['problem']['index']}"
        for s in payload["result"]
        if s["problem"].get("contestId")
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--src", default="sonnet_gen", help="Directory holding <pid>/solution.py")
    parser.add_argument("--out", default="submissions/manifest_sonnet_100.json")
    parser.add_argument("--skip", nargs="*", default=[], help="Problem ids to leave out")
    parser.add_argument("--skip-attempted", action="store_true",
                        help="Also skip every problem already submitted on the account")
    parser.add_argument("--handle", default="__ParadigmShift")
    args = parser.parse_args()

    meta = json.loads((ROOT / "codeforces_data" / "problems_meta.json").read_text())
    skip = set(args.skip)
    if args.skip_attempted:
        already = attempted_problems(args.handle)
        skip |= already
        print(f"Skipping {len(already)} problems already attempted by {args.handle}")
    entries = []
    missing = []
    for problem in meta[: args.limit]:
        pid = f"{problem['contestId']}{problem['index']}"
        if pid in skip:
            continue
        path = ROOT / args.src / pid / "solution.py"
        if not path.exists():
            missing.append(pid)
            continue
        entries.append({
            "problem": pid,
            "path": str(path.relative_to(ROOT)),
            "rating": problem.get("rating"),
            "name": problem["name"],
        })

    out = ROOT / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(entries, indent=2))
    print(f"Wrote {out} with {len(entries)} entries")
    if missing:
        print(f"Missing solutions ({len(missing)}): {missing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
