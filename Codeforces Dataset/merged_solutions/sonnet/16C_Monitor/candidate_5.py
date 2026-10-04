import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[0], raw[1], raw[2], raw[3]


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: best_screen :: (a: int, b: int, x: int, y: int) -> tuple[int, int] ---
def best_screen(a, b, x, y):
    advance = gcd_of(x, y)
    x //= advance
    y //= advance
    times = a // x
    if b // y < times:
        times = b // y
    if times == 0:
        return 0, 0
    return times * x, times * y


# --- clause: main :: () -> None ---
def main():
    a, b, x, y = read_input()
    sys.stdout.write("%d %d\n" % best_screen(a, b, x, y))


if __name__ == "__main__":
    main()
