import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        pos += 1
        bounds = [int(token) for token in data[pos:pos + 2 * n]]
        pos += 2 * n
        cases.append(bounds)
    return cases


# --- clause: reachable :: (bounds: list[int], k: int) -> bool ---
def reachable(bounds, k):
    low = 0
    high = 0
    for i in range(0, len(bounds), 2):
        low -= k
        high += k
        if low < bounds[i]:
            low = bounds[i]
        if high > bounds[i + 1]:
            high = bounds[i + 1]
        if low > high:
            return False
    return True


# --- clause: smallest_reach :: (bounds: list[int]) -> int ---
def smallest_reach(bounds):
    lo = 0
    hi = 1
    while not reachable(bounds, hi):
        hi *= 2
    while lo < hi:
        mid = (lo + hi) >> 1
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
    print("\n".join(out))


if __name__ == "__main__":
    main()
