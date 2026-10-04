#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

problems=(1693B 2084A 180D 985C 519C)
for problem in "${problems[@]}"; do
  node scripts/submit_codeforces.mjs ${CF_SUBMIT_ARGS---human-chrome} "$problem" "codeforces_sols/$problem/solution.py"
done
