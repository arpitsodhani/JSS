#!/usr/bin/env python3
"""Submit gpt_5.5_sol batches and reconcile Codeforces verdicts.

The existing browser submitter sometimes reports "submitted" after landing on a
status page without capturing an ID. This wrapper treats the Codeforces API as
authoritative, retries API-unconfirmed submissions, and separates problems whose
submit form has no Python language option.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "codeforces" / "codeforces_data" / "problems_meta.json"
SOL = ROOT / "gpt_5.5_sol"
SUBMISSIONS = ROOT / "submissions"
LOGS = ROOT / "logs"
SUBMITTER = ROOT / "scripts" / "submit_batch_codeforces.mjs"

LABELS = {
    "OK": "Accepted",
    "WRONG_ANSWER": "Wrong answer",
    "TIME_LIMIT_EXCEEDED": "Time limit exceeded",
    "MEMORY_LIMIT_EXCEEDED": "Memory limit exceeded",
    "RUNTIME_ERROR": "Runtime error",
    "COMPILATION_ERROR": "Compilation error",
    "IDLENESS_LIMIT_EXCEEDED": "Idleness limit exceeded",
    "PARTIAL": "Partial",
    "TESTING": "Testing",
}


def log(message: str) -> None:
    print(time.strftime("[%Y-%m-%d %H:%M:%S]"), message, flush=True)


def pid(problem: dict) -> str:
    return f"{problem['contestId']}{problem['index']}"


def run_submit(manifest: Path, delay: int, log_path: Path) -> Path:
    cmd = ["node", str(SUBMITTER), "--delay", str(delay), str(manifest)]
    log(f"Running: {' '.join(cmd)}")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w") as lf:
        proc = subprocess.Popen(
            cmd,
            cwd=str(ROOT),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
        )
        assert proc.stdout is not None
        for line in proc.stdout:
            print(line, end="", flush=True)
            lf.write(line)
            lf.flush()
        rc = proc.wait()
    if rc != 0:
        raise RuntimeError(f"submitter exited {rc} for {manifest}")
    return manifest.with_name(manifest.stem + "_results.json")


def fetch_status(handle: str, count: int) -> list[dict]:
    api = f"https://codeforces.com/api/user.status?handle={handle}&from=1&count={count}"
    for attempt in range(8):
        try:
            with urllib.request.urlopen(api, timeout=30) as fh:
                payload = json.load(fh)
            if payload.get("status") == "OK":
                return payload["result"]
        except Exception:
            pass
        time.sleep(3 + attempt * 2)
    raise RuntimeError("Could not fetch Codeforces user.status")


def latest_for(problems: set[str], handle: str, lower_bound: int, count: int) -> dict[str, dict]:
    latest: dict[str, dict] = {}
    for sub in fetch_status(handle, count):
        problem = sub["problem"]
        name = f"{problem.get('contestId')}{problem.get('index')}"
        if name in problems and sub.get("creationTimeSeconds", 0) >= lower_bound and name not in latest:
            latest[name] = sub
    return latest


def write_manifest(entries: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(entries, indent=2))


def reconcile(
    manifest: list[dict],
    initial_results: list[dict],
    form_retry_results: list[dict],
    unconfirmed_retry_results: list[dict],
    handle: str,
    lower_bound: int,
    api_count: int,
    out: Path,
) -> dict:
    wanted = {entry["problem"] for entry in manifest}
    unavailable = {r["problem"] for r in form_retry_results if r.get("status") == "error"}
    initial_by_pid = {r["problem"]: r for r in initial_results}
    rejected = {
        r["problem"]: r.get("error")
        for r in initial_results
        if r.get("status") == "rejected"
    }

    expected = wanted - unavailable - set(rejected)
    latest: dict[str, dict] = {}
    for attempt in range(30):
        latest = latest_for(wanted, handle, lower_bound, api_count)
        pending = [
            name
            for name in expected
            if name not in latest or latest[name].get("verdict") in (None, "TESTING")
        ]
        log(f"API poll {attempt + 1}: matched {len(latest)}/{len(expected)}, pending {len(pending)}")
        if not pending:
            break
        time.sleep(20)

    rows = []
    for entry in manifest:
        name = entry["problem"]
        sub = latest.get(name)
        initial = initial_by_pid.get(name, {})
        if name in unavailable:
            status = "unavailable-python"
            label = "unavailable-python"
            error = "Could not find a Python language option on the submit form."
        elif name in rejected and not sub:
            status = "rejected"
            label = "rejected"
            error = rejected[name]
        elif sub:
            status = "submitted"
            label = LABELS.get(sub.get("verdict"), sub.get("verdict") or "submitted")
            error = None
        else:
            status = "unconfirmed"
            label = "unconfirmed"
            error = initial.get("error")
        rows.append(
            {
                "problem": name,
                "name": entry.get("name"),
                "rating": entry.get("rating"),
                "status": status,
                "submitError": error,
                "submissionId": sub.get("id") if sub else None,
                "creationTimeSeconds": sub.get("creationTimeSeconds") if sub else None,
                "language": sub.get("programmingLanguage") if sub else initial.get("language"),
                "verdict": sub.get("verdict") if sub else None,
                "verdictLabel": label,
                "passedTestCount": sub.get("passedTestCount") if sub else None,
                "timeMs": sub.get("timeConsumedMillis") if sub else None,
            }
        )

    out.write_text(json.dumps(rows, indent=2))
    counts = Counter(row["verdictLabel"] for row in rows)
    submitted = [row for row in rows if row.get("submissionId")]
    accepted = sum(1 for row in submitted if row.get("verdict") == "OK")
    return {
        "rows": rows,
        "counts": dict(counts),
        "submitted": len(submitted),
        "accepted": accepted,
        "notAccepted": len(submitted) - accepted,
        "unavailable": [row["problem"] for row in rows if row["status"] == "unavailable-python"],
        "otherNotSubmitted": [
            row["problem"] for row in rows if not row.get("submissionId") and row["status"] != "unavailable-python"
        ],
        "out": str(out.relative_to(ROOT)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=200, help="0-based metadata start index")
    parser.add_argument("--end", type=int, default=1000, help="0-based metadata end index")
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--delay", type=int, default=35)
    parser.add_argument("--retry-delay", type=int, default=35)
    parser.add_argument("--handle", default="__ParadigmShift")
    parser.add_argument("--api-count", type=int, default=2000)
    args = parser.parse_args()

    meta = json.loads(META.read_text())
    all_summaries = []
    run_started = int(time.time()) - 120
    aggregate_rows = []

    for start in range(args.start, args.end, args.batch_size):
        end = min(start + args.batch_size, args.end)
        batch_no = start // args.batch_size + 1
        entries = []
        missing = []
        for problem in meta[start:end]:
            name = pid(problem)
            path = SOL / name / "solution.py"
            if path.exists():
                entries.append(
                    {
                        "problem": name,
                        "path": str(path.relative_to(ROOT)),
                        "rating": problem.get("rating"),
                        "name": problem["name"],
                    }
                )
            else:
                missing.append(name)
        if missing:
            raise RuntimeError(f"missing solutions in batch {batch_no}: {missing}")

        prefix = f"gpt55_batch{batch_no:02d}_{start + 1}_{end}"
        manifest = SUBMISSIONS / f"manifest_{prefix}.json"
        write_manifest(entries, manifest)
        log(f"Batch {batch_no}: metadata {start + 1}-{end}, {len(entries)} entries")

        initial_results_path = run_submit(manifest, args.delay, LOGS / f"submit_{prefix}.log")
        initial_results = json.loads(initial_results_path.read_text())

        form_errors = [
            {k: v for k, v in r.items() if k in ("problem", "path", "rating", "name")}
            for r in initial_results
            if r.get("status") == "error"
        ]
        form_retry_results: list[dict] = []
        if form_errors:
            form_retry_manifest = SUBMISSIONS / f"manifest_{prefix}_retry_errors.json"
            write_manifest(form_errors, form_retry_manifest)
            form_retry_path = run_submit(
                form_retry_manifest,
                args.retry_delay,
                LOGS / f"submit_{prefix}_retry_errors.log",
            )
            form_retry_results = json.loads(form_retry_path.read_text())

        wanted = {entry["problem"] for entry in entries}
        unavailable = {r["problem"] for r in form_retry_results if r.get("status") == "error"}
        rejected = {r["problem"] for r in initial_results if r.get("status") == "rejected"}
        latest = latest_for(wanted, args.handle, run_started, args.api_count)
        retry_unconfirmed = [
            entry
            for entry in entries
            if entry["problem"] not in latest
            and entry["problem"] not in unavailable
            and entry["problem"] not in rejected
        ]
        unconfirmed_retry_results: list[dict] = []
        if retry_unconfirmed:
            retry_manifest = SUBMISSIONS / f"manifest_{prefix}_retry_unconfirmed.json"
            write_manifest(retry_unconfirmed, retry_manifest)
            retry_path = run_submit(
                retry_manifest,
                args.retry_delay,
                LOGS / f"submit_{prefix}_retry_unconfirmed.log",
            )
            unconfirmed_retry_results = json.loads(retry_path.read_text())

        verdict_path = SUBMISSIONS / f"manifest_{prefix}_final_verdicts.json"
        summary = reconcile(
            entries,
            initial_results,
            form_retry_results,
            unconfirmed_retry_results,
            args.handle,
            run_started,
            args.api_count,
            verdict_path,
        )
        all_summaries.append({"batch": batch_no, "range": [start + 1, end], **{k: v for k, v in summary.items() if k != "rows"}})
        aggregate_rows.extend(summary["rows"])
        aggregate_path = SUBMISSIONS / "manifest_gpt55_remaining800_aggregate_verdicts.json"
        aggregate_path.write_text(json.dumps(aggregate_rows, indent=2))
        summary_path = SUBMISSIONS / "manifest_gpt55_remaining800_summary.json"
        summary_path.write_text(json.dumps(all_summaries, indent=2))

        log(
            f"Batch {batch_no} done: accepted {summary['accepted']}/{summary['submitted']}, "
            f"not accepted {summary['notAccepted']}/{summary['submitted']}, "
            f"unavailable {len(summary['unavailable'])}, other not submitted {len(summary['otherNotSubmitted'])}"
        )

    total_submitted = sum(item["submitted"] for item in all_summaries)
    total_accepted = sum(item["accepted"] for item in all_summaries)
    total_not_accepted = sum(item["notAccepted"] for item in all_summaries)
    total_unavailable = sum(len(item["unavailable"]) for item in all_summaries)
    total_other = sum(len(item["otherNotSubmitted"]) for item in all_summaries)
    log("Remaining-800 run complete")
    log(f"Accepted {total_accepted}/{total_submitted}; not accepted {total_not_accepted}/{total_submitted}")
    log(f"Unavailable-python ignored: {total_unavailable}; other not submitted: {total_other}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
