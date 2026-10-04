import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, int, list[bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    r1, c1 = int(data[1]) - 1, int(data[2]) - 1
    r2, c2 = int(data[3]) - 1, int(data[4]) - 1
    grid = data[5:5 + n]
    return n, r1, c1, r2, c2, grid


# --- clause: collect_component :: (n: int, grid: list[bytes], r: int, c: int) -> list[tuple[int, int]] ---
def collect_component(n, grid, r, c):
    land = ord("0")
    seen = [[False] * n for _ in range(n)]
    seen[r][c] = True
    stack = [(r, c)]
    cells = []
    while stack:
        row, col = stack.pop()
        cells.append((row, col))
        for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nrow = row + drow
            ncol = col + dcol
            if 0 <= nrow < n and 0 <= ncol < n and not seen[nrow][ncol]:
                if grid[nrow][ncol] == land:
                    seen[nrow][ncol] = True
                    stack.append((nrow, ncol))
    return cells


# --- clause: min_tunnel_cost :: (first: list[tuple[int, int]], second: list[tuple[int, int]]) -> int ---
def min_tunnel_cost(first, second):
    best = 1 << 60
    for ar, ac in first:
        for br, bc in second:
            cost = (ar - br) * (ar - br) + (ac - bc) * (ac - bc)
            if cost < best:
                best = cost
    return best


# --- clause: main :: () -> None ---
def main():
    n, r1, c1, r2, c2, grid = read_input()
    source = collect_component(n, grid, r1, c1)
    target = collect_component(n, grid, r2, c2)
    sys.stdout.write(str(min_tunnel_cost(source, target)) + "\n")


if __name__ == "__main__":
    main()
