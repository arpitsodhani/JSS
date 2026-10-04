import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        k = int(data[pos + 1])
        pos += 2
        values = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((n, k, values))
    return cases

# Clause best_sum [Confidence: 1.00]
def best_sum(n, k, values):
    values.sort()
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + values[i]
    total = prefix[n]
    best = None
    for pairs in range(k + 1):
        singles = k - pairs
        low = 2 * pairs
        if low + singles > n:
            continue
        keep = total - prefix[low] - (prefix[n] - prefix[n - singles])
        if best is None or keep > best:
            best = keep
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, k, values in read_input():
        out.append(str(best_sum(n, k, values)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

