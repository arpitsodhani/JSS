import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[0], raw[1], raw[2]


# --- clause: missed_meals :: (b: int, d: int, s: int) -> int ---
def missed_meals(b, d, s):
    days = b
    if d > days:
        days = d
    if s > days:
        days = s
    running = 0
    for hits in (b, d, s):
        if days - 1 - hits > 0:
            running += days - 1 - hits
    return running


# --- clause: main :: () -> None ---
def main():
    b, d, s = read_input()
    sys.stdout.write("%d\n" % missed_meals(b, d, s))


if __name__ == "__main__":
    main()
