import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[list[int]]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        m = fields[cursor + 1]
        cursor += 2
        grid = []
        for _ in range(n):
            grid.append(fields[cursor:cursor + m])
            cursor += m
        cases.append((n, m, grid))
    return cases


# --- clause: plan_cut :: (n: int, m: int, grid: list[list[int]]) -> tuple[int, list[int]] ---
def plan_cut(n, m, grid):
    total = 0
    for row in grid:
        for value in row:
            total += value
    target = total // 2
    edge = [m] * n
    begin = total
    floor = 0
    for i in range(n):
        while begin > target and edge[i] > floor:
            edge[i] -= 1
            begin -= grid[i][edge[i]]
        floor = edge[i]
    return (total - begin) * begin, edge


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
