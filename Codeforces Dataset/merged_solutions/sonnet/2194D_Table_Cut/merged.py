import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = data[offset]
        m = data[offset + 1]
        offset += 2
        grid = []
        for _ in range(n):
            grid.append(data[offset:offset + m])
            offset += m
        cases.append((n, m, grid))
    return cases

# Clause plan_cut [Confidence: 1.00]
def plan_cut(n, m, grid):
    total = 0
    for row in grid:
        for number in row:
            total += number
    target = total // 2
    edge = [m] * n
    first_side = total
    floor = 0
    for i in range(n):
        while first_side > target and edge[i] > floor:
            edge[i] -= 1
            first_side -= grid[i][edge[i]]
        floor = edge[i]
    return (total - first_side) * first_side, edge

# Clause draw_path [Confidence: 1.00]
def draw_path(n, m, edge):
    moves = []
    here = 0
    for i in range(n):
        moves.append("R" * (edge[i] - here))
        moves.append("D")
        here = edge[i]
    moves.append("R" * (m - here))
    return "".join(moves)

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, m, grid in read_input():
        best, edge = plan_cut(n, m, grid)
        out.append(str(best))
        out.append(draw_path(n, m, edge))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

