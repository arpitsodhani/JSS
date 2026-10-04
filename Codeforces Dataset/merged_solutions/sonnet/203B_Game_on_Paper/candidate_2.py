import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    m = values[1]
    cells = []
    pos = 2
    for _ in range(m):
        cells.append((values[pos], values[pos + 1]))
        pos += 2
    return n, cells


# --- clause: completes_square :: (grid: list[list[int]], x: int, y: int, n: int) -> bool ---
def completes_square(grid, x, y, n):
    for cx in range(max(1, x - 2), x + 1):
        if cx + 2 > n:
            continue
        for cy in range(max(1, y - 2), y + 1):
            if cy + 2 > n:
                continue
            count = 0
            for dx in range(3):
                for dy in range(3):
                    count += grid[cx + dx][cy + dy]
            if count == 9:
                return True
    return False


# --- clause: find_move :: (n: int, cells: list[tuple[int, int]]) -> int ---
def find_move(n, cells):
    grid = [[0] * (n + 3) for _ in range(n + 3)]
    move = 0
    for cell in cells:
        move += 1
        grid[cell[0]][cell[1]] = 1
        if completes_square(grid, cell[0], cell[1], n):
            return move
    return -1


# --- clause: main :: () -> None ---
def main():
    n, cells = read_input()
    sys.stdout.write(str(find_move(n, cells)) + "\n")


if __name__ == "__main__":
    main()
