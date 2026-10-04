import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# Clause best_sum [Confidence: 1.00]
def best_sum(a):
    total = sum(a)
    best = -(1 << 62)
    for i in range(len(a) - 1):
        gain = -2 * (a[i] + a[i + 1])
        if gain > best:
            best = gain
    return total + best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(best_sum(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

