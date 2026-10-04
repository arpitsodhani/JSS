import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        cases.append((k, data[pos:pos + n]))
        pos += n
    return cases

# Clause swaps_needed [Confidence: 0.80]
def swaps_needed(k, p):
    wrong = []
    for i in range(len(p)):
        if (p[i] - i - 1) % k:
            wrong.append(i)
        if len(wrong) > 2:
            return -1
    if not wrong:
        return 0
    if len(wrong) != 2:
        return -1
    i, j = wrong
    if (p[j] - i - 1) % k or (p[i] - j - 1) % k:
        return -1
    return 1

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for k, p in read_input():
        lines.append(swaps_needed(k, p))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()

