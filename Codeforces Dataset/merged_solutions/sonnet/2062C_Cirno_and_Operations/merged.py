import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = raw[p]
    p += 1
    cases = []
    for _ in range(t):
        n = raw[p]
        p += 1
        values = raw[p:p + n]
        p += n
        cases.append(values)
    return cases

# Clause solve_case [Confidence: 1.00]
def solve_case(a):
    cur = list(a)
    best = sum(cur)
    while len(cur) > 1:
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        total = sum(cur)
        if total < 0:
            total = -total
        if total > best:
            best = total
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(str(solve_case(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

