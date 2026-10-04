import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    n = nums[0]
    m = nums[1]
    cells = []
    cursor = 2
    while len(cells) < m:
        cells.append((nums[cursor], nums[cursor + 1]))
        cursor += 2
    return n, cells


# --- clause: completes_square :: (grid: list[list[int]], x: int, y: int, n: int) -> bool ---
def completes_square(grid, x, y, n):
    for cx in range(x - 2, x + 1):
        for cy in range(y - 2, y + 1):
            if cx < 1 or cy < 1 or cx + 2 > n or cy + 2 > n:
                continue
            black = 0
            for dx in range(3):
                for dy in range(3):
                    if grid[cx + dx][cy + dy] == 1:
                        black += 1
            if black == 9:
                return True
    return False


# --- clause: find_move :: (n: int, cells: list[tuple[int, int]]) -> int ---
def find_move(n, cells):
    grid = [[0] * (n + 3) for _ in range(n + 3)]
    answer = -1
    for i in range(len(cells)):
        x, y = cells[i]
        grid[x][y] = 1
        if completes_square(grid, x, y, n):
            answer = i + 1
            break
    return answer


# --- clause: main :: () -> None ---
def main():
    n, cells = read_input()
    print(find_move(n, cells))


if __name__ == "__main__":
    main()
