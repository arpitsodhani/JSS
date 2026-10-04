# CLAUSE: parse_grid_coordinates
import sys
from collections import deque

raw = sys.stdin.readline
n = int(raw())
a_r, a_c = [int(x) - 1 for x in raw().split()]
b_r, b_c = [int(x) - 1 for x in raw().split()]
grid = [raw().strip() for _ in range(n)]
steps = [-1, 0, 1, 0, -1]

def traverse(seed_r, seed_c):
    used = [[False] * n for _ in range(n)]
    bag = []
    queue = deque()
    queue.append((seed_r, seed_c))
    used[seed_r][seed_c] = True
    while queue:
        r, c = queue.popleft()
        bag.append((r, c))
        for k in range(4):
            nr = r + steps[k]
            nc = c + steps[k + 1]
            inside = 0 <= nr < n and 0 <= nc < n
            if inside and grid[nr][nc] == '0' and not used[nr][nc]:
                used[nr][nc] = True
                queue.append((nr, nc))
    return used, bag

# CLAUSE: discover_start_region
reachable_from_a, cells_from_a = traverse(a_r, a_c)

# CLAUSE: discover_target_region
reachable_from_b, cells_from_b = traverse(b_r, b_c)

# CLAUSE: enumerate_component_cells
first_cells = cells_from_a[:]
second_cells = cells_from_b[:]

# CLAUSE: detect_existing_connectivity
if reachable_from_a[b_r][b_c]:
    print(0)
    sys.exit()

# CLAUSE: evaluate_pairwise_tunnel_cost
def pair_cost(first, second):
    x = first[0] - second[0]
    y = first[1] - second[1]
    return x * x + y * y

# CLAUSE: minimize_connection_cost
best_cost = float("inf")
for first in first_cells:
    costs = [pair_cost(first, second) for second in second_cells]
    local = min(costs)
    if local < best_cost:
        best_cost = local
print(best_cost)
