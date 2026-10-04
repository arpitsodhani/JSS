# Testing and Submission Guide

Use this guide to test a generated or merged program and, when appropriate,
submit it to the original online judge. Local testing and online submission are
different checks:

- **HumanEval** includes paired input/output fixtures in this repository.
- **AtCoder** and **Codeforces** expose public samples, but their full judge
  suites are private. A local sample pass is therefore not a full correctness
  result; submit to the official judge to obtain that verdict.

Do not overwrite checked-in artifacts while experimenting. Compile or write
outputs under `/tmp`, or use a copy of the source file.

## 1. Locate the program to test

### HumanEval

```text
HumanEval/gpt_codes/<PROBLEM_NAME>/merged.c
HumanEval/meta_llama_codes/<PROBLEM_NAME>/merged.c
```

Example: `HumanEval/gpt_codes/000_has_close_elements/merged.c`.

### AtCoder

```text
Atcoder-350/<PROBLEM_ID>/merged.c
```

Example: `Atcoder-350/350A/merged.c`.

### Codeforces

```text
Codeforces Dataset/merged_solutions/<MODEL>/<PROBLEM_ID>_<PROBLEM_NAME>/merged.py
```

`<MODEL>` is `gpt` or `sonnet`. The five source candidates sit alongside
`merged.py`; the single-call baseline is in
`Codeforces Dataset/oneshot_solutions/<MODEL>/`.

## 2. Test HumanEval with the supplied fixtures

Each HumanEval problem may provide paired files:

```text
test_inputs/input_<N>.txt   ->   test_outputs/output_<N>.txt
```

Some older problems use `test_<N>.txt` on both sides. Use matching file names
and test every supplied pair.

To test one program and one fixture manually:

```bash
gcc -std=c11 -O2 -Wall -Wextra \
  HumanEval/gpt_codes/000_has_close_elements/merged.c \
  -lm -o /tmp/humaneval_program

/tmp/humaneval_program \
  < HumanEval/gpt_codes/000_has_close_elements/test_inputs/input_0.txt \
  > /tmp/actual.txt

diff -u \
  HumanEval/gpt_codes/000_has_close_elements/test_outputs/output_0.txt \
  /tmp/actual.txt
```

Use the supplied fixtures only as local checks. Passing them does not establish
hidden-test or general semantic correctness.

## 3. Test AtCoder and Codeforces locally

Neither repository contains the official complete judge test suite for these
platforms as the full list of test cases is not public in both plaforms. Test with the public samples from the problem statement for sanity check but for metrics and full fledged evaluation; submit on the official submission links.

### AtCoder

Compile the C program:

```bash
gcc -std=c11 -O2 -Wall -Wextra \
  Atcoder-350/<PROBLEM_ID>/merged.c \
  -o /tmp/atcoder_program
```

Run a public sample after saving it to a local file:

```bash
/tmp/atcoder_program < sample_input.txt > /tmp/actual.txt
diff -u sample_output.txt /tmp/actual.txt
```

The local `description.txt` contains the problem description. The actual task
page is the authoritative source for public samples, limits, and judge rules.

### Codeforces

Run the Python merged program with a public sample:

```bash
python3 'Codeforces Dataset/merged_solutions/sonnet/<PROBLEM_ID>_<PROBLEM_NAME>/merged.py' \
  < sample_input.txt > /tmp/actual.txt
diff -u sample_output.txt /tmp/actual.txt
```

The public samples are stored in the corresponding statement JSON under the
`samples` field. For example,
`Codeforces Dataset/dataset/statements/6C_Alice,_Bob_and_Chocolate.json`
contains `samples[0].input` and `samples[0].output`.

For interactive problems or problems with a custom checker, a byte-for-byte
comparison may be invalid. Follow the official problem's checker or
interaction protocol instead.

## 4. Official submission links

Submitting sends code to an external judge on the website as official test cases are not public.

### Codeforces

For a Codeforces problem ID written as `<CONTEST_ID><INDEX>`, open:

```text
https://codeforces.com/problemset/problem/<CONTEST_ID>/<INDEX>
```

Then choose **Submit** on the problem page and upload or paste `merged.py`.

Example for problem `902D`:

```text
https://codeforces.com/problemset/problem/902/D
```

Here `902` is `<CONTEST_ID>` and `D` is `<INDEX>`. The same pattern applies to
any ID, such as `<PROBLEM_ID>`.

### AtCoder

For an `ABC<CONTEST><TASK>` problem identifier such as `350A`, use:

```text
Task page:   https://atcoder.jp/contests/abc<CONTEST>/tasks/abc<CONTEST>_<task>
Submit page: https://atcoder.jp/contests/abc<CONTEST>/submit
```

Use a lowercase task letter in the task URL. Example for `350A`:

```text
Task page:   https://atcoder.jp/contests/abc350/tasks/abc350_a
Submit page: https://atcoder.jp/contests/abc350/submit
```

Each `Atcoder-350/<PROBLEM_ID>/submission_link.txt` also stores the relevant
contest submission page. On that page, select the task (for example,
`ABC350_A`), choose a C language version compatible with the code, paste
`merged.c`, and submit.

