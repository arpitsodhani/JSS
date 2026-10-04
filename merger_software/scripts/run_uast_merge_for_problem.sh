#!/usr/bin/env bash
set -euo pipefail

problem_id="${1:?usage: scripts/run_uast_merge_for_problem.sh <problem-id>}"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"$root/.venv/bin/python" "$root/tools/build_uast_input.py" "$problem_id" --root "$root"
mkdir -p "$root/merged_outputs/$problem_id"
"$root/.venv/bin/python" "$root/ast_merger_lang_agnostic/evaluate_clauses.py" \
  --lang python \
  --input "$root/merger_inputs/$problem_id/uast_input.json" \
  --out "$root/merged_outputs/$problem_id/merged.py"

echo "Merged output: $root/merged_outputs/$problem_id/merged.py"
