#!/usr/bin/env python3
"""Generate Sonnet 4.5 solutions for every Codeforces problem in the dataset.

The job is long-running and survives Claude usage limits: when the CLI reports
"You've hit your session limit · resets 2:40am (Asia/Kolkata)", every worker
pauses, the reset instant is parsed out of that message, and generation restarts
by itself the moment the limit lifts. If a message ever arrives without a
parseable time, the daemon falls back to a fixed daily reset anchor and then to
a 30-minute probe loop, so it can never get stuck.

State lives in sonnet_gen/progress.json and sonnet_gen/PROGRESS.md, both
rewritten after every problem, so the run is fully resumable: rerunning the
script picks up exactly where it stopped and skips solutions already on disk.

  .venv/bin/python tools/generate_all_sonnet.py                 # all 1000
  .venv/bin/python tools/generate_all_sonnet.py --limit 200     # first 200
  .venv/bin/python tools/generate_all_sonnet.py --status        # print progress
"""
from __future__ import annotations

import argparse
import json
import queue
import re
import signal
import subprocess
import sys
import threading
import time
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
STATEMENTS = ROOT / "codeforces_data" / "statements"
OUT_DIR = ROOT / "sonnet_gen"
PROGRESS_JSON = OUT_DIR / "progress.json"
PROGRESS_MD = OUT_DIR / "PROGRESS.md"

DEFAULT_MODEL = "claude-sonnet-4-5-20250929"
LOCAL_TZ = ZoneInfo("Asia/Kolkata")

# Usage-limit detection. The CLI exits non-zero with a message such as
#   "You've hit your session limit · resets 2:40am (Asia/Kolkata)"
#   "Claude usage limit reached. Your limit will reset at 3pm (UTC)"
LIMIT_PATTERNS = [
    re.compile(r"hit your (?:session|usage|weekly|5-hour) limit", re.I),
    re.compile(r"usage limit reached", re.I),
    re.compile(r"rate limit", re.I),
    re.compile(r"\blimit will reset\b", re.I),
    re.compile(r"\bresets? (?:at )?\d{1,2}(?::\d{2})?\s*(?:am|pm)?", re.I),
    re.compile(r"\b429\b"),
]

# "resets 2:40am (Asia/Kolkata)", "reset at 15:00 (UTC)", "resets Mon 3pm"
RESET_PATTERN = re.compile(
    r"reset(?:s|\s+at)?\s+"
    r"(?:(?P<weekday>mon|tue|tues|wed|thu|thur|thurs|fri|sat|sun)[a-z]*\s+)?"
    r"(?P<hour>\d{1,2})(?::(?P<minute>\d{2}))?\s*"
    r"(?P<meridiem>am|pm)?"
    r"(?:\s*\((?P<tz>[A-Za-z_]+/[A-Za-z_]+|UTC|GMT)\))?",
    re.I,
)

WEEKDAYS = {"mon": 0, "tue": 1, "tues": 1, "wed": 2, "thu": 3, "thur": 3,
            "thurs": 3, "fri": 4, "sat": 5, "sun": 6}

PROMPT_TEMPLATE = """You are solving a Codeforces problem. Write a complete, correct, efficient Python 3 solution.

Problem id: {pid}
Title: {title}
Rating: {rating}
Tags: {tags}
Time limit: {time_limit}
Memory limit: {mem_limit}

--- STATEMENT ---
{statement}
--- END STATEMENT ---

Sample tests (NOTE: newlines inside each sample input were lost during dataset
scraping, so the input lines appear concatenated; infer the intended line
structure from the statement):
{samples}

Requirements:
- Read from standard input, write to standard output. No prompts, no extra text.
- Plain Python 3 standard library only. It will run on PyPy 3 on Codeforces.
- Use fast I/O (sys.stdin.buffer.read()) and keep within the time limit for the
  maximum constraints stated in the problem.
- Set a higher recursion limit or use an iterative formulation if recursion is deep.
- Handle multiple test cases if the problem has them.

Reply with ONLY one fenced code block containing the full program:

```python
<your solution>
```
"""

CODE_BLOCK = re.compile(r"```(?:python|py)?\s*\n(.*?)```", re.DOTALL)


# ---------------------------------------------------------------- utilities


def now() -> datetime:
    return datetime.now(LOCAL_TZ)


def stamp() -> str:
    return now().strftime("%Y-%m-%d %H:%M:%S %Z")


def log(message: str) -> None:
    print(f"[{stamp()}] {message}", flush=True)


def is_limit_error(text: str) -> bool:
    return any(pattern.search(text) for pattern in LIMIT_PATTERNS)


def parse_reset_time(text: str, reference: datetime | None = None) -> datetime | None:
    """Turn a '... resets 2:40am (Asia/Kolkata)' message into an absolute time."""
    match = RESET_PATTERN.search(text)
    if not match:
        return None
    reference = reference or now()

    tz_name = match.group("tz")
    if tz_name:
        tz_name = {"GMT": "UTC"}.get(tz_name.upper(), tz_name)
        try:
            tz = ZoneInfo(tz_name if "/" in tz_name else tz_name.upper())
        except Exception:  # noqa: BLE001 - unknown zone, use local
            tz = LOCAL_TZ
    else:
        tz = LOCAL_TZ

    hour = int(match.group("hour"))
    minute = int(match.group("minute") or 0)
    meridiem = (match.group("meridiem") or "").lower()
    if meridiem == "pm" and hour != 12:
        hour += 12
    elif meridiem == "am" and hour == 12:
        hour = 0
    if hour > 23 or minute > 59:
        return None

    local_reference = reference.astimezone(tz)
    target = local_reference.replace(hour=hour, minute=minute, second=0, microsecond=0)

    weekday = match.group("weekday")
    if weekday:
        wanted = WEEKDAYS[weekday.lower()[:3]]
        days_ahead = (wanted - target.weekday()) % 7
        if days_ahead == 0 and target <= local_reference:
            days_ahead = 7
        target += timedelta(days=days_ahead)
    elif target <= local_reference:
        target += timedelta(days=1)

    return target.astimezone(LOCAL_TZ)


def next_daily_anchor(anchor: str, reference: datetime | None = None) -> datetime:
    """Next occurrence of a hardcoded HH:MM daily reset anchor."""
    reference = reference or now()
    hour, _, minute = anchor.partition(":")
    target = reference.replace(hour=int(hour), minute=int(minute or 0), second=0, microsecond=0)
    if target <= reference:
        target += timedelta(days=1)
    return target


# ---------------------------------------------------------------- state


class Progress:
    """Resumable, thread-safe run state persisted to disk after every problem."""

    def __init__(self, path: Path, total: int, model: str):
        self.path = path
        self.total = total
        self.model = model
        self.lock = threading.Lock()
        self.started = stamp()
        self.problems: dict[str, dict] = {}
        self.pause_info: dict | None = None
        self.pauses = 0
        if path.exists():
            try:
                stored = json.loads(path.read_text())
                self.problems = stored.get("problems", {})
                self.started = stored.get("started", self.started)
                self.pauses = stored.get("pauses", 0)
            except (json.JSONDecodeError, OSError):
                pass

    def counts(self) -> dict[str, int]:
        counts = {"ok": 0, "failed": 0, "pending": 0}
        for record in self.problems.values():
            key = record.get("status")
            counts[key] = counts.get(key, 0) + 1
        counts["pending"] = self.total - counts["ok"] - counts["failed"]
        return counts

    def record(self, pid: str, status: str, **extra) -> None:
        with self.lock:
            self.problems[pid] = {"status": status, "updated": stamp(), **extra}
            self._flush()

    def set_pause(self, info: dict | None) -> None:
        with self.lock:
            self.pause_info = info
            if info:
                self.pauses += 1
            self._flush()

    def touch(self) -> None:
        with self.lock:
            self._flush()

    def _flush(self) -> None:
        counts = self.counts()
        payload = {
            "model": self.model,
            "total": self.total,
            "started": self.started,
            "updated": stamp(),
            "counts": counts,
            "pauses": self.pauses,
            "paused": self.pause_info,
            "problems": self.problems,
        }
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(payload, indent=2))
        tmp.replace(self.path)
        self._write_markdown(counts)

    def _write_markdown(self, counts: dict[str, int]) -> None:
        done = counts["ok"]
        pct = done / self.total * 100 if self.total else 0.0
        filled = int(pct // 4)
        bar = "█" * filled + "░" * (25 - filled)
        lines = [
            "# Sonnet solution generation progress",
            "",
            f"- Model: `{self.model}`",
            f"- Started: {self.started}",
            f"- Updated: {stamp()}",
            "",
            f"`{bar}` **{done}/{self.total}** ({pct:.1f}%)",
            "",
            f"- Generated: {done}",
            f"- Failed (exhausted retries): {counts['failed']}",
            f"- Remaining: {counts['pending']}",
            f"- Usage-limit pauses so far: {self.pauses}",
        ]
        if self.pause_info:
            lines += [
                "",
                "## Currently paused on a usage limit",
                f"- Detected: {self.pause_info.get('detected')}",
                f"- Resumes at: {self.pause_info.get('resume_at')}",
                f"- Source: {self.pause_info.get('source')}",
                f"- Message: `{self.pause_info.get('message', '')[:200]}`",
            ]
        failures = {pid: r for pid, r in self.problems.items() if r.get("status") == "failed"}
        if failures:
            lines += ["", "## Failed problems", ""]
            for pid, record in sorted(failures.items()):
                lines.append(f"- `{pid}`: {record.get('error', '')[:160]}")
        PROGRESS_MD.write_text("\n".join(lines) + "\n")


# ---------------------------------------------------------------- limiter


class LimitGate:
    """Blocks every worker while a Claude usage limit is in force."""

    def __init__(self, progress: Progress, poll_seconds: int, daily_anchor: str | None,
                 model: str, probe_timeout: int):
        self.progress = progress
        self.poll_seconds = poll_seconds
        self.daily_anchor = daily_anchor
        self.model = model
        self.probe_timeout = probe_timeout
        self.open_event = threading.Event()
        self.open_event.set()
        self.lock = threading.Lock()
        self.stopping = threading.Event()
        self.waiter: threading.Thread | None = None

    def wait_until_open(self) -> None:
        while not self.stopping.is_set():
            if self.open_event.wait(timeout=5):
                return

    def report_limit(self, message: str) -> None:
        """Called by a worker that just hit the limit; starts one waiter thread."""
        with self.lock:
            if not self.open_event.is_set():
                return  # another worker already opened the gate handling
            resume_at, source = self._resume_time(message)
            self.open_event.clear()
            self.progress.set_pause({
                "detected": stamp(),
                "resume_at": resume_at.strftime("%Y-%m-%d %H:%M:%S %Z"),
                "source": source,
                "message": message,
            })
            log(f"USAGE LIMIT hit. Pausing all workers until {resume_at:%Y-%m-%d %H:%M %Z} "
                f"(source: {source}).")
            self.waiter = threading.Thread(target=self._wait_and_reopen, args=(resume_at,),
                                           daemon=True)
            self.waiter.start()

    def _resume_time(self, message: str) -> tuple[datetime, str]:
        parsed = parse_reset_time(message)
        if parsed:
            return parsed + timedelta(seconds=90), "reset time parsed from CLI message"
        if self.daily_anchor:
            return next_daily_anchor(self.daily_anchor) + timedelta(seconds=90), \
                f"hardcoded daily reset anchor {self.daily_anchor}"
        return now() + timedelta(seconds=self.poll_seconds), \
            f"{self.poll_seconds // 60}-minute poll fallback"

    def _wait_and_reopen(self, resume_at: datetime) -> None:
        while not self.stopping.is_set():
            last_report = now()
            while not self.stopping.is_set():
                remaining = (resume_at - now()).total_seconds()
                if remaining <= 0:
                    break
                time.sleep(min(remaining, 60))
                if (now() - last_report).total_seconds() >= 1800:
                    left = (resume_at - now()).total_seconds()
                    log(f"Still waiting on usage limit; {max(left, 0) / 60:.0f} min to go.")
                    last_report = now()
            if self.stopping.is_set():
                return

            log("Reset time reached; probing whether the limit has lifted.")
            ok, detail = self._probe()
            if ok:
                log("Limit lifted. Resuming generation.")
                self.progress.set_pause(None)
                self.open_event.set()
                return

            parsed = parse_reset_time(detail)
            if parsed and parsed > now():
                resume_at = parsed + timedelta(seconds=90)
                source = "reset time parsed from probe"
            else:
                resume_at = now() + timedelta(seconds=self.poll_seconds)
                source = f"{self.poll_seconds // 60}-minute poll fallback"
            log(f"Limit still in force ({detail[:120]}). Next check at "
                f"{resume_at:%Y-%m-%d %H:%M %Z} ({source}).")
            self.progress.set_pause({
                "detected": stamp(),
                "resume_at": resume_at.strftime("%Y-%m-%d %H:%M:%S %Z"),
                "source": source,
                "message": detail,
            })

    def _probe(self) -> tuple[bool, str]:
        try:
            result = subprocess.run(
                ["claude", "-p", "Reply with exactly: OK", "--model", self.model,
                 "--allowedTools", "", "--output-format", "text"],
                cwd=str(ROOT), text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                timeout=self.probe_timeout, check=False,
            )
        except subprocess.TimeoutExpired:
            return False, "probe timed out"
        detail = (result.stderr.strip() or result.stdout.strip())[:400]
        if result.returncode == 0 and not is_limit_error(detail):
            return True, detail
        return False, detail or f"probe exit {result.returncode}"

    def stop(self) -> None:
        self.stopping.set()
        self.open_event.set()


# ---------------------------------------------------------------- generation


def load_problems(limit: int | None) -> list[dict]:
    meta = json.loads((ROOT / "codeforces_data" / "problems_meta.json").read_text())
    return meta[:limit] if limit else meta


def statement_path(problem: dict) -> Path:
    return STATEMENTS / f"{problem['contestId']}_{problem['index']}.json"


def build_prompt(problem: dict) -> str:
    data = json.loads(statement_path(problem).read_text())
    samples = [
        f"Sample {i} input:\n{sample.get('input', '')}\n"
        f"Sample {i} output:\n{sample.get('output', '')}"
        for i, sample in enumerate(data.get("samples", []), 1)
    ]
    return PROMPT_TEMPLATE.format(
        pid=f"{problem['contestId']}{problem['index']}",
        title=data.get("title") or problem["name"],
        rating=problem.get("rating", "unknown"),
        tags=", ".join(problem.get("tags", [])),
        time_limit=data.get("time_limit", "unknown"),
        mem_limit=data.get("mem_limit", "unknown"),
        statement=data.get("statement", ""),
        samples="\n\n".join(samples) if samples else "(none available)",
    )


class LimitReached(RuntimeError):
    pass


def call_model(prompt: str, model: str, timeout: int) -> str:
    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", model, "--allowedTools", "",
             "--output-format", "text"],
            cwd=str(ROOT), text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=timeout, check=False,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"claude CLI timed out after {timeout}s") from None
    if result.returncode != 0:
        detail = (result.stderr.strip() or result.stdout.strip())[:400]
        if is_limit_error(detail):
            raise LimitReached(detail)
        raise RuntimeError(f"exit {result.returncode}: {detail or 'no output'}")
    return result.stdout


def extract_code(reply: str) -> str | None:
    blocks = CODE_BLOCK.findall(reply)
    return max(blocks, key=len).strip() + "\n" if blocks else None


def compiles(path: Path) -> tuple[bool, str]:
    result = subprocess.run([sys.executable, "-m", "py_compile", str(path)],
                            text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            check=False)
    return result.returncode == 0, result.stderr.strip()[:300]


class Runner:
    def __init__(self, problems: list[dict], args) -> None:
        self.args = args
        self.problems = {f"{p['contestId']}{p['index']}": p for p in problems}
        self.progress = Progress(PROGRESS_JSON, len(problems), args.model)
        self.gate = LimitGate(self.progress, args.poll_seconds, args.daily_reset,
                              args.model, args.probe_timeout)
        self.queue: queue.Queue[str] = queue.Queue()
        self.attempts: dict[str, int] = {}
        self.attempts_lock = threading.Lock()
        self.stopping = threading.Event()
        # Problems accepted for work but not yet in a terminal state. Workers stay
        # alive while this is non-zero, so a problem waiting on a retry timer is
        # never stranded by an empty queue.
        self.outstanding = 0
        self.outstanding_lock = threading.Lock()

    def _finish(self) -> None:
        with self.outstanding_lock:
            self.outstanding -= 1

    def _outstanding(self) -> int:
        with self.outstanding_lock:
            return self.outstanding

    def seed_queue(self) -> int:
        queued = 0
        for pid in self.problems:
            if (OUT_DIR / pid / "solution.py").exists():
                if self.progress.problems.get(pid, {}).get("status") != "ok":
                    self.progress.record(pid, "ok", note="already on disk")
                continue
            self.queue.put(pid)
            queued += 1
        with self.outstanding_lock:
            self.outstanding = queued
        return queued

    def worker(self) -> None:
        while not self.stopping.is_set():
            try:
                pid = self.queue.get(timeout=2)
            except queue.Empty:
                if self._outstanding() == 0:
                    return
                continue
            try:
                self.handle(pid)
            finally:
                self.queue.task_done()

    def handle(self, pid: str) -> None:
        self.gate.wait_until_open()
        if self.stopping.is_set():
            return
        problem = self.problems[pid]
        out_dir = OUT_DIR / pid
        solution = out_dir / "solution.py"
        if solution.exists():
            self.progress.record(pid, "ok", note="already on disk")
            self._finish()
            return
        out_dir.mkdir(parents=True, exist_ok=True)

        with self.attempts_lock:
            self.attempts[pid] = self.attempts.get(pid, 0) + 1
            attempt = self.attempts[pid]

        try:
            reply = call_model(build_prompt(problem), self.args.model, self.args.timeout)
        except LimitReached as exc:
            self.gate.report_limit(str(exc))
            with self.attempts_lock:
                self.attempts[pid] = attempt - 1  # limit pauses do not burn an attempt
            self.queue.put(pid)
            return
        except RuntimeError as exc:
            self.retry_or_fail(pid, attempt, str(exc))
            return

        (out_dir / f"raw_attempt{attempt}.md").write_text(reply)
        code = extract_code(reply)
        if not code:
            self.retry_or_fail(pid, attempt, "no fenced code block in reply")
            return
        solution.write_text(code)
        ok, err = compiles(solution)
        if not ok:
            solution.unlink(missing_ok=True)
            self.retry_or_fail(pid, attempt, f"syntax error: {err}")
            return

        self.progress.record(pid, "ok", attempt=attempt, bytes=len(code))
        self._finish()
        done = self.progress.counts()["ok"]
        log(f"{pid}: ok (attempt {attempt}) — {done}/{len(self.problems)} generated")

    def retry_or_fail(self, pid: str, attempt: int, error: str) -> None:
        if attempt < self.args.max_attempts and not self.stopping.is_set():
            delay = min(20 * 2 ** (attempt - 1), 300)
            log(f"{pid}: attempt {attempt} failed ({error[:120]}); retrying in {delay}s")
            self.progress.record(pid, "pending", attempt=attempt, error=error)
            timer = threading.Timer(delay, self.queue.put, args=(pid,))
            timer.daemon = True
            timer.start()
            return
        log(f"{pid}: FAILED after {attempt} attempts — {error[:160]}")
        self.progress.record(pid, "failed", attempt=attempt, error=error)
        self._finish()

    def run(self) -> int:
        queued = self.seed_queue()
        counts = self.progress.counts()
        log(f"Model {self.args.model}: {counts['ok']} already generated, {queued} to do, "
            f"{self.args.workers} workers.")
        if queued == 0:
            log("Nothing to generate. All solutions present.")
            return 0

        if self.args.start_at_reset:
            self.gate.report_limit("start-at-reset requested")

        threads = [threading.Thread(target=self.worker, daemon=True)
                   for _ in range(self.args.workers)]
        for thread in threads:
            thread.start()

        try:
            while any(thread.is_alive() for thread in threads):
                time.sleep(5)
        except KeyboardInterrupt:
            log("Interrupted; saving progress and stopping.")
            self.stopping.set()
            self.gate.stop()
            for thread in threads:
                thread.join(timeout=10)
            self.progress.touch()
            return 130

        self.gate.stop()
        counts = self.progress.counts()
        self.progress.touch()
        log(f"Done. Generated {counts['ok']}/{self.progress.total}; failed {counts['failed']}; "
            f"usage-limit pauses {self.progress.pauses}.")
        return 0 if counts["failed"] == 0 else 1


def print_status() -> int:
    if not PROGRESS_JSON.exists():
        print("No progress file yet.")
        return 1
    data = json.loads(PROGRESS_JSON.read_text())
    counts = data["counts"]
    total = data["total"]
    print(f"Model:     {data['model']}")
    print(f"Started:   {data['started']}")
    print(f"Updated:   {data['updated']}")
    print(f"Generated: {counts['ok']}/{total} ({counts['ok'] / total:.1%})")
    print(f"Failed:    {counts['failed']}")
    print(f"Remaining: {counts['pending']}")
    print(f"Pauses:    {data['pauses']}")
    if data.get("paused"):
        print(f"PAUSED until {data['paused']['resume_at']} ({data['paused']['source']})")
    return 0


def self_test() -> int:
    """Check limit detection and reset-time parsing against real CLI messages."""
    reference = datetime(2026, 8, 16, 1, 0, tzinfo=LOCAL_TZ)
    cases = [
        ("You've hit your session limit · resets 2:40am (Asia/Kolkata)", (2026, 8, 16, 2, 40)),
        ("You've hit your session limit · resets 2:40am", (2026, 8, 16, 2, 40)),
        ("Claude usage limit reached. Your limit will reset at 3pm (Asia/Kolkata)",
         (2026, 8, 16, 15, 0)),
        ("You've hit your usage limit · resets 12am (Asia/Kolkata)", (2026, 8, 17, 0, 0)),
        ("You've hit your weekly limit · resets Mon 9:30am (Asia/Kolkata)",
         (2026, 8, 17, 9, 30)),
        ("You've hit your session limit · resets 14:15 (Asia/Kolkata)", (2026, 8, 16, 14, 15)),
    ]
    failures = 0
    for message, expected in cases:
        assert is_limit_error(message), f"not detected as a limit: {message}"
        parsed = parse_reset_time(message, reference)
        got = (parsed.year, parsed.month, parsed.day, parsed.hour, parsed.minute) if parsed else None
        status = "ok " if got == expected else "FAIL"
        failures += got != expected
        print(f"{status} {message!r} -> {got} (expected {expected})")

    utc_case = "You've hit your session limit · resets 9:00pm (UTC)"
    parsed = parse_reset_time(utc_case, reference)
    expected_ist = (2026, 8, 16, 2, 30)  # 21:00 UTC previous day is 02:30 IST
    got = (parsed.year, parsed.month, parsed.day, parsed.hour, parsed.minute) if parsed else None
    print(f"{'ok ' if got == expected_ist else 'FAIL'} {utc_case!r} -> {got}")
    failures += got != expected_ist

    for benign in ["exit 1: no output", "claude CLI timed out after 900s",
                   "syntax error: invalid syntax"]:
        if is_limit_error(benign):
            print(f"FAIL false positive on {benign!r}")
            failures += 1
        else:
            print(f"ok  no false positive on {benign!r}")

    anchor = next_daily_anchor("02:40", reference)
    print(f"{'ok ' if (anchor.hour, anchor.minute) == (2, 40) else 'FAIL'} "
          f"daily anchor 02:40 -> {anchor}")
    print("\nself-test:", "PASSED" if failures == 0 else f"{failures} FAILURES")
    return 0 if failures == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--limit", type=int, default=None,
                        help="Only the first N problems (default: all 1000)")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=900, help="Per-call timeout in seconds")
    parser.add_argument("--probe-timeout", type=int, default=180)
    parser.add_argument("--max-attempts", type=int, default=5)
    parser.add_argument("--poll-seconds", type=int, default=1800,
                        help="Fallback poll interval when no reset time can be parsed")
    parser.add_argument("--daily-reset", default=None, metavar="HH:MM",
                        help="Hardcoded daily reset anchor used before falling back to polling")
    parser.add_argument("--start-at-reset", action="store_true",
                        help="Wait for the next reset before generating anything")
    parser.add_argument("--status", action="store_true", help="Print progress and exit")
    parser.add_argument("--self-test", action="store_true",
                        help="Verify limit detection and reset-time parsing, then exit")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if args.status:
        return print_status()

    problems = [p for p in load_problems(args.limit) if statement_path(p).exists()]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    runner = Runner(problems, args)

    def shutdown(signum, _frame):
        log(f"Signal {signum} received; shutting down cleanly.")
        runner.stopping.set()
        runner.gate.stop()

    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)
    return runner.run()


if __name__ == "__main__":
    raise SystemExit(main())
