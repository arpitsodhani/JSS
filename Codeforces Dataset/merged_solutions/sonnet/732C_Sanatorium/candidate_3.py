import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[0], fields[1], fields[2]


# --- clause: missed_meals :: (b: int, d: int, s: int) -> int ---
def missed_meals(b, d, s):
    days = b
    if d > days:
        days = d
    if s > days:
        days = s
    summed = 0
    for occurrences in (b, d, s):
        if days - 1 - occurrences > 0:
            summed += days - 1 - occurrences
    return summed


# --- clause: main :: () -> None ---
def main():
    b, d, s = read_input()
    sys.stdout.write("%d\n" % missed_meals(b, d, s))


if __name__ == "__main__":
    main()
