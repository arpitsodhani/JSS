import sys

# CLAUSE: parse_known_flow_edges
tokens = list(map(int, sys.stdin.buffer.read().split()))
if not tokens:
    raise SystemExit
n = tokens[0]
m = tokens[1]
raw = []
at = 2
for number in range(1, m + 1):
    u = tokens[at]
    v = tokens[at + 1]
    w = tokens[at + 2]
    b = tokens[at + 3]
    at += 4
    raw.append((number, u, v, w, b))

# CLAUSE: assign_edge_potentials
constraints = []
for number, u, v, w, b in raw:
    constraints.append((number, u, v, w * b))

# CLAUSE: merge_weighted_components
par = [i for i in range(n + 1)]
rank_size = [1] * (n + 1)
rel = [0] * (n + 1)
mn = [0] * (n + 1)
mx = [0] * (n + 1)
mn_count = [1] * (n + 1)
mx_count = [1] * (n + 1)
seen1 = [False] * (n + 1)
seenn = [False] * (n + 1)
seen1[1] = True
seenn[n] = True

def leader(x):
    path = []
    s = 0
    y = x
    while par[y] != y:
        path.append((y, s))
        s += rel[y]
        y = par[y]
    root = y
    for node, before in path:
        par[node] = root
        rel[node] = s - before
    return root, s

def combine(root, child, delta):
    cmn = mn[child] + delta
    cmx = mx[child] + delta
    if cmn == mn[root]:
        mn_count[root] += mn_count[child]
    elif cmn < mn[root]:
        mn[root] = cmn
        mn_count[root] = mn_count[child]
    if cmx == mx[root]:
        mx_count[root] += mx_count[child]
    elif cmx > mx[root]:
        mx[root] = cmx
        mx_count[root] = mx_count[child]
    rank_size[root] += rank_size[child]
    seen1[root] = seen1[root] or seen1[child]
    seenn[root] = seenn[root] or seenn[child]

# CLAUSE: detect_cycle_inconsistency
def add_constraint(u, v, need):
    ru, pu = leader(u)
    rv, pv = leader(v)
    if ru == rv:
        return pv - pu == need, ru
    if rank_size[ru] >= rank_size[rv]:
        move = need + pu - pv
        par[rv] = ru
        rel[rv] = move
        combine(ru, rv, move)
        return True, ru
    move = pv - need - pu
    par[ru] = rv
    rel[ru] = move
    combine(rv, ru, move)
    return True, rv

# CLAUSE: enforce_terminal_ordering
def ordered(root):
    if seen1[root]:
        r, base = leader(1)
        if mn[r] != base:
            return False
        if mn_count[r] != 1:
            return False
    if seenn[root]:
        r, top = leader(n)
        if mx[r] != top:
            return False
        if mx_count[r] != 1:
            return False
    return True

first_bad = 0
for number, u, v, need in constraints:
    good, comp = add_constraint(u, v, need)
    if not good:
        first_bad = number
        break
    comp = leader(v)[0]
    if not ordered(comp):
        first_bad = number
        break

# CLAUSE: derive_efficiency_state
fixed = False
value = 0
if first_bad == 0:
    a, va = leader(1)
    b, vb = leader(n)
    if a == b:
        fixed = True
        value = vb - va

# CLAUSE: emit_certified_result
if first_bad:
    sys.stdout.write("BAD " + str(first_bad) + "\n")
elif fixed:
    sys.stdout.write(str(value) + "\n")
else:
    sys.stdout.write("UNKNOWN\n")
