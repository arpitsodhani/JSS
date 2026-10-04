# CLAUSE: parse_garland_cells
import sys
from array import array

inp = sys.stdin.buffer.read().split()
at = 0
n = int(inp[at]); m = int(inp[at + 1]); k = int(inp[at + 2])
at += 3

chains = [[] for _ in range(k)]
bulbs_seen = 0
for g in range(k):
    s = int(inp[at])
    at += 1
    bulbs_seen += s
    for _ in range(s):
        chains[g].append((int(inp[at]), int(inp[at + 1]), int(inp[at + 2])))
        at += 3

# CLAUSE: classify_garland_sizes
cutoff = 1
while cutoff * cutoff < max(1, bulbs_seen):
    cutoff += 1
heavy_no = [-1] * k
heavies = []
for g in range(k):
    if len(chains[g]) > cutoff:
        heavy_no[g] = len(heavies)
        heavies.append(g)

# CLAUSE: initialize_active_light_index
fw = [array("q", [0]) * (m + 1) for _ in range(n + 1)]

def fw_add(r, c, val):
    r0 = r
    while r0 < n + 1:
        c0 = c
        row = fw[r0]
        while c0 < m + 1:
            row[c0] += val
            c0 += c0 & -c0
        r0 += r0 & -r0

def fw_pref(r, c):
    total = 0
    r0 = r
    while r0:
        c0 = c
        row = fw[r0]
        while c0:
            total += row[c0]
            c0 -= c0 & -c0
        r0 -= r0 & -r0
    return total

def fw_box(r1, c1, r2, c2):
    total = fw_pref(r2, c2)
    total -= fw_pref(r1 - 1, c2)
    total -= fw_pref(r2, c1 - 1)
    total += fw_pref(r1 - 1, c1 - 1)
    return total

for g, chain in enumerate(chains):
    if heavy_no[g] == -1:
        for cell in chain:
            fw_add(cell[0], cell[1], cell[2])

# CLAUSE: build_heavy_prefix_tables
row_len = m + 1
heavy_ps = []
for g in heavies:
    ps = array("q", [0]) * ((n + 1) * row_len)
    for r, c, val in chains[g]:
        ps[r * row_len + c] += val
    for r in range(1, n + 1):
        left_sum = 0
        row_start = r * row_len
        prev_start = (r - 1) * row_len
        for c in range(1, m + 1):
            idx = row_start + c
            left_sum += ps[idx]
            ps[idx] = left_sum + ps[prev_start + c]
    heavy_ps.append(ps)

lit = bytearray([1]) * k
outs = []
query_count = int(inp[at])
at += 1

# CLAUSE: apply_light_garland_toggle
def do_switch(g):
    lit[g] = 0 if lit[g] else 1
    if heavy_no[g] == -1:
        if lit[g]:
            for r, c, val in chains[g]:
                fw_add(r, c, val)
        else:
            for r, c, val in chains[g]:
                fw_add(r, c, -val)

# CLAUSE: query_heavy_rectangle_delta
def ps_box(ps, r1, c1, r2, c2):
    high = ps[r2 * row_len + c2] - ps[(r1 - 1) * row_len + c2]
    low = ps[r2 * row_len + c1 - 1] - ps[(r1 - 1) * row_len + c1 - 1]
    return high - low

def heavy_box(r1, c1, r2, c2):
    total = 0
    for i, g in enumerate(heavies):
        if lit[g]:
            total += ps_box(heavy_ps[i], r1, c1, r2, c2)
    return total

# CLAUSE: combine_rectangle_answer
for _ in range(query_count):
    if inp[at] == b"ASK":
        at += 1
        r1 = int(inp[at]); c1 = int(inp[at + 1]); r2 = int(inp[at + 2]); c2 = int(inp[at + 3])
        at += 4
        outs.append(str(fw_box(r1, c1, r2, c2) + heavy_box(r1, c1, r2, c2)))
    else:
        at += 1
        do_switch(int(inp[at]) - 1)
        at += 1

sys.stdout.write("\n".join(outs))
