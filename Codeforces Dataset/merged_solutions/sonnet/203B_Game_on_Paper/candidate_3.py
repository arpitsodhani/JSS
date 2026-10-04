import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    size = tokens[0]
    moves = tokens[1]
    cells = [(tokens[2 + 2 * i], tokens[3 + 2 * i]) for i in range(moves)]
    return size, cells


# --- clause: completes_square :: (grid: list[list[int]], x: int, y: int, n: int) -> bool ---
def completes_square(grid, x, y, n):
    lo_x = x - 2 if x - 2 > 1 else 1
    lo_y = y - 2 if y - 2 > 1 else 1
    for cx in range(lo_x, x + 1):
        if cx + 2 > n:
            break
        for cy in range(lo_y, y + 1):
            if cy + 2 > n:
                break
            ok = True
            for dx in range(3):
                row = grid[cx + dx]
                for dy in range(3):
                    if not row[cy + dy]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return True
    return False


# --- clause: find_move :: (n: int, cells: list[tuple[int, int]]) -> int ---
def find_move(n, cells):
    grid = [[0] * (n + 3) for _ in range(n + 3)]
    for i in range(len(cells)):
        x = cells[i][0]
        y = cells[i][1]
        grid[x][y] = 1
        if completes_square(grid, x, y, n):
            return i + 1
    return -1


# --- clause: main :: () -> None ---
def main():
    n, cells = read_input()
    answer = find_move(n, cells)
    print(answer)


if __name__ == "__main__":
    main()
