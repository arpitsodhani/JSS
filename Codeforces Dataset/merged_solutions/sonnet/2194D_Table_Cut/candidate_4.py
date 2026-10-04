import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[list[int]]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        m = numbers[reader + 1]
        reader += 2
        grid = []
        for _ in range(n):
            grid.append(numbers[reader:reader + m])
            reader += m
        cases.append((n, m, grid))
    return cases


# --- clause: plan_cut :: (n: int, m: int, grid: list[list[int]]) -> tuple[int, list[int]] ---
def plan_cut(n, m, grid):
    total = 0
    for row in grid:
        for value in row:
            total += value
    target = total // 2
    edge = [0] * n
    taken = 0
    for i in range(n - 1, -1, -1):
        cap = edge[i + 1] if i + 1 < n else m
        j = 0
        while j < cap and taken + grid[i][j] <= target:
            taken += grid[i][j]
            j += 1
        edge[i] = j
    return taken * (total - taken), edge


# --- clause: draw_path :: (n: int, m: int, edge: list[int]) -> str ---
def draw_path(n, m, edge):
    moves = []
    here = 0
    for i in range(n):
        moves.append("R" * (edge[i] - here))
        moves.append("D")
        here = edge[i]
    moves.append("R" * (m - here))
    return "".join(moves)


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m, grid in read_input():
        best, edge = plan_cut(n, m, grid)
        out.append(str(best))
        out.append(draw_path(n, m, edge))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
