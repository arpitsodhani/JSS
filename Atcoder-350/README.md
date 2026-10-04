# Atcoder-350 (Claude) - Merge Regeneration Guide

This folder contains Atcoder problem subfolders (for example `350A`, `379A`). Each problem
folder includes a `solutions.json` file.

## Requirements
- Python 3.x
- A working C parser backend (libclang recommended; tree-sitter fallback)

## Run the merger for one problem
From this folder:

```bash
python3 run_merge_problem.py 350A
```

This will (re)generate the following files inside the problem folder:
- `merged.c`
- `merge_report.json`
- `confidence_report.json`

## Verify outputs
Example verification commands:

```bash
ls 350A/merged.c 350A/confidence_report.json
python3 -c "import json; print(json.load(open('350A/confidence_report.json'))['overall_metrics'])"
```

## Notes
- Use a relative problem name (subfolder) or an absolute path.
- Optional flags are available: `--threshold`, `--max-rounds`, `--verbose`.
