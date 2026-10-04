# CLAUSE: parse_grid_coordinates
import sys

tokens = sys.stdin.buffer.read().split()
n = int(tokens[0])
r1 = int(tokens[1]) - 1
c1 = int(tokens[2]) - 1
r2 = int(tokens[3]) - 1
c2 = int(tokens[4]) - 1
grid = [row.decode() for row in tokens[5:5 + n]]

def collect_component(root_r, root_c):
    stack = [(root_r, root_c)]
    visited = [[0] * n for _ in range(n)]
    visited[root_r][root_c] = 1
    cells = []
    while stack:
        r, c = stack.pop()
        cells.append((r, c))
        if r > 0 and not visited[r - 1][c] and grid[r - 1][c] == '0':
            visited[r - 1][c] = 1
            stack.append((r - 1, c))
        if r + 1 < n and not visited[r + 1][c] and grid[r + 1][c] == '0':
            visited[r + 1][c] = 1
            stack.append((r + 1, c))
        if c > 0 and not visited[r][c - 1] and grid[r][c - 1] == '0':
            visited[r][c - 1] = 1
            stack.append((r, c - 1))
        if c + 1 < n and not visited[r][c + 1] and grid[r][c + 1] == '0':
            visited[r][c + 1] = 1
            stack.append((r, c + 1))
    return visited, cells

# CLAUSE: discover_start_region
start_mark, start_group = collect_component(r1, c1)

# CLAUSE: discover_target_region
target_mark, target_group = collect_component(r2, c2)

# CLAUSE: enumerate_component_cells
component_a = [(x, y) for x, y in start_group]
component_b = [(x, y) for x, y in target_group]

# CLAUSE: detect_existing_connectivity
if start_mark[r2][c2]:
    print(0)
    raise SystemExit

# CLAUSE: evaluate_pairwise_tunnel_cost
def squared_distance(x1, y1, x2, y2):
    dr = x1 - x2
    dc = y1 - y2
    return dr * dr + dc * dc

# CLAUSE: minimize_connection_cost
best = n * n * 2
for x1, y1 in component_a:
    for x2, y2 in component_b:
        value = squared_distance(x1, y1, x2, y2)
        if value < best:
            best = value
print(best)
