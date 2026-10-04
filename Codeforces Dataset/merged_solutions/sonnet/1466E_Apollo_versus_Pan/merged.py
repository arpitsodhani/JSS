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

# Clause bit_counts [Confidence: 1.00]
def bit_counts(x):
    counts = [0] * 60
    for value in x:
        while value:
            bottom = value & (-value)
            counts[bottom.bit_length() - 1] += 1
            value -= bottom
    return counts

# Clause triple_sum [Confidence: 1.00]
def triple_sum(x, counts):
    mod = 1000000007
    n = len(x)
    total = 0
    for value in x:
        left = 0
        right = 0
        for b in range(60):
            if (value >> b) & 1:
                left += (1 << b) * counts[b]
                right += (1 << b) * n
            else:
                right += (1 << b) * counts[b]
        total += (left % mod) * (right % mod)
    return total % mod

# Clause main [Confidence: 1.00]
def main():
    out = []
    for x in read_input():
        out.append(triple_sum(x, bit_counts(x)))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

