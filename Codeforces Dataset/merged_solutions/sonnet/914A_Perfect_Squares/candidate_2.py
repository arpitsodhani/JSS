import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = list(map(int, data[1:n + 1]))
    return n, values


# --- clause: is_square :: (value: int) -> bool ---
def is_square(value):
    if value < 0:
        return False
    lo = 0
    hi = 1000
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * mid < value:
            lo = mid + 1
        else:
            hi = mid
    return lo * lo == value


# --- clause: largest_plain :: (n: int, values: list[int]) -> int ---
def largest_plain(n, values):
    best = None
    for value in values:
        if is_square(value):
            continue
        if best is None or value > best:
            best = value
    return best


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    sys.stdout.write("%d\n" % largest_plain(n, values))


if __name__ == "__main__":
    main()
