import sys
sys.setrecursionlimit(300000)

tokens = list(map(int, sys.stdin.buffer.read().split()))
k = 0
n = tokens[k]
m = tokens[k + 1]
k += 2
base = [0] + tokens[k:k + n]
k += n
g = [[] for _ in range(n + 1)]
for node in range(2, n + 1):
    g[tokens[k]].append(node)
    k += 1

# CLAUSE: flatten_subtree_intervals
enter = [0] * (n + 1)
leave = [0] * (n + 1)
seq = [0]
def dfs(v):
    enter[v] = len(seq)
    seq.append(v)
    for nxt in g[v]:
        dfs(nxt)
    leave[v] = len(seq) - 1
dfs(1)

# CLAUSE: sieve_prime_residues
is_comp = [False] * m
if m > 0:
    is_comp[0] = True
if m > 1:
    is_comp[1] = True
for x in range(2, m):
    if x * x >= m:
        break
    if not is_comp[x]:
        for y in range(x * x, m, x):
            is_comp[y] = True
want = 0
for x in range(m):
    if not is_comp[x]:
        want |= 1 << x

# CLAUSE: encode_residue_masks
cap = (1 << m) - 1
st = [0] * (4 * n + 10)
lz = [0] * (4 * n + 10)
def shifted(mask, delta):
    delta %= m
    if delta == 0:
        return mask
    return ((mask << delta) | (mask >> (m - delta))) & cap

def build_tree(id, l, r):
    if l == r:
        st[id] = 1 << (base[seq[l]] % m)
        return
    mid = (l + r) >> 1
    build_tree(id + id, l, mid)
    build_tree(id + id + 1, mid + 1, r)

# CLAUSE: apply_cyclic_shift_lazy
def cover(id, delta):
    delta %= m
    if delta != 0:
        st[id] = shifted(st[id], delta)
        lz[id] += delta
        if lz[id] >= m:
            lz[id] %= m

def relax(id):
    if lz[id]:
        cover(id + id, lz[id])
        cover(id + id + 1, lz[id])
        lz[id] = 0

# CLAUSE: merge_segment_masks
def join(id):
    st[id] = st[id + id] | st[id + id + 1]

build_tree(1, 1, n)
def range_add(id, l, r, left, right, delta):
    if left <= l and r <= right:
        cover(id, delta)
        return
    relax(id)
    mid = (l + r) >> 1
    if left <= mid:
        range_add(id + id, l, mid, left, right, delta)
    if right > mid:
        range_add(id + id + 1, mid + 1, r, left, right, delta)
    join(id)

def range_mask(id, l, r, left, right):
    if left <= l and r <= right:
        return st[id]
    relax(id)
    mid = (l + r) >> 1
    got = 0
    if left <= mid:
        got = range_mask(id + id, l, mid, left, right)
    if right > mid:
        got |= range_mask(id + id + 1, mid + 1, r, left, right)
    return got

q = tokens[k]
k += 1
lines = []
for _ in range(q):
    typ = tokens[k]
    v = tokens[k + 1]
    k += 2
    # CLAUSE: execute_subtree_updates
    if typ == 1:
        delta = tokens[k]
        k += 1
        range_add(1, 1, n, enter[v], leave[v], delta)
    # CLAUSE: answer_prime_presence_queries
    else:
        lines.append(str((range_mask(1, 1, n, enter[v], leave[v]) & want).bit_count()))
sys.stdout.write("\n".join(lines))
