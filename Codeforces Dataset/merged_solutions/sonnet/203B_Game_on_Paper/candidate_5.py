import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    coords = raw[2:2 + 2 * m]
    cells = [(coords[2 * i], coords[2 * i + 1]) for i in range(m)]
    return n, cells


# --- clause: completes_square :: (grid: list[list[int]], x: int, y: int, n: int) -> bool ---
def completes_square(grid, x, y, n):
    for cx in range(x - 2, x + 1):
        if cx < 1 or cx > n - 2:
            continue
        for cy in range(y - 2, y + 1):
            if cy < 1 or cy > n - 2:
                continue
            total = 0
            for dx in range(3):
                total += grid[cx + dx][cy] + grid[cx + dx][cy + 1] + grid[cx + dx][cy + 2]
            if total == 9:
                return True
    return False


# --- clause: find_move :: (n: int, cells: list[tuple[int, int]]) -> int ---
def find_move(n, cells):
    grid = [[0] * (n + 3) for _ in range(n + 3)]
    idx = 0
    for x, y in cells:
        idx += 1
        grid[x][y] = 1
        if completes_square(grid, x, y, n):
            return idx
    return -1


# --- clause: main :: () -> None ---
def main():
    n, cells = read_input()
    sys.stdout.write("%d\n" % find_move(n, cells))


if __name__ == "__main__":
    main()
