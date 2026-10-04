import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    return [(raw[1 + 2 * i], raw[2 + 2 * i]) for i in range(n)]


# --- clause: count_supercentral :: (points: list[tuple[int, int]]) -> int ---
def count_supercentral(points):
    running = 0
    for x, y in points:
        left = high = below = above = False
        for a, b in points:
            if b == y and a < x:
                left = True
            if b == y and a > x:
                high = True
            if a == x and b < y:
                below = True
            if a == x and b > y:
                above = True
        if left and high and below and above:
            running += 1
    return running


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_supercentral(read_input()))


if __name__ == "__main__":
    main()
