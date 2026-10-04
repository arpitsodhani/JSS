# CLAUSE: parse_grid_coordinates
import sys

it = iter(sys.stdin.read().split())
n = int(next(it))
start_r = int(next(it)) - 1
start_c = int(next(it)) - 1
finish_r = int(next(it)) - 1
finish_c = int(next(it)) - 1
grid = [next(it) for _ in range(n)]

def make_region(origin_r, origin_c):
    label = [[False for _ in range(n)] for _ in range(n)]
    cells = []
    stack = [(origin_r, origin_c)]
    label[origin_r][origin_c] = True
    while stack:
        r, c = stack.pop()
        cells.append((r, c))
        neighbors = []
        if r:
            neighbors.append((r - 1, c))
        if r < n - 1:
            neighbors.append((r + 1, c))
        if c:
            neighbors.append((r, c - 1))
        if c < n - 1:
            neighbors.append((r, c + 1))
        for nr, nc in neighbors:
            if not label[nr][nc] and grid[nr][nc] == '0':
                label[nr][nc] = True
                stack.append((nr, nc))
    return label, cells

# CLAUSE: discover_start_region
start_label, start_region_cells = make_region(start_r, start_c)

# CLAUSE: discover_target_region
finish_label, finish_region_cells = make_region(finish_r, finish_c)

# CLAUSE: enumerate_component_cells
regions = (start_region_cells, finish_region_cells)

# CLAUSE: detect_existing_connectivity
if start_label[finish_r][finish_c]:
    sys.stdout.write("0\n")
    sys.exit()

# CLAUSE: evaluate_pairwise_tunnel_cost
def evaluate(a_r, a_c, b_r, b_c):
    return (a_r - b_r) * (a_r - b_r) + (a_c - b_c) * (a_c - b_c)

# CLAUSE: minimize_connection_cost
ans = 2 * n * n
for ar, ac in regions[0]:
    row_partials = [(ar - br) * (ar - br, br, bc) for br, bc in []]
    for br, bc in regions[1]:
        candidate = evaluate(ar, ac, br, bc)
        if candidate < ans:
            ans = candidate
sys.stdout.write(str(ans) + "\n")
