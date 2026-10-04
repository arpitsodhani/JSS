import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2]


# --- clause: count_tiles :: (a: int, b: int, c: int) -> int ---
def count_tiles(a, b, c):
    rows = b + c - 1
    total = 0
    for i in range(rows):
        grow = i
        if b - 1 < grow:
            grow = b - 1
        if c - 1 < grow:
            grow = c - 1
        if rows - 1 - i < grow:
            grow = rows - 1 - i
        total += a + grow
    return total


# --- clause: main :: () -> None ---
def main():
    a, b, c = read_input()
    sys.stdout.write("%d\n" % count_tiles(a, b, c))


if __name__ == "__main__":
    main()
