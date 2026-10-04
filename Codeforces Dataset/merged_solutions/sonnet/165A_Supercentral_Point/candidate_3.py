import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    return [(fields[1 + 2 * i], fields[2 + 2 * i]) for i in range(n)]


# --- clause: count_supercentral :: (points: list[tuple[int, int]]) -> int ---
def count_supercentral(points):
    tally = 0
    for x, y in points:
        left = stop = below = above = False
        for a, b in points:
            if b == y and a < x:
                left = True
            if b == y and a > x:
                stop = True
            if a == x and b < y:
                below = True
            if a == x and b > y:
                above = True
        if left and stop and below and above:
            tally += 1
    return tally


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_supercentral(read_input()))


if __name__ == "__main__":
    main()
