import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        pos += 1
        values = list(map(int, data[pos:pos + n]))
        pos += n
        cases.append(values)
    return cases


# --- clause: compress_runs :: (values: list[int]) -> list[int] ---
def compress_runs(values):
    runs = []
    for value in values:
        if len(runs) == 0 or runs[len(runs) - 1] != value:
            runs.append(value)
    return runs


# --- clause: count_peaks :: (runs: list[int]) -> int ---
def count_peaks(runs):
    total = len(runs)
    clones = 0
    for i in range(total):
        if i > 0 and runs[i] < runs[i - 1]:
            continue
        if i + 1 < total and runs[i] < runs[i + 1]:
            continue
        clones = clones + 1
    return clones


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(str(count_peaks(compress_runs(values))))
    print("\n".join(out))


if __name__ == "__main__":
    main()
