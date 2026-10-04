import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    return [(numbers[1 + 2 * i], numbers[2 + 2 * i]) for i in range(n)]


# --- clause: count_supercentral :: (points: list[tuple[int, int]]) -> int ---
def count_supercentral(points):
    rows = {}
    columns = {}
    for x, y in points:
        rows.setdefault(y, []).append(x)
        columns.setdefault(x, []).append(y)
    total = 0
    for x, y in points:
        row = rows[y]
        column = columns[x]
        if min(row) < x < max(row) and min(column) < y < max(column):
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % count_supercentral(read_input()))


if __name__ == "__main__":
    main()
