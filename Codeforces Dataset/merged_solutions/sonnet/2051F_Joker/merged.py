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
        m = data[pos + 1]
        q = data[pos + 2]
        pos += 3
        ops = data[pos:pos + q]
        pos += q
        cases.append((n, m, ops))
    return cases

# Clause advance [Confidence: 1.00]
def advance(segments, a, n):
    produced = []
    for lo, hi in segments:
        if lo <= a <= hi:
            produced.append((1, 1))
            produced.append((n, n))
        left = min(hi, a - 1)
        if lo <= left:
            produced.append((lo, left + 1))
        right = max(lo, a + 1)
        if right <= hi:
            produced.append((right - 1, hi))
    produced.sort()
    merged = []
    for lo, hi in produced:
        if merged and lo <= merged[-1][1] + 1:
            if hi > merged[-1][1]:
                merged[-1] = (merged[-1][0], hi)
        else:
            merged.append((lo, hi))
    return merged

# Clause solve_case [Confidence: 1.00]
def solve_case(n, m, ops):
    segments = [(m, m)]
    counts = []
    for a in ops:
        segments = advance(segments, a, n)
        counts.append(sum(hi - lo + 1 for lo, hi in segments))
    return counts

# Clause main [Confidence: 1.00]
def main():
    pieces = []
    for case in read_input():
        counts = solve_case(case[0], case[1], case[2])
        pieces.append(" ".join(map(str, counts)))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()

