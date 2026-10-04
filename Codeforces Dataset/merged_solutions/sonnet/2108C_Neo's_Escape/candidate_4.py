import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 1
    t = int(data[0])
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        values = [int(data[pos + i]) for i in range(n)]
        pos += n
        cases.append(values)
    return cases


# --- clause: compress_runs :: (values: list[int]) -> list[int] ---
def compress_runs(values):
    runs = []
    for value in values:
        if not runs:
            runs.append(value)
        elif runs[-1] != value:
            runs.append(value)
    return runs


# --- clause: count_peaks :: (runs: list[int]) -> int ---
def count_peaks(runs):
    total = len(runs)
    clones = 0
    for i in range(total):
        if i > 0 and runs[i - 1] > runs[i]:
            continue
        if i + 1 < total and runs[i + 1] > runs[i]:
            continue
        clones += 1
    return clones


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        runs = compress_runs(values)
        out.append(str(count_peaks(runs)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
