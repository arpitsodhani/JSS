#!/usr/bin/env bash
# Supervisor for the full 1000-problem Sonnet generation run.
#
# The Python daemon already pauses and self-restarts across Claude usage limits.
# This wrapper adds crash recovery on top: if the daemon dies for any other
# reason (OOM, killed terminal, transient CLI breakage) it is restarted, and
# rounds keep going until every problem has a solution or progress stalls.
#
#   scripts/run_full_generation.sh                 # run in the foreground
#   nohup scripts/run_full_generation.sh &         # run detached
#   scripts/run_full_generation.sh --status        # print progress and exit
set -uo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

PY="$root/.venv/bin/python"
DAEMON="$root/tools/generate_all_sonnet.py"
LOG="$root/logs/full_generation.log"
LOCK="$root/logs/full_generation.lock"
WORKERS="${WORKERS:-4}"
LIMIT_ARGS="${LIMIT_ARGS:-}"          # e.g. LIMIT_ARGS="--limit 200"
DAILY_RESET="${DAILY_RESET:-}"        # e.g. DAILY_RESET="02:40" as a fallback anchor
MAX_STALLED_ROUNDS="${MAX_STALLED_ROUNDS:-3}"
RESTART_DELAY="${RESTART_DELAY:-60}"

mkdir -p "$root/logs"

if [[ "${1:-}" == "--status" ]]; then
  exec "$PY" "$DAEMON" --status
fi

exec 9>"$LOCK"
if ! flock -n 9; then
  echo "Another run_full_generation.sh is already running (lock: $LOCK)." >&2
  exit 1
fi

say() { echo "[$(date '+%Y-%m-%d %H:%M:%S %Z')] supervisor: $*" | tee -a "$LOG"; }

count_done() { find "$root/sonnet_gen" -name solution.py 2>/dev/null | wc -l; }

total_problems() {
  "$PY" - "$root" <<'EOF'
import json, sys
from pathlib import Path
meta = json.loads((Path(sys.argv[1]) / "codeforces_data" / "problems_meta.json").read_text())
print(len(meta))
EOF
}

total="$(total_problems)"
[[ -n "$LIMIT_ARGS" ]] && total="$(awk '{print $2}' <<<"$LIMIT_ARGS")"

extra_args=()
[[ -n "$DAILY_RESET" ]] && extra_args+=(--daily-reset "$DAILY_RESET")
# shellcheck disable=SC2206
[[ -n "$LIMIT_ARGS" ]] && extra_args+=($LIMIT_ARGS)

say "starting; target $total problems, $WORKERS workers, log $LOG"

round=0
stalled=0
while :; do
  round=$((round + 1))
  before="$(count_done)"
  if [[ "$before" -ge "$total" ]]; then
    say "all $total solutions present; nothing left to do"
    break
  fi

  say "round $round: $before/$total generated, launching daemon"
  "$PY" "$DAEMON" --workers "$WORKERS" "${extra_args[@]}" >>"$LOG" 2>&1
  status=$?
  after="$(count_done)"
  say "round $round finished (exit $status); $after/$total generated"

  if [[ "$after" -ge "$total" ]]; then
    say "COMPLETE: $after/$total solutions generated"
    break
  fi

  if [[ "$status" -eq 130 ]]; then
    say "interrupted by signal; stopping supervisor"
    break
  fi

  if [[ "$after" -le "$before" ]]; then
    stalled=$((stalled + 1))
    say "no progress this round ($stalled/$MAX_STALLED_ROUNDS stalled rounds)"
    if [[ "$stalled" -ge "$MAX_STALLED_ROUNDS" ]]; then
      say "STOPPING: $MAX_STALLED_ROUNDS rounds with no progress. See sonnet_gen/PROGRESS.md"
      exit 1
    fi
  else
    stalled=0
  fi

  say "restarting in ${RESTART_DELAY}s"
  sleep "$RESTART_DELAY"
done

"$PY" "$DAEMON" --status | tee -a "$LOG"
