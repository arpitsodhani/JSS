import sys


# --- clause: read_input :: () -> list[list[str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cursor = 1
    cases = []
    for _ in range(t):
        n = int(numbers[cursor])
        cursor += 2
        grid = [numbers[cursor + i].decode() for i in range(n)]
        cursor += n
        cases.append(grid)
    return cases


# --- clause: trapped_count :: (grid: list[str]) -> int ---
def trapped_count(grid):
    n = len(grid)
    m = len(grid[0])
    steps = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    free = [[False] * m for _ in range(n)]
    holes = [[0] * m for _ in range(n)]
    stack = []
    for i in range(n):
        for j in range(m):
            ch = grid[i][j]
            if ch == "?":
                gone = 0
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    y = i + di
                    x = j + dj
                    if y < 0 or y >= n or x < 0 or x >= m:
                        gone += 1
                holes[i][j] = gone
                if gone == 4:
                    free[i][j] = True
                    stack.append((i, j))
                continue
            di, dj = steps[ch]
            y = i + di
            x = j + dj
            if y < 0 or y >= n or x < 0 or x >= m:
                free[i][j] = True
                stack.append((i, j))
    while stack:
        i, j = stack.pop()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            y = i + di
            x = j + dj
            if y < 0 or y >= n or x < 0 or x >= m or free[y][x]:
                continue
            ch = grid[y][x]
            if ch == "?":
                holes[y][x] += 1
                if holes[y][x] < 4:
                    continue
            else:
                ey, ex = steps[ch]
                if y + ey != i or x + ex != j:
                    continue
            free[y][x] = True
            stack.append((y, x))
    trapped = 0
    for i in range(n):
        for j in range(m):
            if not free[i][j]:
                trapped += 1
    return trapped


# --- clause: main :: () -> None ---
def main():
    out = []
    for grid in read_input():
        out.append(trapped_count(grid))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
