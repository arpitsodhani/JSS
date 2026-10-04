import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        c = data[pos + 1]
        d = data[pos + 2]
        pos += 3
        cases.append((n, c, d, data[pos:pos + n]))
        pos += n
    return cases

# Clause solve_case [Confidence: 1.00]
def solve_case(n, c, d, a):
    distinct = sorted(set(a))
    best = n * c + d
    for i, value in enumerate(distinct, start=1):
        cost = (n - i) * c + (value - i) * d
        if cost < best:
            best = cost
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, c, d, a in read_input():
        out.append(str(solve_case(n, c, d, a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

