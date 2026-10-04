import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    cursor = 0
    count = nums[cursor]
    cursor += 1
    cases = []
    while len(cases) < count:
        n = nums[cursor]
        m = nums[cursor + 1]
        q = nums[cursor + 2]
        cursor += 3
        ops = nums[cursor:cursor + q]
        cursor += q
        cases.append((n, m, ops))
    return cases


# --- clause: advance :: (segments: list[tuple[int, int]], a: int, n: int) -> list[tuple[int, int]] ---
def advance(segments, a, n):
    buckets = []
    for lo, hi in segments:
        if lo <= a <= hi:
            buckets.append((1, 1))
            buckets.append((n, n))
        if lo < a:
            buckets.append((lo, min(hi, a - 1) + 1))
        if hi > a:
            buckets.append((max(lo, a + 1) - 1, hi))
    buckets.sort()
    result = []
    for lo, hi in buckets:
        if result and lo - 1 <= result[-1][1]:
            if hi > result[-1][1]:
                result[-1] = (result[-1][0], hi)
        else:
            result.append((lo, hi))
    return result


# --- clause: solve_case :: (n: int, m: int, ops: list[int]) -> list[int] ---
def solve_case(n, m, ops):
    reach = [(m, m)]
    values = []
    for a in ops:
        reach = advance(reach, a, n)
        width = 0
        for lo, hi in reach:
            width += hi - lo + 1
        values.append(width)
    return values


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    out = []
    for i in range(len(cases)):
        n, m, ops = cases[i]
        out.append(" ".join(map(str, solve_case(n, m, ops))))
    print("\n".join(out))


if __name__ == "__main__":
    main()
