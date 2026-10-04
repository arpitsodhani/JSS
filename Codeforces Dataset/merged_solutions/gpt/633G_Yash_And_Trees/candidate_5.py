import sys
sys.setrecursionlimit(300000)

inp = list(map(int, sys.stdin.buffer.read().split()))
idx = 0
n, m = inp[idx], inp[idx + 1]
idx += 2
nums = [0] + inp[idx:idx + n]
idx += n
adj = [[] for _ in range(n + 1)]
for v in range(2, n + 1):
    adj[inp[idx]].append(v)
    idx += 1

# CLAUSE: flatten_subtree_intervals
tin = [0] * (n + 1)
tout = [0] * (n + 1)
at = [0] * n
clock = 0
def tour(v):
    global clock
    tin[v] = clock
    at[clock] = v
    clock += 1
    for to in adj[v]:
        tour(to)
    tout[v] = clock
tour(1)

# CLAUSE: sieve_prime_residues
ok = [False, False] + [True] * max(0, m - 2)
for z in range(2, m):
    if z * z >= m:
        break
    if ok[z]:
        t = z * z
        while t < m:
            ok[t] = False
            t += z
pmask = 0
for z in range(m):
    if ok[z]:
        pmask |= 1 << z

# CLAUSE: encode_residue_masks
mask_limit = (1 << m) - 1
tree = [0] * (4 * n + 1)
lazy = [0] * (4 * n + 1)
def rotate_bits(mask, add):
    add %= m
    if add == 0:
        return mask
    return ((mask << add) & mask_limit) ^ (mask >> (m - add))

def construct(o, l, r):
    if r - l == 1:
        tree[o] = 1 << (nums[at[l]] % m)
        return
    mid = (l + r) >> 1
    construct(o << 1, l, mid)
    construct(o << 1 | 1, mid, r)

# CLAUSE: apply_cyclic_shift_lazy
def shift_node(o, add):
    add %= m
    if add:
        tree[o] = rotate_bits(tree[o], add)
        lazy[o] = (lazy[o] + add) % m

def propagate(o):
    add = lazy[o]
    if add:
        left = o << 1
        shift_node(left, add)
        shift_node(left | 1, add)
        lazy[o] = 0

# CLAUSE: merge_segment_masks
def recalc(o):
    left = o << 1
    tree[o] = tree[left] | tree[left | 1]

construct(1, 0, n)
def modify(o, l, r, ql, qr, add):
    if ql <= l and r <= qr:
        shift_node(o, add)
        return
    propagate(o)
    mid = (l + r) >> 1
    if ql < mid:
        modify(o << 1, l, mid, ql, qr, add)
    if qr > mid:
        modify(o << 1 | 1, mid, r, ql, qr, add)
    recalc(o)

def read(o, l, r, ql, qr):
    if ql <= l and r <= qr:
        return tree[o]
    propagate(o)
    mid = (l + r) >> 1
    mask = 0
    if ql < mid:
        mask = read(o << 1, l, mid, ql, qr)
    if qr > mid:
        mask |= read(o << 1 | 1, mid, r, ql, qr)
    return mask

q = inp[idx]
idx += 1
ans = []
for _ in range(q):
    typ = inp[idx]
    v = inp[idx + 1]
    idx += 2
    # CLAUSE: execute_subtree_updates
    if typ == 1:
        add = inp[idx]
        idx += 1
        modify(1, 0, n, tin[v], tout[v], add)
    # CLAUSE: answer_prime_presence_queries
    else:
        ans.append(str((read(1, 0, n, tin[v], tout[v]) & pmask).bit_count()))
sys.stdout.write("\n".join(ans))
