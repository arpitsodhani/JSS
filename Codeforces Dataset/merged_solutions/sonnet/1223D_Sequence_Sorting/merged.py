import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    queries = data[ptr]
    ptr += 1
    cases = []
    for _ in range(queries):
        n = data[ptr]
        ptr += 1
        arr = data[ptr:ptr + n]
        ptr += n
        cases.append(arr)
    return cases

# Clause solve_case [Confidence: 1.00]
def solve_case(a):
    n = len(a)
    first = {}
    last = {}
    for i in range(n):
        v = a[i]
        if v not in first:
            first[v] = i
        last[v] = i
    vals = sorted(first)
    best = 1
    cur = 1
    for j in range(1, len(vals)):
        if last[vals[j - 1]] < first[vals[j]]:
            cur += 1
        else:
            cur = 1
        if cur > best:
            best = cur
    return len(vals) - best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(str(solve_case(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

