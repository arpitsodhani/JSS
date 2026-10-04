import sys


# --- clause: read_input :: () -> tuple[int, int, list[str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    grid = [data[2 + i].decode() for i in range(n)]
    return n, m, grid


# --- clause: segments_ok :: (n: int, m: int, grid: list[str]) -> bool ---
def segments_ok(n, m, grid):
    for row in grid:
        blocks = 0
        run = False
        for ch in row:
            if ch == "#":
                if not run:
                    blocks += 1
                    run = True
            else:
                run = False
        if blocks > 1:
            return False
    for c in range(m):
        blocks = 0
        run = False
        for r in range(n):
            if grid[r][c] == "#":
                if not run:
                    blocks += 1
                    run = True
            else:
                run = False
        if blocks > 1:
            return False
    empty_row = any("#" not in row for row in grid)
    empty_col = any(all(grid[r][c] == "." for r in range(n)) for c in range(m))
    return empty_row == empty_col


# --- clause: count_components :: (n: int, m: int, grid: list[str]) -> int ---
def count_components(n, m, grid):
    parent = list(range(n * m))
    total = 0
    for r in range(n):
        row = grid[r]
        for c in range(m):
            if row[c] != "#":
                continue
            total += 1
            here = r * m + c
            for other in ((here - 1) if c and row[c - 1] == "#" else -1,
                          (here - m) if r and grid[r - 1][c] == "#" else -1):
                if other < 0:
                    continue
                a = other
                while parent[a] != a:
                    parent[a] = parent[parent[a]]
                    a = parent[a]
                b = here
                while parent[b] != b:
                    parent[b] = parent[parent[b]]
                    b = parent[b]
                if a != b:
                    parent[a] = b
                    total -= 1
    return total

# --- clause: main :: () -> None ---
def main():
    n, m, grid = read_input()
    if not segments_ok(n, m, grid):
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(str(count_components(n, m, grid)) + "\n")


if __name__ == "__main__":
    main()
