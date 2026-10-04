# CLAUSE: parse_grid_coordinates
import sys
from collections import deque

data = sys.stdin.read().strip().split()
n = int(data[0])
sr, sc = int(data[1]) - 1, int(data[2]) - 1
tr, tc = int(data[3]) - 1, int(data[4]) - 1
grid = data[5:5 + n]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(start_r, start_c):
    seen = [[False] * n for _ in range(n)]
    cells = []
    q = deque([(start_r, start_c)])
    seen[start_r][start_c] = True
    while q:
        r, c = q.popleft()
        cells.append((r, c))
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc] and grid[nr][nc] == '0':
                seen[nr][nc] = True
                q.append((nr, nc))
    return seen, cells

# CLAUSE: discover_start_region
start_seen, start_cells = bfs(sr, sc)

# CLAUSE: discover_target_region
target_seen, target_cells = bfs(tr, tc)

# CLAUSE: enumerate_component_cells
left_component = start_cells
right_component = target_cells

# CLAUSE: detect_existing_connectivity
if start_seen[tr][tc]:
    print(0)
    sys.exit()

# CLAUSE: evaluate_pairwise_tunnel_cost
def tunnel_cost(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

# CLAUSE: minimize_connection_cost
answer = 10 ** 18
for a in left_component:
    for b in right_component:
        answer = min(answer, tunnel_cost(a, b))
print(answer)
