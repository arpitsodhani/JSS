import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 1
    total = int(data[0])
    cases = []
    for _ in range(total):
        n = int(data[idx])
        idx += 1
        values = list(map(int, data[idx:idx + n]))
        idx += n
        cases.append(values)
    return cases


# --- clause: compress_runs :: (values: list[int]) -> list[int] ---
def compress_runs(values):
    runs = []
    previous = None
    for value in values:
        if value != previous:
            runs.append(value)
            previous = value
    return runs


# --- clause: count_peaks :: (runs: list[int]) -> int ---
def count_peaks(runs):
    total = len(runs)
    clones = 0
    for i in range(total):
        left_ok = i == 0 or runs[i - 1] < runs[i]
        right_ok = i + 1 == total or runs[i + 1] < runs[i]
        if left_ok and right_ok:
            clones += 1
    return clones


# --- clause: main :: () -> None ---
def main():
    answers = []
    for values in read_input():
        runs = compress_runs(values)
        answers.append(str(count_peaks(runs)))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
