# Codeforces AST Merger Testbed

This folder brings together the three pieces that were scattered across the desktop:

- `ast_merger/`: the ISSTA-2026 C AST merger from `ISSTA-2026/software_code`.
- `ast_merger_lang_agnostic/`: the BTP language-agnostic AST merger copy, excluding its old virtualenv.
- `codeforces/`: the MTP-I Codeforces data, generated solutions, fixtures, and pipeline results.
- `scripts/submit_codeforces.mjs`: the Codeforces submitter automation from MTP-I.

The convenience symlinks `codeforces_data` and `codeforces_sols` point into `codeforces/` so the old submitter path defaults still work.

## Verify The First Five

```bash
.venv/bin/python tools/verify_first_five.py
```

The local `.venv` already contains the merger dependencies. If it is deleted, recreate it with:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-testbed.txt
```

The first five problems from `codeforces_data/problems_meta.json` are:

```text
1693B Fake Plastic Trees
2084A Max and Mod
180D Name
985C Liebig's Barrels
519C A and B and Team Training
```

Their copied `solution.py` files have been replaced with sample-checked solutions in this testbed.

## Run The Python UAST Merger

```bash
scripts/run_uast_merge_for_problem.sh 1693B
```

This builds `merger_inputs/<problem>/uast_input.json` from the corrected final solution plus any available generated `fixtures/llm_cf/codegen__...json` candidates, up to five candidates, then writes `merged_outputs/<problem>/merged.py`.

## Run The ISSTA C Merger Demo

```bash
.venv/bin/python ast_merger/run_merge.py \
  --input ast_merger/solutions.json \
  --out ast_merger/merged.c \
  --merge-report ast_merger/merge_report.json \
  --confidence-report ast_merger/confidence_report.json
```

## Submit The First Five

```bash
scripts/submit_first_five.sh
```

By default this uses `--human-chrome`, reusing the original MTP browser profile symlinks. To only open/fill the form without clicking submit:

```bash
CF_SUBMIT_ARGS="--human-chrome --dry-run" scripts/submit_first_five.sh
```
