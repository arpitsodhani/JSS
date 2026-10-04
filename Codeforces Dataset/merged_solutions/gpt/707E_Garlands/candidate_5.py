# CLAUSE: parse_garland_cells
import sys
from array import array

items = sys.stdin.buffer.read().split()
idx = 0
n = int(items[idx]); idx += 1
m = int(items[idx]); idx += 1
k = int(items[idx]); idx += 1

by_garland = []
lamp_count = 0
for _ in range(k):
    size = int(items[idx])
    idx += 1
    one = []
    lamp_count += size
    for _ in range(size):
        rr = int(items[idx])
        cc = int(items[idx + 1])
        ww = int(items[idx + 2])
        idx += 3
        one += [(rr, cc, ww)]
    by_garland += [one]

# CLAUSE: classify_garland_sizes
barrier = max(1, round(lamp_count ** 0.5))
heavy_map = {}
heavy_order = []
for gid in range(k):
    if len(by_garland[gid]) > barrier:
        heavy_map[gid] = len(heavy_order)
        heavy_order.append(gid)

# CLAUSE: initialize_active_light_index
fen = [array("q", [0]) * (m + 1) for _ in range(n + 1)]

def insert(x, y, z):
    while x <= n:
        y2 = y
        fen_x = fen[x]
        while y2 <= m:
            fen_x[y2] += z
            y2 += y2 & -y2
        x += x & -x

def accum(x, y):
    s = 0
    while x > 0:
        y2 = y
        fen_x = fen[x]
        while y2 > 0:
            s += fen_x[y2]
            y2 -= y2 & -y2
        x -= x & -x
    return s

def dynamic_rect(x1, y1, x2, y2):
    return accum(x2, y2) + accum(x1 - 1, y1 - 1) - accum(x1 - 1, y2) - accum(x2, y1 - 1)

for gid, one in enumerate(by_garland):
    if gid not in heavy_map:
        for x, y, z in one:
            insert(x, y, z)

# CLAUSE: build_heavy_prefix_tables
w = m + 1
heavy_data = []
for gid in heavy_order:
    grid = array("q", [0]) * ((n + 1) * w)
    for x, y, z in by_garland[gid]:
        grid[x * w + y] += z
    for x in range(1, n + 1):
        row_offset = x * w
        prev_offset = row_offset - w
        y = 1
        while y <= m:
            grid[row_offset + y] += grid[row_offset + y - 1] + grid[prev_offset + y] - grid[prev_offset + y - 1]
            y += 1
    heavy_data.append(grid)

state = [1 for _ in range(k)]
ans = []
q = int(items[idx])
idx += 1

# CLAUSE: apply_light_garland_toggle
def flip(gid):
    state[gid] ^= 1
    if gid not in heavy_map:
        coef = (state[gid] << 1) - 1
        for x, y, z in by_garland[gid]:
            insert(x, y, coef * z)

# CLAUSE: query_heavy_rectangle_delta
def read_heavy(grid, x1, y1, x2, y2):
    p1 = x2 * w + y2
    p2 = (x1 - 1) * w + y2
    p3 = x2 * w + y1 - 1
    p4 = (x1 - 1) * w + y1 - 1
    return grid[p1] - grid[p2] - grid[p3] + grid[p4]

def heavy_part(x1, y1, x2, y2):
    s = 0
    for slot, gid in enumerate(heavy_order):
        if state[gid]:
            s += read_heavy(heavy_data[slot], x1, y1, x2, y2)
    return s

# CLAUSE: combine_rectangle_answer
for _ in range(q):
    word = items[idx]
    idx += 1
    if word[0] == 65:
        x1 = int(items[idx]); y1 = int(items[idx + 1]); x2 = int(items[idx + 2]); y2 = int(items[idx + 3])
        idx += 4
        ans.append(str(dynamic_rect(x1, y1, x2, y2) + heavy_part(x1, y1, x2, y2)))
    else:
        flip(int(items[idx]) - 1)
        idx += 1

sys.stdout.write("\n".join(ans))
