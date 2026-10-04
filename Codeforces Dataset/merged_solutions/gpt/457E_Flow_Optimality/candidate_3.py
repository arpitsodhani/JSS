import sys

# CLAUSE: parse_known_flow_edges
inp = sys.stdin.buffer.read().split()
if not inp:
    sys.exit()
it = iter(inp)
n = int(next(it))
m = int(next(it))
links = []
for idx in range(1, m + 1):
    f = int(next(it))
    t = int(next(it))
    w = int(next(it))
    b = int(next(it))
    links.append((idx, f, t, w, b))

# CLAUSE: assign_edge_potentials
drops = [(idx, f, t, w * b) for idx, f, t, w, b in links]

# CLAUSE: merge_weighted_components
root_of = list(range(n + 1))
mass = [1] * (n + 1)
to_parent = [0] * (n + 1)
low = [0] * (n + 1)
high = [0] * (n + 1)
low_num = [1] * (n + 1)
high_num = [1] * (n + 1)
source_inside = [False] * (n + 1)
sink_inside = [False] * (n + 1)
source_inside[1] = True
sink_inside[n] = True

def get(x):
    r = x
    val = 0
    while root_of[r] != r:
        val += to_parent[r]
        r = root_of[r]
    node = x
    passed = 0
    while root_of[node] != node:
        nxt = root_of[node]
        edge = to_parent[node]
        root_of[node] = r
        to_parent[node] = val - passed
        passed += edge
        node = nxt
    return r, val

def install(parent_root, child_root, offset):
    child_low = low[child_root] + offset
    child_high = high[child_root] + offset
    new_low = low[parent_root]
    new_low_num = low_num[parent_root]
    if child_low < new_low:
        new_low = child_low
        new_low_num = low_num[child_root]
    elif child_low == new_low:
        new_low_num += low_num[child_root]
    new_high = high[parent_root]
    new_high_num = high_num[parent_root]
    if child_high > new_high:
        new_high = child_high
        new_high_num = high_num[child_root]
    elif child_high == new_high:
        new_high_num += high_num[child_root]
    low[parent_root] = new_low
    high[parent_root] = new_high
    low_num[parent_root] = new_low_num
    high_num[parent_root] = new_high_num
    mass[parent_root] += mass[child_root]
    source_inside[parent_root] |= source_inside[child_root]
    sink_inside[parent_root] |= sink_inside[child_root]

# CLAUSE: detect_cycle_inconsistency
def apply_edge(u, v, delta):
    a, au = get(u)
    b, bv = get(v)
    if a == b:
        if bv - au != delta:
            return False, a
        return True, a
    if mass[a] < mass[b]:
        offset = bv - delta - au
        root_of[a] = b
        to_parent[a] = offset
        install(b, a, offset)
        return True, b
    offset = delta + au - bv
    root_of[b] = a
    to_parent[b] = offset
    install(a, b, offset)
    return True, a

# CLAUSE: enforce_terminal_ordering
def boundary_holds(component):
    if source_inside[component]:
        sr, sv = get(1)
        if low[sr] < sv or low_num[sr] != 1:
            return False
    if sink_inside[component]:
        tr, tv = get(n)
        if high[tr] > tv or high_num[tr] != 1:
            return False
    return True

bad = -1
for idx, u, v, delta in drops:
    ok, component = apply_edge(u, v, delta)
    if not ok:
        bad = idx
        break
    component = get(u)[0]
    if not boundary_holds(component):
        bad = idx
        break

# CLAUSE: derive_efficiency_state
known = False
eff = 0
if bad < 0:
    left_root, left_val = get(1)
    right_root, right_val = get(n)
    if left_root == right_root:
        known = True
        eff = right_val - left_val

# CLAUSE: emit_certified_result
out = []
if bad >= 0:
    out.append("BAD " + str(bad))
elif known:
    out.append(str(eff))
else:
    out.append("UNKNOWN")
sys.stdout.write(out[0] + "\n")
