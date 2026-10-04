import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    return [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(t)]


# --- clause: find_cell :: (n: int, m: int) -> tuple[int, int] ---
def find_cell(n, m):
    steps = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    for row in range(1, n + 1):
        for column in range(1, m + 1):
            stuck = True
            for dr, dc in steps:
                r = row + dr
                c = column + dc
                if 1 <= r <= n and 1 <= c <= m:
                    stuck = False
                    break
            if stuck:
                return row, column
    return 1, 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m in read_input():
        row, column = find_cell(n, m)
        out.append("%d %d" % (row, column))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
