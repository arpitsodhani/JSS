# Agent Instructions: Codeforces AST Merger Testbed

Use this folder:

```bash
cd /home/arpit/Desktop/cf_ast_merger_testbed
```

## What Is Here

- `ast_merger/`: ISSTA-2026 C AST merger copied from `ISSTA-2026/software_code`.
- `ast_merger_lang_agnostic/`: BTP language-agnostic UAST merger copied from ` BTP/lang_agnostic_uast`, excluding its old virtualenv.
- `codeforces/`: MTP-I Codeforces dataset, generated solutions, fixtures, and pipeline results.
- `codeforces_data` and `codeforces_sols`: symlinks used by existing scripts.
- `scripts/submit_codeforces.mjs`: Codeforces submitter automation.
- `.cf-browser-profile` and `.cf-human-profile`: symlinks to the existing MTP-I browser profiles.

The local `.venv` already has required merger dependencies. If it is missing:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-testbed.txt
```

## First-Five Verification Problems

The first five entries in `codeforces_data/problems_meta.json` are:

```text
1693B Fake Plastic Trees
2084A Max and Mod
180D Name
985C Liebig's Barrels
519C A and B and Team Training
```

Their copied solutions are in:

```text
codeforces_sols/1693B/solution.py
codeforces_sols/2084A/solution.py
codeforces_sols/180D/solution.py
codeforces_sols/985C/solution.py
codeforces_sols/519C/solution.py
```

Run local sample checks:

```bash
.venv/bin/python tools/verify_first_five.py
```

Expected output:

```text
Verified sample checks for 1693B, 2084A, 180D, 985C, 519C
```

## Run The Language-Agnostic Python UAST Merger

For one problem:

```bash
scripts/run_uast_merge_for_problem.sh 1693B
```

This does two things:

1. Builds `merger_inputs/1693B/uast_input.json` from the corrected solution plus available generated candidate fixtures, up to five candidates.
2. Runs `ast_merger_lang_agnostic/evaluate_clauses.py` and writes `merged_outputs/1693B/merged.py`.

## Run The ISSTA C Merger Demo

```bash
.venv/bin/python ast_merger/run_merge.py \
  --input ast_merger/solutions.json \
  --out ast_merger/merged.c \
  --merge-report ast_merger/merge_report.json \
  --confidence-report ast_merger/confidence_report.json
```

Expected result: successful compile and generated `ast_merger/merged.c`, `ast_merger/merge_report.json`, and `ast_merger/confidence_report.json`.

## Submit To Codeforces

Dry-run a single problem first. This opens Chrome, logs in/reuses the profile, selects Python, fills the form, and closes the window without submitting:

```bash
node scripts/submit_codeforces.mjs --dry-run --human-chrome 2084A codeforces_sols/2084A/solution.py
```

Actually submit one problem:

```bash
node scripts/submit_codeforces.mjs --human-chrome 2084A codeforces_sols/2084A/solution.py
```

Submit the first five:

```bash
scripts/submit_first_five.sh
```

The submitter has been patched so the `--human-chrome` window exits after each run. To verify no browser session is left open:

```bash
curl -s --max-time 2 http://127.0.0.1:9223/json/version >/dev/null \
  && echo "still open" || echo "closed"
```

## Current Codeforces Results

These five were submitted on August 15, 2026 and accepted:

```text
387142717 1693B Accepted
387142750 2084A Accepted
387142769 180D Accepted
387142788 985C Accepted
387142801 519C Accepted
```

Do not resubmit them unless explicitly asked.
