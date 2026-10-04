import sys

# CLAUSE: parse_known_flow_edges
arr = list(map(int, sys.stdin.buffer.read().split()))
if not arr:
    sys.exit(0)
n = arr[0]
m = arr[1]
items = []
k = 2
for edge_id in range(1, m + 1):
    items.append((edge_id, arr[k], arr[k + 1], arr[k + 2], arr[k + 3]))
    k += 4

# CLAUSE: assign_edge_potentials
items = [(edge_id, start, end, weight * flow) for edge_id, start, end, weight, flow in items]

# CLAUSE: merge_weighted_components
rep = list(range(n + 1))
nodes = [1] * (n + 1)
add_up = [0] * (n + 1)
bottom = [0] * (n + 1)
top = [0] * (n + 1)
bottom_ways = [1] * (n + 1)
top_ways = [1] * (n + 1)
has_left = [False] * (n + 1)
has_right = [False] * (n + 1)
has_left[1] = True
has_right[n] = True

def root(x):
    seq = []
    v = x
    z = 0
    while rep[v] != v:
        seq.append((v, z))
        z += add_up[v]
        v = rep[v]
    r = v
    for v, before in seq:
        rep[v] = r
        add_up[v] = z - before
    return r, z

def take(dst, src, inc):
    lo = bottom[src] + inc
    hi = top[src] + inc
    if lo < bottom[dst]:
        bottom[dst] = lo
        bottom_ways[dst] = bottom_ways[src]
    elif lo == bottom[dst]:
        bottom_ways[dst] += bottom_ways[src]
    if hi > top[dst]:
        top[dst] = hi
        top_ways[dst] = top_ways[src]
    elif hi == top[dst]:
        top_ways[dst] += top_ways[src]
    nodes[dst] += nodes[src]
    has_left[dst] = has_left[dst] or has_left[src]
    has_right[dst] = has_right[dst] or has_right[src]

# CLAUSE: detect_cycle_inconsistency
def put(u, v, gap):
    ru, xu = root(u)
    rv, xv = root(v)
    if ru == rv:
        return xv - xu == gap, ru
    if nodes[ru] < nodes[rv]:
        inc = xv - gap - xu
        rep[ru] = rv
        add_up[ru] = inc
        take(rv, ru, inc)
        return True, rv
    inc = gap + xu - xv
    rep[rv] = ru
    add_up[rv] = inc
    take(ru, rv, inc)
    return True, ru

# CLAUSE: enforce_terminal_ordering
def terminals(component):
    if has_left[component]:
        r, val = root(1)
        if bottom[r] != val:
            return False
        if bottom_ways[r] != 1:
            return False
    if has_right[component]:
        r, val = root(n)
        if top[r] != val:
            return False
        if top_ways[r] != 1:
            return False
    return True

failed = 0
for edge_id, start, end, gap in items:
    ok, component = put(start, end, gap)
    if not ok:
        failed = edge_id
        break
    component = root(end)[0]
    if not terminals(component):
        failed = edge_id
        break

# CLAUSE: derive_efficiency_state
state = "UNKNOWN"
if failed == 0:
    a, va = root(1)
    b, vb = root(n)
    if a == b:
        state = str(vb - va)

# CLAUSE: emit_certified_result
if failed:
    print("BAD", failed)
else:
    print(state)
