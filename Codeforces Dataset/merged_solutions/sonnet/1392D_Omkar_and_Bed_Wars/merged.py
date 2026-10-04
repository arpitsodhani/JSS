import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[2 * i + 2] for i in range(t)]

# Clause run_lengths [Confidence: 1.00]
def run_lengths(s):
    n = len(s)
    start = 0
    while start < n and s[start] == s[n - 1]:
        start += 1
    if start == n:
        return [n]
    runs = []
    length = 1
    for step in range(1, n):
        i = (start + step) % n
        prev = (i - 1) % n
        if s[i] == s[prev]:
            length += 1
        else:
            runs.append(length)
            length = 1
    runs.append(length)
    return runs

# Clause fewest_talks [Confidence: 1.00]
def fewest_talks(s):
    runs = run_lengths(s)
    if len(runs) == 1:
        return (runs[0] + 2) // 3
    total = 0
    for length in runs:
        total += length // 3
    return total

# Clause main [Confidence: 1.00]
def main():
    out = []
    for s in read_input():
        out.append(str(fewest_talks(s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

