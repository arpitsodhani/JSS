import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    total = tokens[idx]
    idx += 1
    cases = []
    for _ in range(total):
        n = tokens[idx]
        m = tokens[idx + 1]
        q = tokens[idx + 2]
        idx += 3
        ops = tokens[idx:idx + q]
        idx += q
        cases.append((n, m, ops))
    return cases


# --- clause: advance :: (segments: list[tuple[int, int]], a: int, n: int) -> list[tuple[int, int]] ---
def advance(segments, a, n):
    raw = []
    for lo, hi in segments:
        if lo <= a <= hi:
            raw.append((1, 1))
            raw.append((n, n))
        cut = min(hi, a - 1)
        if cut >= lo:
            raw.append((lo, cut + 1))
        start = max(lo, a + 1)
        if start <= hi:
            raw.append((start - 1, hi))
    raw.sort(key=lambda seg: seg[0])
    clean = []
    for lo, hi in raw:
        if clean and lo <= clean[-1][1] + 1:
            prev_lo, prev_hi = clean[-1]
            clean[-1] = (prev_lo, hi if hi > prev_hi else prev_hi)
        else:
            clean.append((lo, hi))
    return clean


# --- clause: solve_case :: (n: int, m: int, ops: list[int]) -> list[int] ---
def solve_case(n, m, ops):
    current = [(m, m)]
    report = []
    for i in range(len(ops)):
        current = advance(current, ops[i], n)
        report.append(sum(hi - lo + 1 for lo, hi in current))
    return report


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n, m, ops in read_input():
        lines.append(" ".join(str(v) for v in solve_case(n, m, ops)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
