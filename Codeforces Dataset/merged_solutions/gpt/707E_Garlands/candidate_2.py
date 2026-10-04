# CLAUSE: parse_garland_cells
import sys
from array import array

tokens = sys.stdin.buffer.read().split()
ptr = 0
n = int(tokens[ptr]); ptr += 1
m = int(tokens[ptr]); ptr += 1
k = int(tokens[ptr]); ptr += 1

owned_cells = []
bulb_total = 0
for _ in range(k):
    length = int(tokens[ptr]); ptr += 1
    current = []
    bulb_total += length
    for _ in range(length):
        row = int(tokens[ptr]); ptr += 1
        col = int(tokens[ptr]); ptr += 1
        val = int(tokens[ptr]); ptr += 1
        current.append((row, col, val))
    owned_cells.append(current)

# CLAUSE: classify_garland_sizes
threshold = int(bulb_total ** 0.5) + 2
large_index = [-1] * k
large_garlands = []
for garland_id in range(k):
    if len(owned_cells[garland_id]) >= threshold:
        large_index[garland_id] = len(large_garlands)
        large_garlands.append(garland_id)

# CLAUSE: initialize_active_light_index
fenwick = [array("q", [0]) * (m + 1) for _ in range(n + 1)]

def update(row, col, value):
    while row <= n:
        c = col
        line = fenwick[row]
        while c <= m:
            line[c] += value
            c += c & -c
        row += row & -row

def prefix(row, col):
    ans = 0
    while row:
        c = col
        line = fenwick[row]
        while c:
            ans += line[c]
            c &= c - 1
        row &= row - 1
    return ans

def fenwick_rectangle(a, b, c, d):
    return prefix(c, d) - prefix(a - 1, d) - prefix(c, b - 1) + prefix(a - 1, b - 1)

for garland_id, cells in enumerate(owned_cells):
    if large_index[garland_id] == -1:
        for row, col, val in cells:
            update(row, col, val)

# CLAUSE: build_heavy_prefix_tables
stride = m + 1
prefix_tables = []
for garland_id in large_garlands:
    pref = array("q", [0]) * ((n + 1) * stride)
    for row, col, val in owned_cells[garland_id]:
        pref[row * stride + col] += val
    for row in range(1, n + 1):
        above = (row - 1) * stride
        here = row * stride
        for col in range(1, m + 1):
            pref[here + col] += pref[here + col - 1] + pref[above + col] - pref[above + col - 1]
    prefix_tables.append(pref)

enabled = [1] * k
answers = []
queries = int(tokens[ptr]); ptr += 1

# CLAUSE: apply_light_garland_toggle
def toggle(garland_id):
    enabled[garland_id] ^= 1
    if large_index[garland_id] < 0:
        multiplier = 1 if enabled[garland_id] else -1
        for row, col, val in owned_cells[garland_id]:
            update(row, col, multiplier * val)

# CLAUSE: query_heavy_rectangle_delta
def table_rectangle(pref, a, b, c, d):
    return pref[c * stride + d] - pref[(a - 1) * stride + d] - pref[c * stride + b - 1] + pref[(a - 1) * stride + b - 1]

def large_sum(a, b, c, d):
    add = 0
    for pos, garland_id in enumerate(large_garlands):
        if enabled[garland_id]:
            add += table_rectangle(prefix_tables[pos], a, b, c, d)
    return add

# CLAUSE: combine_rectangle_answer
for _ in range(queries):
    typ = tokens[ptr]; ptr += 1
    if typ[0] == 83:
        toggle(int(tokens[ptr]) - 1)
        ptr += 1
    else:
        r1 = int(tokens[ptr]); ptr += 1
        c1 = int(tokens[ptr]); ptr += 1
        r2 = int(tokens[ptr]); ptr += 1
        c2 = int(tokens[ptr]); ptr += 1
        answers.append(str(fenwick_rectangle(r1, c1, r2, c2) + large_sum(r1, c1, r2, c2)))

sys.stdout.write("\n".join(answers))
