import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int], list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    a = int(data[2])
    boys = [int(token) for token in data[3:3 + n]]
    bikes = [int(token) for token in data[3 + n:3 + n + m]]
    return n, m, a, boys, bikes


# --- clause: affordable :: (count: int, a: int, boys: list[int], bikes: list[int]) -> bool ---
def affordable(count, a, boys, bikes):
    need = 0
    start = len(boys) - count
    for i in range(count):
        gap = bikes[i] - boys[start + i]
        if gap > 0:
            need += gap
            if need > a:
                return False
    return need <= a


# --- clause: best_plan :: (n: int, m: int, a: int, boys: list[int], bikes: list[int]) -> tuple[int, int] ---
def best_plan(n, m, a, boys, bikes):
    boys.sort()
    bikes.sort()
    lo = 0
    hi = n if n < m else m
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if affordable(mid, a, boys, bikes):
            lo = mid
        else:
            hi = mid - 1
    total = 0
    for i in range(lo):
        total += bikes[i]
    spent = total - a
    if spent < 0:
        spent = 0
    return lo, spent


# --- clause: main :: () -> None ---
def main():
    n, m, a, boys, bikes = read_input()
    count, spent = best_plan(n, m, a, boys, bikes)
    sys.stdout.write("%d %d\n" % (count, spent))


if __name__ == "__main__":
    main()
