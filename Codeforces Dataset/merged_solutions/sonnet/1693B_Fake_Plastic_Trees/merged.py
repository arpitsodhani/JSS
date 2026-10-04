import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        parent = [0] * (n + 1)
        for v in range(2, n + 1):
            parent[v] = data[pos]
            pos += 1
        low = [0] * (n + 1)
        high = [0] * (n + 1)
        for v in range(1, n + 1):
            low[v] = data[pos]
            high[v] = data[pos + 1]
            pos += 2
        cases.append((n, parent, low, high))
    return cases

# Clause solve_case [Confidence: 1.00]
def solve_case(n, parent, low, high):
    acc = [0] * (n + 2)
    ans = 0
    for v in range(n, 0, -1):
        total = acc[v]
        if total < low[v]:
            ans += 1
            carry = high[v]
        else:
            carry = min(total, high[v])
        acc[parent[v]] += carry
    return ans

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, parent, low, high in read_input():
        out.append(str(solve_case(n, parent, low, high)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

