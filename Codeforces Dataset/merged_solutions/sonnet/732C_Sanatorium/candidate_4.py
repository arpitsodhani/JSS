import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2]


# --- clause: missed_meals :: (b: int, d: int, s: int) -> int ---
def missed_meals(b, d, s):
    days = max(b, d, s)
    served = min(b, days - 1) + min(d, days - 1) + min(s, days - 1)
    return 3 * (days - 1) - served


# --- clause: main :: () -> None ---
def main():
    b, d, s = read_input()
    sys.stdout.write("%d\n" % missed_meals(b, d, s))


if __name__ == "__main__":
    main()
