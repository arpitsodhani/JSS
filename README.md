# Clause-wise AST Ensemble Merger

This repository is a self-contained research snapshot of the merger software,
three benchmark datasets, and their generated artifacts. The merger takes
multiple implementations of the **same program**, compares corresponding code
clauses structurally, selects a consensus clause, and assembles a new program.

This is not a correctness oracle: a high agreement score means that candidates
look structurally similar. Always compile and test a merged program against the
target problem's test suite to verify actual correctness.

For local testing and official-judge submission instructions, see
[`TESTING_AND_SUBMISSION.md`]

## Contents

| Path | Contents |
| --- | --- |
| `merger_software/` | C and language-agnostic merger implementations and helper tools. |
| `Codeforces Dataset/dataset/` | Codeforces-1000 index and problem statements. |
| `Codeforces Dataset/oneshot_solutions/` | One Python solution per Codeforces problem from GPT and Sonnet. |
| `Codeforces Dataset/merged_solutions/` | Five candidate Python solutions plus a clause-wise merged solution per Codeforces problem and model. |
| `Atcoder-350/` | 350 Claude-generated C ensembles and merged programs. |
| `HumanEval/` | 161 HumanEval ensembles for GPT and Meta-Llama. |

### Dataset coverage

| Dataset | Model(s) | Code artifacts |
| --- | --- | --- |
| Codeforces-1000 | GPT, Sonnet | 1,000 one-shot files and 1,000 merged directories per model; each merged directory has `candidate_1.py` through `candidate_5.py` and `merged.py`. |
| AtCoder-350 | Claude | 350 problem directories, each with `solutions.json`, `merged.c`, and merge/confidence reports. |
| HumanEval | GPT, Meta-Llama | 161 problem directories per model, each with `solutions.json` and `merged.c`. |

## Setup

The core code requires Python 3 and the packages in
`merger_software/requirements-testbed.txt`. Create an isolated environment
from the repository root:

```bash
python3 -m venv .venv
.venv/bin/pip install -r merger_software/requirements-testbed.txt
```

The C merger uses libclang when available and has a tree-sitter fallback. A C
compiler such as `gcc` is needed to compile generated C programs. Node.js and
a logged-in browser profile are only needed for the Codeforces submission
scripts; they are not required to merge or inspect artifacts.

## Quick start: language-agnostic merger

The general entry point is:

```bash
python3 merger_software/ast_merger_lang_agnostic/evaluate_clauses.py \
  --lang python \
  --input path/to/uast_input.json \
  --out path/to/merged.py \
  --threshold 0.60 \
  --out-trees path/to/trees.txt
```

Supported values for `--lang` are `c`, `cpp`, `python`, `java`, and
`javascript`. `--threshold` is optional; if omitted, the evaluator uses its
language-specific default. The command writes the merged source to `--out`,
writes AST diagnostics only when `--out-trees` is supplied, and prints the
per-clause confidence report to standard output.

Try the included Python fixture without changing the repository:

```bash
python3 merger_software/ast_merger_lang_agnostic/evaluate_clauses.py \
  --lang python \
  --input merger_software/ast_merger_lang_agnostic/test_python.json \
  --out /tmp/merged_example.py
python3 -m py_compile /tmp/merged_example.py
```

## General merger input and output

The evaluator consumes a JSON object with a `programs` array. Each program has
an identifier, optional shared import/include lines, and one or more clauses.
The important input contract is that equivalent clauses across candidates use
the same `clause_id` and have compatible interfaces.

```json
{
  "global_includes": ["import sys"],
  "programs": [
    {
      "id": "candidate_1",
      "includes": ["from collections import deque"],
      "clauses": [
        {
          "clause_id": "read_input",
          "signature": "() -> tuple[int, list[int]]",
          "code": "def read_input():\n    n = int(input())\n    return n, list(map(int, input().split()))"
        },
        {
          "clause_id": "main",
          "signature": "() -> None",
          "code": "def main():\n    n, a = read_input()\n    print(sum(a))\n\nif __name__ == '__main__':\n    main()"
        }
      ]
    }
  ]
}
```

Input fields:

- `global_includes` — optional lines placed before every assembled program.
- `programs` — one entry per candidate program.
- `id` — a label used in diagnostics.
- `includes` — optional import or include lines for that candidate; duplicates
  are removed during assembly.
- `clauses` — code fragments to compare. Each fragment contains a `clause_id`,
  optional `signature`, and source `code`.

Output is one complete source file containing deduplicated includes and the
selected clause bodies. The standard-output report gives the candidate count,
agreement, selected fragments, and confidence for every clause. A confidence
score is not a test result.

For safe recombination, keep these invariants across all candidates:

1. Each candidate should have the same clause IDs, in the same logical order.
2. A clause and its callers must agree on argument names, types, return values,
   global names, and data representation.
3. Required imports, helper definitions, and entry-point code must be included
   in the appropriate `includes` or clause.
4. Compile the output and run the actual tests. Syntax success alone does not
   establish semantic correctness.

## C merger: per-problem workflow

AtCoder and HumanEval use the C-oriented input format. A problem directory
contains a `solutions.json` whose top-level `programs` array has five candidate
programs. Every program supplies `includes` and clauses with `clause_id`, a C
function `signature`, and a `code` body. See
[`merger_software/ast_merger/solutions.json`](merger_software/ast_merger/solutions.json)
for a complete small example.

Regenerate an AtCoder merged program from the repository root:

```bash
cd Atcoder-350
python3 run_merge_problem.py 350A
```

Regenerate a HumanEval GPT program:

```bash
cd HumanEval/gpt_codes
python3 run_merge_problem.py 000_has_close_elements
```

Both commands read `<problem>/solutions.json` and write the following files in
that directory:

- `merged.c` — assembled C program.
- `merge_report.json` — selected clause and merger details.
- `confidence_report.json` — per-clause and aggregate agreement scores.

Use `--out`, `--merge-report`, and `--confidence-report` to avoid overwriting
the checked-in artifacts. For example:

```bash
cd Atcoder-350
python3 run_merge_problem.py 350A \
  --out merged_local.c \
  --merge-report merge_local.json \
  --confidence-report confidence_local.json
gcc -std=c11 -Wall -Wextra 350A/merged_local.c -o /tmp/350A
```

The lower-level C command is useful for a standalone `solutions.json`:

```bash
python3 merger_software/ast_merger/run_merge.py \
  --input merger_software/ast_merger/solutions.json \
  --out /tmp/merged.c \
  --merge-report /tmp/merge_report.json \
  --confidence-report /tmp/confidence_report.json
```

## Working with the Codeforces artifacts

`Codeforces Dataset/dataset/problems_index.json` is the machine-readable list of all 1,000
problems. Each item has `problem_id`, `name`, `rating`, `tags`, and the name of
its statement file under `Codeforces Dataset/dataset/statements/`.

For a problem named `<ID>_<name>`:

```text
Codeforces Dataset/oneshot_solutions/sonnet/<ID>_<name>.py
Codeforces Dataset/merged_solutions/sonnet/<ID>_<name>/candidate_1.py
Codeforces Dataset/merged_solutions/sonnet/<ID>_<name>/candidate_2.py
Codeforces Dataset/merged_solutions/sonnet/<ID>_<name>/candidate_3.py
Codeforces Dataset/merged_solutions/sonnet/<ID>_<name>/candidate_4.py
Codeforces Dataset/merged_solutions/sonnet/<ID>_<name>/candidate_5.py
Codeforces Dataset/merged_solutions/sonnet/<ID>_<name>/merged.py
```

The same layout exists for GPT. The Python candidate files contain markers of
the following form, which identify clauses for the merger:

```python
# --- clause: read_input :: () -> tuple[int, list[int]] ---
```

`merger_software/tools/sonnet_clauses.py` parses these markers. To merge a new
Python ensemble, convert the marked candidates to the general JSON format above
and invoke `evaluate_clauses.py`. Some historical pipeline scripts in
`merger_software/tools/` (for example `run_sonnet_merge.py`) retain paths to
the original testbed and are not drop-in commands for this publication
snapshot; use the general CLI or adapt their `ROOT` and output paths first.

## HumanEval fixtures

Each retained HumanEval problem folder includes its source candidates, merged
program, description, and any supplied `input_N.txt` / `output_N.txt` fixture
pairs.
