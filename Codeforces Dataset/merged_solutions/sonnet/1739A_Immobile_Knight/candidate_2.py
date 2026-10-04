import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    return [(tokens[1 + 2 * i], tokens[2 + 2 * i]) for i in range(t)]


# --- clause: find_cell :: (n: int, m: int) -> tuple[int, int] ---
def find_cell(n, m):
    steps = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    for line in range(1, n + 1):
        for column in range(1, m + 1):
            stuck = True
            for dr, dc in steps:
                r = line + dr
                c = column + dc
                if 1 <= r <= n and 1 <= c <= m:
                    stuck = False
                    break
            if stuck:
                return line, column
    return 1, 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m in read_input():
        line, column = find_cell(n, m)
        out.append("%d %d" % (line, column))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
