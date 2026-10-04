import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = raw[p]
    p += 1
    cases = []
    for _ in range(t):
        n = raw[p]
        m = raw[p + 1]
        q = raw[p + 2]
        p += 3
        ops = raw[p:p + q]
        p += q
        cases.append((n, m, ops))
    return cases


# --- clause: advance :: (segments: list[tuple[int, int]], a: int, n: int) -> list[tuple[int, int]] ---
def advance(segments, a, n):
    gathered = []
    for lo, hi in segments:
        if a >= lo and a <= hi:
            gathered.append((1, 1))
            gathered.append((n, n))
        head = min(hi, a - 1)
        if lo <= head:
            gathered.append((lo, head + 1))
        tail = max(lo, a + 1)
        if tail <= hi:
            gathered.append((tail - 1, hi))
    gathered.sort()
    packed = []
    for lo, hi in gathered:
        if packed and packed[-1][1] + 1 >= lo:
            if packed[-1][1] < hi:
                packed[-1] = (packed[-1][0], hi)
        else:
            packed.append((lo, hi))
    return packed


# --- clause: solve_case :: (n: int, m: int, ops: list[int]) -> list[int] ---
def solve_case(n, m, ops):
    spots = [(m, m)]
    seq = []
    for a in ops:
        spots = advance(spots, a, n)
        seq.append(sum(hi - lo + 1 for lo, hi in spots))
    return seq


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for case in read_input():
        counts = solve_case(case[0], case[1], case[2])
        pieces.append(" ".join(map(str, counts)))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
