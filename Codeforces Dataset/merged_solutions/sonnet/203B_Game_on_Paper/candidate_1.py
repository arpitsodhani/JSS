import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    cells = []
    for i in range(m):
        cells.append((data[2 + 2 * i], data[3 + 2 * i]))
    return n, cells


# --- clause: completes_square :: (grid: list[list[int]], x: int, y: int, n: int) -> bool ---
def completes_square(grid, x, y, n):
    for cx in range(x - 2, x + 1):
        if cx < 1 or cx + 2 > n:
            continue
        for cy in range(y - 2, y + 1):
            if cy < 1 or cy + 2 > n:
                continue
            full = True
            for dx in range(3):
                for dy in range(3):
                    if grid[cx + dx][cy + dy] == 0:
                        full = False
                        break
                if not full:
                    break
            if full:
                return True
    return False


# --- clause: find_move :: (n: int, cells: list[tuple[int, int]]) -> int ---
def find_move(n, cells):
    grid = [[0] * (n + 3) for _ in range(n + 3)]
    for step in range(len(cells)):
        x, y = cells[step]
        grid[x][y] = 1
        if completes_square(grid, x, y, n):
            return step + 1
    return -1


# --- clause: main :: () -> None ---
def main():
    n, cells = read_input()
    print(find_move(n, cells))


if __name__ == "__main__":
    main()
