# Clause parse_known_flow_edges [Confidence: 0.60]
import sys

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


# Clause assign_edge_potentials [Confidence: 0.80]
drops = [(idx, f, t, w * b) for idx, f, t, w, b in links]


# Clause merge_weighted_components [Confidence: 1.00]
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


# Clause detect_cycle_inconsistency [Confidence: 1.00]
def join_or_check(u, v, d):
    ru, xu = find(u)
    rv, xv = find(v)
    if ru == rv:
        return xv - xu == d, ru
    if size[ru] < size[rv]:
        add = xv - d - xu
        parent[ru] = rv
        shift[ru] = add
        absorb(rv, ru, add)
        return True, rv
    add = d + xu - xv
    parent[rv] = ru
    shift[rv] = add
    absorb(ru, rv, add)
    return True, ru


# Clause enforce_terminal_ordering [Confidence: 1.00]
def terminal_ok(root):
    if has_s[root]:
        rs, xs = find(1)
        if lo[rs] != xs or clo[rs] != 1:
            return False
    if has_t[root]:
        rt, xt = find(n)
        if hi[rt] != xt or chi[rt] != 1:
            return False
    return True

bad = None
for idx, u, v, d in observed:
    ok, root = join_or_check(u, v, d)
    if not ok:
        bad = idx
        break
    root = find(u)[0]
    if not terminal_ok(root):
        bad = idx
        break


# Clause derive_efficiency_state [Confidence: 1.00]
answer = None
if bad is None:
    r1, x1 = find(1)
    rn, xn = find(n)
    if r1 == rn:
        answer = xn - x1


# Clause emit_certified_result [Confidence: 0.40]
if bad is not None:
    print("BAD", bad)
elif answer is None:
    print("UNKNOWN")
else:
    print(answer)


