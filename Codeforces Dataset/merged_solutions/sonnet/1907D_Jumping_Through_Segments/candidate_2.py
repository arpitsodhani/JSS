import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        bounds = list(map(int, data[pos:pos + 2 * n]))
        pos += 2 * n
        cases.append(bounds)
    return cases


# --- clause: reachable :: (bounds: list[int], k: int) -> bool ---
def reachable(bounds, k):
    low = 0
    high = 0
    i = 0
    total = len(bounds)
    while i < total:
        low = max(low - k, bounds[i])
        high = min(high + k, bounds[i + 1])
        if high < low:
            return False
        i += 2
    return True


# --- clause: smallest_reach :: (bounds: list[int]) -> int ---
def smallest_reach(bounds):
    lo = 0
    hi = 1000000000
    while lo < hi:
        mid = (lo + hi) // 2
        if reachable(bounds, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


# --- clause: main :: () -> None ---
def main():
    out = []
    for bounds in read_input():
        out.append(str(smallest_reach(bounds)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
