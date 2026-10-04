import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        x = data[pos + 1]
        pos += 2
        jumps = []
        for _ in range(n):
            jumps.append((data[pos], data[pos + 1], data[pos + 2]))
            pos += 3
        cases.append((n, x, jumps))
    return cases

# Clause fewest_rollbacks [Confidence: 1.00]
def fewest_rollbacks(n, x, jumps):
    free = 0
    best_gain = 0
    for a, b, c in jumps:
        free += (b - 1) * a
        gain = b * a - c
        if gain > best_gain:
            best_gain = gain
    if free >= x:
        return 0
    if best_gain <= 0:
        return -1
    missing = x - free
    return (missing + best_gain - 1) // best_gain

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, x, jumps in read_input():
        out.append(str(fewest_rollbacks(n, x, jumps)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

