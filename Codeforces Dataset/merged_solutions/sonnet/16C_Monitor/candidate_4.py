import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2], numbers[3]


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: best_screen :: (a: int, b: int, x: int, y: int) -> tuple[int, int] ---
def best_screen(a, b, x, y):
    step = gcd_of(x, y)
    width = x // step
    height = y // step
    if width > a or height > b:
        return 0, 0
    times = min(a // width, b // height)
    return width * times, height * times


# --- clause: main :: () -> None ---
def main():
    a, b, x, y = read_input()
    sys.stdout.write("%d %d\n" % best_screen(a, b, x, y))


if __name__ == "__main__":
    main()
