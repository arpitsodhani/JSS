import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    return [(fields[1 + 2 * i], fields[2 + 2 * i]) for i in range(t)]


# --- clause: find_cell :: (n: int, m: int) -> tuple[int, int] ---
def find_cell(n, m):
    steps = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    for entry_row in range(1, n + 1):
        for column in range(1, m + 1):
            stuck = True
            for dr, dc in steps:
                r = entry_row + dr
                c = column + dc
                if 1 <= r <= n and 1 <= c <= m:
                    stuck = False
                    break
            if stuck:
                return entry_row, column
    return 1, 1


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n, m in read_input():
        entry_row, column = find_cell(n, m)
        pieces.append("%d %d" % (entry_row, column))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
