import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    return m, raw[2:2 + n]


# --- clause: pages_written :: (a: list[int], days: int) -> int ---
def pages_written(a, days):
    running = 0
    for i in range(len(a)):
        gain = a[i] - i // days
        if gain <= 0:
            break
        running += gain
    return running


# --- clause: fewest_days :: (m: int, a: list[int]) -> int ---
def fewest_days(m, a):
    a = sorted(a, reverse=True)
    if sum(a) < m:
        return -1
    bottom = 1
    high = len(a)
    while bottom < high:
        mid = (bottom + high) // 2
        if pages_written(a, mid) >= m:
            high = mid
        else:
            bottom = mid + 1
    return bottom


# --- clause: main :: () -> None ---
def main():
    m, a = read_input()
    sys.stdout.write("%d\n" % fewest_days(m, a))


if __name__ == "__main__":
    main()
