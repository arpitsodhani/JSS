import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1]))
        pos += 2
    return cases

# Clause build [Confidence: 0.80]
def build(values, k):
    if k == 1:
        return list(values)
    total = len(values)
    keep = (1 << (k - 2)) + 1
    survivors = build(values[total - keep:], k - 1)
    fillers = values[:total - keep]
    split = len(fillers) - (keep - 1)
    extras = fillers[:split]
    gaps = fillers[split:]
    result = list(extras)
    for i, value in enumerate(survivors):
        result.append(value)
        if i < len(gaps):
            result.append(gaps[i])
    return result

# Clause solve_case [Confidence: 1.00]
def solve_case(n, k):
    if (1 << (k - 1)) >= n:
        return "-1"
    return " ".join(map(str, build(list(range(1, n + 1)), k)))

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, k in read_input():
        out.append(solve_case(n, k))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

