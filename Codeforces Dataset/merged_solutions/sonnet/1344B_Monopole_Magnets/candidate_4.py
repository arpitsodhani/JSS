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
    empty_row = False
    for row in grid:
        first = row.find("#")
        if first < 0:
            empty_row = True
            continue
        last = row.rfind("#")
        if row.count("#") != last - first + 1:
            return False
    empty_col = False
    for c in range(m):
        column = "".join(grid[r][c] for r in range(n))
        first = column.find("#")
        if first < 0:
            empty_col = True
            continue
        last = column.rfind("#")
        if column.count("#") != last - first + 1:
            return False
    return empty_row == empty_col


# --- clause: count_components :: (n: int, m: int, grid: list[str]) -> int ---
def count_components(n, m, grid):
    seen = [[False] * m for _ in range(n)]
    total = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] != "#" or seen[r][c]:
                continue
            total += 1
            stack = [(r, c)]
            seen[r][c] = True
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "#" and not seen[nx][ny]:
                        seen[nx][ny] = True
                        stack.append((nx, ny))
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
