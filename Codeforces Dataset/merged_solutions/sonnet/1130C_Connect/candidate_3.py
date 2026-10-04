import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, int, list[bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    start_row = int(data[1]) - 1
    start_col = int(data[2]) - 1
    goal_row = int(data[3]) - 1
    goal_col = int(data[4]) - 1
    grid = data[5:5 + n]
    return n, start_row, start_col, goal_row, goal_col, grid


# --- clause: collect_component :: (n: int, grid: list[bytes], r: int, c: int) -> list[tuple[int, int]] ---
def collect_component(n, grid, r, c):
    land = ord("0")
    seen = set()
    seen.add((r, c))
    stack = [(r, c)]
    cells = []
    while stack:
        row, col = stack.pop()
        cells.append((row, col))
        for nrow, ncol in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
            if nrow < 0 or nrow >= n or ncol < 0 or ncol >= n:
                continue
            if (nrow, ncol) in seen:
                continue
            if grid[nrow][ncol] == land:
                seen.add((nrow, ncol))
                stack.append((nrow, ncol))
    return cells


# --- clause: min_tunnel_cost :: (first: list[tuple[int, int]], second: list[tuple[int, int]]) -> int ---
def min_tunnel_cost(first, second):
    best = 1 << 60
    for ar, ac in first:
        for br, bc in second:
            dr = ar - br
            dc = ac - bc
            cost = dr * dr + dc * dc
            if cost < best:
                best = cost
    return best


# --- clause: main :: () -> None ---
def main():
    n, r1, c1, r2, c2, grid = read_input()
    start = collect_component(n, grid, r1, c1)
    goal = collect_component(n, grid, r2, c2)
    print(min_tunnel_cost(start, goal))


if __name__ == "__main__":
    main()
