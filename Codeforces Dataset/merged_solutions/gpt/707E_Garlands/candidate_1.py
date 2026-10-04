# CLAUSE: parse_garland_cells
import sys
from math import isqrt
from array import array

data = sys.stdin.buffer.read().split()
it = iter(data)
n = int(next(it))
m = int(next(it))
k = int(next(it))

garlands = []
total_bulbs = 0
for _ in range(k):
    cnt = int(next(it))
    cells = []
    total_bulbs += cnt
    for _ in range(cnt):
        r = int(next(it))
        c = int(next(it))
        v = int(next(it))
        cells.append((r, c, v))
    garlands.append(cells)

# CLAUSE: classify_garland_sizes
limit = max(1, isqrt(max(1, total_bulbs)) + 1)
is_heavy = [len(g) > limit for g in garlands]
heavy_pos = {}
heavy_ids = []
for idx, g in enumerate(garlands):
    if is_heavy[idx]:
        heavy_pos[idx] = len(heavy_ids)
        heavy_ids.append(idx)

# CLAUSE: initialize_active_light_index
bit = [array("q", [0]) * (m + 1) for _ in range(n + 1)]

def add_cell(x, y, delta):
    i = x
    while i <= n:
        row = bit[i]
        j = y
        while j <= m:
            row[j] += delta
            j += j & -j
        i += i & -i

def bit_sum(x, y):
    res = 0
    i = x
    while i > 0:
        row = bit[i]
        j = y
        while j > 0:
            res += row[j]
            j -= j & -j
        i -= i & -i
    return res

def rect_sum(x1, y1, x2, y2):
    return bit_sum(x2, y2) - bit_sum(x1 - 1, y2) - bit_sum(x2, y1 - 1) + bit_sum(x1 - 1, y1 - 1)

for gid, cells in enumerate(garlands):
    if not is_heavy[gid]:
        for r, c, v in cells:
            add_cell(r, c, v)

# CLAUSE: build_heavy_prefix_tables
heavy_tables = []
width = m + 1
size = (n + 1) * (m + 1)
for gid in heavy_ids:
    table = array("q", [0]) * size
    for r, c, v in garlands[gid]:
        table[r * width + c] += v
    for r in range(1, n + 1):
        base = r * width
        prev = (r - 1) * width
        run = 0
        for c in range(1, m + 1):
            run += table[base + c]
            table[base + c] = run + table[prev + c]
    heavy_tables.append(table)

active = [True] * k
out = []
q = int(next(it))

# CLAUSE: apply_light_garland_toggle
def switch_garland(gid):
    active[gid] = not active[gid]
    if not is_heavy[gid]:
        sign = 1 if active[gid] else -1
        for r, c, v in garlands[gid]:
            add_cell(r, c, sign * v)

# CLAUSE: query_heavy_rectangle_delta
def heavy_rect(table, x1, y1, x2, y2):
    return table[x2 * width + y2] - table[(x1 - 1) * width + y2] - table[x2 * width + y1 - 1] + table[(x1 - 1) * width + y1 - 1]

def heavy_delta(x1, y1, x2, y2):
    res = 0
    for gid in heavy_ids:
        if active[gid]:
            res += heavy_rect(heavy_tables[heavy_pos[gid]], x1, y1, x2, y2)
    return res

# CLAUSE: combine_rectangle_answer
for _ in range(q):
    op = next(it)
    if op == b"SWITCH":
        switch_garland(int(next(it)) - 1)
    else:
        x1 = int(next(it))
        y1 = int(next(it))
        x2 = int(next(it))
        y2 = int(next(it))
        out.append(str(rect_sum(x1, y1, x2, y2) + heavy_delta(x1, y1, x2, y2)))

sys.stdout.write("\n".join(out))
