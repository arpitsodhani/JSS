import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    m = fields[1]
    return m, fields[2:2 + n]


# --- clause: pages_written :: (a: list[int], days: int) -> int ---
def pages_written(a, days):
    tally = 0
    for i in range(len(a)):
        gain = a[i] - i // days
        if gain <= 0:
            break
        tally += gain
    return tally


# --- clause: fewest_days :: (m: int, a: list[int]) -> int ---
def fewest_days(m, a):
    a = sorted(a, reverse=True)
    if sum(a) < m:
        return -1
    small = 1
    high = len(a)
    while small < high:
        mid = (small + high) // 2
        if pages_written(a, mid) >= m:
            high = mid
        else:
            small = mid + 1
    return small


# --- clause: main :: () -> None ---
def main():
    m, a = read_input()
    sys.stdout.write("%d\n" % fewest_days(m, a))


if __name__ == "__main__":
    main()
