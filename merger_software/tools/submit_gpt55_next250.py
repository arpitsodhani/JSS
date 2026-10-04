#!/usr/bin/env python3
"""Resume GPT-5.5 submissions and stop after 250 Python-submittable results."""
from __future__ import annotations

import argparse
import json
import subprocess
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
PREVIOUS_VERDICT_FILES = [
    "submissions/manifest_gpt55_first100_final_verdicts.json",
    "submissions/manifest_gpt55_second100_final_verdicts.json",
    "submissions/manifest_gpt55_batch03_201_300_partial_verdicts_daily_limit.json",
]


def log(msg: str) -> None:
    print(time.strftime("[%Y-%m-%d %H:%M:%S]"), msg, flush=True)


def pid(problem: dict) -> str:
    return f"{problem['contestId']}{problem['index']}"


def fetch_status(handle: str, count: int) -> list[dict]:
    url = f"https://codeforces.com/api/user.status?handle={handle}&from=1&count={count}"
    for attempt in range(8):
        try:
            with urllib.request.urlopen(url, timeout=30) as fh:
                payload = json.load(fh)
            if payload.get("status") == "OK":
                return payload["result"]
        except Exception:
            pass
        time.sleep(3 + attempt * 2)
    raise RuntimeError("Could not read Codeforces API")


def latest_for(problems: set[str], handle: str, lower_bound: int, count: int) -> dict[str, dict]:
    latest: dict[str, dict] = {}
    for sub in fetch_status(handle, count):
        problem = sub["problem"]
        name = f"{problem.get('contestId')}{problem.get('index')}"
        if name in problems and sub.get("creationTimeSeconds", 0) >= lower_bound and name not in latest:
            latest[name] = sub
    return latest


def previous_state() -> tuple[set[str], set[str]]:
    done: set[str] = set()
    unavailable: set[str] = set()
    for rel in PREVIOUS_VERDICT_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        for row in json.loads(path.read_text()):
            status = row.get("status")
            problem = row["problem"]
            if status in {"submitted", "rejected"} or row.get("submissionId"):
                done.add(problem)
            elif status == "unavailable-python":
                done.add(problem)
                unavailable.add(problem)
    return done, unavailable


def write_manifest(entries: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(entries, indent=2))


def run_submit(manifest: Path, delay: int, log_path: Path) -> list[dict]:
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
        raise RuntimeError(f"submitter exited {rc}: {manifest}")
    results_path = manifest.with_name(manifest.stem + "_results.json")
    return json.loads(results_path.read_text())


def is_daily_limit_error(row: dict) -> bool:
    return "no more than" in (row.get("error") or "").lower()


def build_rows(entries: list[dict], latest: dict[str, dict], errors: dict[str, str]) -> list[dict]:
    rows = []
    for entry in entries:
        name = entry["problem"]
        sub = latest.get(name)
        error = errors.get(name)
        if sub:
            status = "submitted"
            label = LABELS.get(sub.get("verdict"), sub.get("verdict") or "submitted")
        elif error and "python language option" in error.lower():
            status = "unavailable-python"
            label = "unavailable-python"
        elif error and "no more than" in error.lower():
            status = "blocked-daily-limit"
            label = "blocked-daily-limit"
        elif error:
            status = "submit-error"
            label = "submit-error"
        else:
            status = "unconfirmed"
            label = "unconfirmed"
        rows.append(
            {
                "problem": name,
                "name": entry.get("name"),
                "rating": entry.get("rating"),
                "status": status,
                "submitError": error,
                "submissionId": sub.get("id") if sub else None,
                "creationTimeSeconds": sub.get("creationTimeSeconds") if sub else None,
                "language": sub.get("programmingLanguage") if sub else None,
                "verdict": sub.get("verdict") if sub else None,
                "verdictLabel": label,
                "passedTestCount": sub.get("passedTestCount") if sub else None,
                "timeMs": sub.get("timeConsumedMillis") if sub else None,
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=int, default=250)
    parser.add_argument("--start", type=int, default=200, help="0-based metadata start index")
    parser.add_argument("--chunk-size", type=int, default=35)
    parser.add_argument("--delay", type=int, default=35)
    parser.add_argument("--handle", default="__ParadigmShift")
    parser.add_argument("--api-count", type=int, default=2500)
    parser.add_argument("--run-started", type=int, default=None)
    parser.add_argument("--prefix", default="gpt55_next250", help="Output filename prefix under submissions/logs")
    args = parser.parse_args()

    run_started = args.run_started or (int(time.time()) - 900)
    meta = json.loads(META.read_text())
    done_previous, unavailable_previous = previous_state()

    all_candidates = []
    for problem in meta[args.start :]:
        name = pid(problem)
        if name in done_previous:
            continue
        path = SOL / name / "solution.py"
        if not path.exists():
            raise RuntimeError(f"missing solution: {name}")
        all_candidates.append(
            {
                "problem": name,
                "path": str(path.relative_to(ROOT)),
                "rating": problem.get("rating"),
                "name": problem["name"],
            }
        )

    # Include any current-run API-visible submissions from candidates, such as a
    # diagnostic submit done just before this runner starts.
    candidate_by_pid = {entry["problem"]: entry for entry in all_candidates}
    current_latest = latest_for(set(candidate_by_pid), args.handle, run_started, args.api_count)
    processed: set[str] = set()
    errors: dict[str, str] = {}
    submitted_pids: set[str] = set(current_latest)
    log(f"Starting next-250 run: {len(submitted_pids)} already API-visible in this run")

    chunk_no = 0
    cursor = 0
    daily_blocked = False
    while len(submitted_pids) < args.target and cursor < len(all_candidates) and not daily_blocked:
        chunk = []
        while cursor < len(all_candidates) and len(chunk) < args.chunk_size:
            entry = all_candidates[cursor]
            cursor += 1
            name = entry["problem"]
            if name in processed or name in submitted_pids:
                continue
            chunk.append(entry)
        if not chunk:
            continue

        chunk_no += 1
        manifest = SUBMISSIONS / f"manifest_{args.prefix}_chunk{chunk_no:02d}.json"
        write_manifest(chunk, manifest)
        results = run_submit(manifest, args.delay, LOGS / f"submit_{args.prefix}_chunk{chunk_no:02d}.log")
        processed.update(row["problem"] for row in results)
        for row in results:
            if row.get("status") == "error":
                errors[row["problem"]] = row.get("error", "")
                if is_daily_limit_error(row):
                    daily_blocked = True

        # Wait for this chunk's successful submissions to appear and finish judging.
        wanted_now = set(submitted_pids) | {row["problem"] for row in results if row.get("status") == "submitted"}
        for attempt in range(18):
            current_latest = latest_for(wanted_now | set(candidate_by_pid), args.handle, run_started, args.api_count)
            submitted_pids = set(current_latest)
            pending = [
                name
                for name in wanted_now
                if name not in current_latest or current_latest[name].get("verdict") in (None, "TESTING")
            ]
            log(
                f"Chunk {chunk_no}: API-visible current submissions {len(submitted_pids)}/{args.target}, "
                f"pending in chunk {len(pending)}"
            )
            if not pending:
                break
            time.sleep(20)

        rows = build_rows(
            [candidate_by_pid[name] for name in sorted(set(processed) | submitted_pids, key=lambda n: list(candidate_by_pid).index(n))],
            current_latest,
            errors,
        )
        out = SUBMISSIONS / f"manifest_{args.prefix}_live_verdicts.json"
        out.write_text(json.dumps(rows, indent=2))
        counts = Counter(row["verdictLabel"] for row in rows)
        accepted = sum(1 for row in rows if row.get("verdict") == "OK")
        not_accepted = sum(1 for row in rows if row.get("submissionId") and row.get("verdict") != "OK")
        log(
            f"Live summary: accepted {accepted}/{len(submitted_pids)}, "
            f"not accepted {not_accepted}/{len(submitted_pids)}, "
            f"unavailable {counts.get('unavailable-python', 0)}, daily-blocked {counts.get('blocked-daily-limit', 0)}"
        )

    final_latest = latest_for(set(candidate_by_pid), args.handle, run_started, args.api_count)
    submitted_pids = set(final_latest)
    # Only include rows up through all processed entries plus API-visible current submissions.
    included = set(processed) | submitted_pids
    rows = build_rows(
        [entry for entry in all_candidates if entry["problem"] in included],
        final_latest,
        errors,
    )
    out = SUBMISSIONS / f"manifest_{args.prefix}_final_verdicts.json"
    out.write_text(json.dumps(rows, indent=2))

    submitted = [row for row in rows if row.get("submissionId")]
    accepted = sum(1 for row in submitted if row.get("verdict") == "OK")
    counts = Counter(row["verdictLabel"] for row in rows)
    summary = {
        "target": args.target,
        "submitted": len(submitted),
        "accepted": accepted,
        "notAccepted": len(submitted) - accepted,
        "counts": dict(counts),
        "unavailablePython": [row["problem"] for row in rows if row["status"] == "unavailable-python"],
        "blockedDailyLimit": [row["problem"] for row in rows if row["status"] == "blocked-daily-limit"],
        "output": str(out.relative_to(ROOT)),
    }
    summary_path = SUBMISSIONS / f"manifest_{args.prefix}_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))
    log(
        f"FINAL: accepted {summary['accepted']}/{summary['submitted']}, "
        f"not accepted {summary['notAccepted']}/{summary['submitted']}, "
        f"unavailable {len(summary['unavailablePython'])}, daily-blocked {len(summary['blockedDailyLimit'])}"
    )
    log(f"Wrote {out.relative_to(ROOT)} and {summary_path.relative_to(ROOT)}")
    return 0 if summary["submitted"] >= args.target else 1


if __name__ == "__main__":
    raise SystemExit(main())
