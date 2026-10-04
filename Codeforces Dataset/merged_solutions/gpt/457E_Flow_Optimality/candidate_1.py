import sys

# CLAUSE: parse_known_flow_edges
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()
n, m = data[0], data[1]
edges = []
p = 2
for i in range(1, m + 1):
    f, t, w, b = data[p], data[p + 1], data[p + 2], data[p + 3]
    p += 4
    edges.append((i, f, t, w, b))

# CLAUSE: assign_edge_potentials
observed = [(idx, u, v, w * b) for idx, u, v, w, b in edges]

# CLAUSE: merge_weighted_components
parent = list(range(n + 1))
size = [1] * (n + 1)
shift = [0] * (n + 1)
lo = [0] * (n + 1)
hi = [0] * (n + 1)
clo = [1] * (n + 1)
chi = [1] * (n + 1)
has_s = [False] * (n + 1)
has_t = [False] * (n + 1)
has_s[1] = True
has_t[n] = True

def find(x):
    r = x
    total = 0
    while parent[r] != r:
        total += shift[r]
        r = parent[r]
    cur = x
    acc = 0
    while parent[cur] != cur:
        nxt = parent[cur]
        old = shift[cur]
        parent[cur] = r
        shift[cur] = total - acc
        acc += old
        cur = nxt
    return r, total

def absorb(a, b, add):
    b_lo = lo[b] + add
    b_hi = hi[b] + add
    if b_lo < lo[a]:
        lo[a], clo[a] = b_lo, clo[b]
    elif b_lo == lo[a]:
        clo[a] += clo[b]
    if b_hi > hi[a]:
        hi[a], chi[a] = b_hi, chi[b]
    elif b_hi == hi[a]:
        chi[a] += chi[b]
    has_s[a] = has_s[a] or has_s[b]
    has_t[a] = has_t[a] or has_t[b]
    size[a] += size[b]

# CLAUSE: detect_cycle_inconsistency
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

# CLAUSE: enforce_terminal_ordering
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

# CLAUSE: derive_efficiency_state
answer = None
if bad is None:
    r1, x1 = find(1)
    rn, xn = find(n)
    if r1 == rn:
        answer = xn - x1

# CLAUSE: emit_certified_result
if bad is not None:
    print("BAD", bad)
elif answer is None:
    print("UNKNOWN")
else:
    print(answer)
