#!/usr/bin/env python3
"""Collect Codeforces verdicts for a batch submission run via the public API."""
from __future__ import annotations

import argparse
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://codeforces.com/api/user.status?handle={handle}&from=1&count={count}"

VERDICT_LABELS = {
    "OK": "Accepted",
    "WRONG_ANSWER": "Wrong answer",
    "TIME_LIMIT_EXCEEDED": "Time limit exceeded",
    "MEMORY_LIMIT_EXCEEDED": "Memory limit exceeded",
    "RUNTIME_ERROR": "Runtime error",
    "COMPILATION_ERROR": "Compilation error",
    "IDLENESS_LIMIT_EXCEEDED": "Idleness limit exceeded",
    "TESTING": "Testing",
}


def fetch_status(handle: str, count: int) -> list[dict]:
    for attempt in range(5):
        try:
            with urllib.request.urlopen(API.format(handle=handle, count=count), timeout=30) as fh:
                payload = json.load(fh)
            if payload.get("status") == "OK":
                return payload["result"]
        except Exception:  # noqa: BLE001 - API is rate limited, retry
            pass
        time.sleep(3 + attempt * 2)
    raise SystemExit("Could not read Codeforces user.status")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", help="Path to *_results.json from the batch submitter")
    parser.add_argument("--handle", default="__ParadigmShift")
    parser.add_argument("--count", type=int, default=400)
    parser.add_argument("--wait-for-testing", type=int, default=0,
                        help="Seconds to keep polling while submissions are still TESTING")
    args = parser.parse_args()

    results = json.loads(Path(args.results).read_text())
    wanted = {r["submissionId"]: r for r in results if r.get("submissionId")}

    deadline = time.time() + args.wait_for_testing
    while True:
        status = {str(s["id"]): s for s in fetch_status(args.handle, args.count)}
        pending = [sid for sid in wanted if status.get(sid, {}).get("verdict") in (None, "TESTING")]
        if not pending or time.time() > deadline:
            break
        print(f"{len(pending)} submissions still testing; waiting...", flush=True)
        time.sleep(20)

    rows = []
    for record in results:
        sid = record.get("submissionId")
        entry = status.get(str(sid)) if sid else None
        verdict = entry.get("verdict") if entry else None
        rows.append({
            "problem": record["problem"],
            "name": record.get("name"),
            "rating": record.get("rating"),
            "submissionId": sid,
            "verdict": verdict,
            "verdictLabel": VERDICT_LABELS.get(verdict, verdict or record.get("status")),
            "passedTestCount": entry.get("passedTestCount") if entry else None,
            "timeMs": entry.get("timeConsumedMillis") if entry else None,
            "status": record.get("status"),
        })

    out = Path(args.results).with_name(Path(args.results).stem + "_verdicts.json")
    out.write_text(json.dumps(rows, indent=2))

    counts: dict[str, int] = {}
    for row in rows:
        key = row["verdictLabel"] or "no submission"
        counts[key] = counts.get(key, 0) + 1
    print(f"{'PROBLEM':<10}{'RATING':<8}{'SUBMISSION':<12}VERDICT")
    for row in rows:
        print(f"{row['problem']:<10}{str(row['rating'] or '-'):<8}"
              f"{str(row['submissionId'] or '-'):<12}{row['verdictLabel']}")
    print("\nSummary:")
    for key, value in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {key}: {value}")
    accepted = counts.get("Accepted", 0)
    print(f"\nAccepted {accepted}/{len(rows)} ({accepted / max(len(rows), 1):.0%})")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
