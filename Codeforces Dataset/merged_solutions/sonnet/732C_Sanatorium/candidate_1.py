import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]


# --- clause: missed_meals :: (b: int, d: int, s: int) -> int ---
def missed_meals(b, d, s):
    days = b
    if d > days:
        days = d
    if s > days:
        days = s
    total = 0
    for count in (b, d, s):
        if days - 1 - count > 0:
            total += days - 1 - count
    return total


# --- clause: main :: () -> None ---
def main():
    b, d, s = read_input()
    sys.stdout.write("%d\n" % missed_meals(b, d, s))


if __name__ == "__main__":
    main()
