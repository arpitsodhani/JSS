# CLAUSE: parse_grid_coordinates
import sys
from collections import deque

lines = sys.stdin.read().splitlines()
n = int(lines[0])
r1, c1 = map(lambda x: int(x) - 1, lines[1].split())
r2, c2 = map(lambda x: int(x) - 1, lines[2].split())
grid = lines[3:3 + n]

def flood(start):
    reached = set([start])
    cells = []
    q = deque([start])
    while q:
        r, c = q.popleft()
        cells.append((r, c))
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == '0' and (nr, nc) not in reached:
                reached.add((nr, nc))
                q.append((nr, nc))
    return reached, cells

# CLAUSE: discover_start_region
start_reached, from_start = flood((r1, c1))

# CLAUSE: discover_target_region
target_reached, from_target = flood((r2, c2))

# CLAUSE: enumerate_component_cells
start_component = list(from_start)
target_component = list(from_target)

# CLAUSE: detect_existing_connectivity
if (r2, c2) in start_reached:
    print(0)
    sys.exit(0)

# CLAUSE: evaluate_pairwise_tunnel_cost
def cost_between(p, q):
    row_gap = p[0] - q[0]
    col_gap = p[1] - q[1]
    return row_gap * row_gap + col_gap * col_gap

# CLAUSE: minimize_connection_cost
minimum = None
for p in start_component:
    for q in target_component:
        current = cost_between(p, q)
        if minimum is None or current < minimum:
            minimum = current
print(minimum)
