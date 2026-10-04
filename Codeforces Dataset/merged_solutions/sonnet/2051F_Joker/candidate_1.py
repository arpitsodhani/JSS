import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
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


# --- clause: advance :: (segments: list[tuple[int, int]], a: int, n: int) -> list[tuple[int, int]] ---
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


# --- clause: solve_case :: (n: int, m: int, ops: list[int]) -> list[int] ---
def solve_case(n, m, ops):
    segments = [(m, m)]
    counts = []
    for a in ops:
        segments = advance(segments, a, n)
        counts.append(sum(hi - lo + 1 for lo, hi in segments))
    return counts


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m, ops in read_input():
        out.append(" ".join(map(str, solve_case(n, m, ops))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
