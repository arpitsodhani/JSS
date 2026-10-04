# CLAUSE: parse_garland_cells
import sys
from array import array
from math import sqrt

raw = sys.stdin.buffer.read().split()
pos = 0
n, m, k = map(int, raw[pos:pos + 3])
pos += 3

garland_cells = []
all_bulbs = 0
for gid in range(k):
    amount = int(raw[pos])
    pos += 1
    block = []
    all_bulbs += amount
    for _ in range(amount):
        x, y, w = map(int, raw[pos:pos + 3])
        pos += 3
        block.append((x, y, w))
    garland_cells.append(block)

# CLAUSE: classify_garland_sizes
border = max(1, int(sqrt(all_bulbs)) + 1)
heavy_slot = [-1 for _ in range(k)]
heavy_list = []
for gid, block in enumerate(garland_cells):
    if len(block) > border:
        heavy_slot[gid] = len(heavy_list)
        heavy_list.append(gid)

# CLAUSE: initialize_active_light_index
tree = [array("q", [0]) * (m + 1) for _ in range(n + 1)]

def point_add(r, c, w):
    rr = r
    while rr <= n:
        cc = c
        target = tree[rr]
        while cc <= m:
            target[cc] += w
            cc += cc & -cc
        rr += rr & -rr

def point_prefix(r, c):
    got = 0
    rr = r
    while rr >= 1:
        cc = c
        source = tree[rr]
        while cc >= 1:
            got += source[cc]
            cc -= cc & -cc
        rr -= rr & -rr
    return got

def light_query(r1, c1, r2, c2):
    bottom = point_prefix(r2, c2) - point_prefix(r2, c1 - 1)
    top = point_prefix(r1 - 1, c2) - point_prefix(r1 - 1, c1 - 1)
    return bottom - top

for gid in range(k):
    if heavy_slot[gid] == -1:
        for x, y, w in garland_cells[gid]:
            point_add(x, y, w)

# CLAUSE: build_heavy_prefix_tables
cols = m + 1
heavy_prefix = []
for gid in heavy_list:
    flat = array("q", [0]) * ((n + 1) * cols)
    for x, y, w in garland_cells[gid]:
        flat[x * cols + y] = w
    for x in range(1, n + 1):
        row_base = x * cols
        upper_base = row_base - cols
        carry = 0
        for y in range(1, m + 1):
            carry += flat[row_base + y]
            flat[row_base + y] = carry + flat[upper_base + y]
    heavy_prefix.append(flat)

on = [True for _ in range(k)]
result = []
q = int(raw[pos])
pos += 1

# CLAUSE: apply_light_garland_toggle
def apply_switch(gid):
    if on[gid]:
        on[gid] = False
        delta_sign = -1
    else:
        on[gid] = True
        delta_sign = 1
    if heavy_slot[gid] == -1:
        for x, y, w in garland_cells[gid]:
            point_add(x, y, delta_sign * w)

# CLAUSE: query_heavy_rectangle_delta
def get_from_heavy_table(table, r1, c1, r2, c2):
    a = table[r2 * cols + c2]
    b = table[(r1 - 1) * cols + c2]
    c = table[r2 * cols + c1 - 1]
    d = table[(r1 - 1) * cols + c1 - 1]
    return a - b - c + d

def active_heavy_query(r1, c1, r2, c2):
    subtotal = 0
    for slot in range(len(heavy_list)):
        gid = heavy_list[slot]
        if on[gid]:
            subtotal += get_from_heavy_table(heavy_prefix[slot], r1, c1, r2, c2)
    return subtotal

# CLAUSE: combine_rectangle_answer
for _ in range(q):
    command = raw[pos]
    pos += 1
    if command == b"SWITCH":
        apply_switch(int(raw[pos]) - 1)
        pos += 1
    else:
        r1, c1, r2, c2 = map(int, raw[pos:pos + 4])
        pos += 4
        result.append(str(light_query(r1, c1, r2, c2) + active_heavy_query(r1, c1, r2, c2)))

print("\n".join(result))
