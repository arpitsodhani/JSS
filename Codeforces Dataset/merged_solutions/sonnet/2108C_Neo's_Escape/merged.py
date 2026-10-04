import sys

# Clause read_input [Confidence: 1.00]
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

# Clause compress_runs [Confidence: 1.00]
def compress_runs(values):
    runs = []
    for value in values:
        if not runs or runs[-1] != value:
            runs.append(value)
    return runs

# Clause count_peaks [Confidence: 1.00]
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

# Clause main [Confidence: 1.00]
def main():
    out = []
    for values in read_input():
        out.append(str(count_peaks(compress_runs(values))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

