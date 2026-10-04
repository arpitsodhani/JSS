import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos = pos + 1
        values = list(map(int, data[pos:pos + n]))
        pos = pos + n
        cases.append(values)
    return cases


# --- clause: compress_runs :: (values: list[int]) -> list[int] ---
def compress_runs(values):
    runs = []
    for value in values:
        if runs and runs[-1] == value:
            continue
        runs.append(value)
    return runs


# --- clause: count_peaks :: (runs: list[int]) -> int ---
def count_peaks(runs):
    total = len(runs)
    clones = 0
    for i in range(total):
        higher_left = i > 0 and runs[i - 1] > runs[i]
        higher_right = i + 1 < total and runs[i + 1] > runs[i]
        if not higher_left and not higher_right:
            clones += 1
    return clones


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(str(count_peaks(compress_runs(values))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
