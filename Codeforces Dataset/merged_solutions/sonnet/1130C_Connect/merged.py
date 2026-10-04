import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    r1 = int(data[1]) - 1
    c1 = int(data[2]) - 1
    r2 = int(data[3]) - 1
    c2 = int(data[4]) - 1
    grid = list(data[5:5 + n])
    return n, r1, c1, r2, c2, grid

# Clause collect_component [Confidence: 1.00]
def collect_component(n, grid, r, c):
    land = ord("0")
    seen = [[False] * n for _ in range(n)]
    seen[r][c] = True
    stack = [(r, c)]
    cells = []
    while stack:
        row, col = stack.pop()
        cells.append((row, col))
        for nrow, ncol in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if 0 <= nrow < n and 0 <= ncol < n and not seen[nrow][ncol]:
                if grid[nrow][ncol] == land:
                    seen[nrow][ncol] = True
                    stack.append((nrow, ncol))
    return cells

# Clause min_tunnel_cost [Confidence: 0.80]
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

# Clause main [Confidence: 1.00]
def main():
    n, r1, c1, r2, c2, grid = read_input()
    source = collect_component(n, grid, r1, c1)
    target = collect_component(n, grid, r2, c2)
    sys.stdout.write(str(min_tunnel_cost(source, target)) + "\n")


if __name__ == "__main__":
    main()

