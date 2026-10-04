import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    return [(tokens[1 + 2 * i], tokens[2 + 2 * i]) for i in range(n)]


# --- clause: count_supercentral :: (points: list[tuple[int, int]]) -> int ---
def count_supercentral(points):
    amount = 0
    for x, y in points:
        left = right = below = above = False
        for a, b in points:
            if b == y and a < x:
                left = True
            if b == y and a > x:
                right = True
            if a == x and b < y:
                below = True
            if a == x and b > y:
                above = True
        if left and right and below and above:
            amount += 1
    return amount


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_supercentral(read_input()))


if __name__ == "__main__":
    main()
