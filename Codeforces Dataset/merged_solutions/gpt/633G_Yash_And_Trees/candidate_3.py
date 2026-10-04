import sys
sys.setrecursionlimit(300000)

arr = list(map(int, sys.stdin.buffer.read().split()))
ptr = 0
n = arr[ptr]
m = arr[ptr + 1]
ptr += 2
value = [0] + arr[ptr:ptr + n]
ptr += n
child = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    child[arr[ptr]].append(i)
    ptr += 1

# CLAUSE: flatten_subtree_intervals
tin = [0] * (n + 1)
tout = [0] * (n + 1)
euler = []
def visit(root):
    stack = [(root, 0)]
    while stack:
        v, idx = stack[-1]
        if idx == 0:
            tin[v] = len(euler)
            euler.append(v)
        if idx == len(child[v]):
            tout[v] = len(euler) - 1
            stack.pop()
        else:
            u = child[v][idx]
            stack[-1] = (v, idx + 1)
            stack.append((u, 0))
visit(1)

# CLAUSE: sieve_prime_residues
bad = [False] * m
if m:
    bad[0] = True
if m > 1:
    bad[1] = True
i = 2
while i < m:
    if not bad[i]:
        j = i * i
        while j < m:
            bad[j] = True
            j += i
    i += 1
prime_mask = 0
for r in range(2, m):
    if not bad[r]:
        prime_mask |= 1 << r

# CLAUSE: encode_residue_masks
all_bits = (1 << m) - 1
seg = [0] * (4 * n + 4)
tag = [0] * (4 * n + 4)
def rotate_left(bits, shift):
    shift %= m
    if not shift:
        return bits
    high = bits >> (m - shift)
    low = (bits << shift) & all_bits
    return low | high

def init(p, l, r):
    if l + 1 == r:
        seg[p] = 1 << (value[euler[l]] % m)
        return
    mid = (l + r) // 2
    init(p * 2, l, mid)
    init(p * 2 + 1, mid, r)

# CLAUSE: apply_cyclic_shift_lazy
def mark(p, shift):
    shift %= m
    if shift:
        seg[p] = rotate_left(seg[p], shift)
        tag[p] = (tag[p] + shift) % m

def spread(p):
    shift = tag[p]
    if shift:
        mark(p * 2, shift)
        mark(p * 2 + 1, shift)
        tag[p] = 0

# CLAUSE: merge_segment_masks
def merge(p):
    seg[p] = seg[p * 2] | seg[p * 2 + 1]

init(1, 0, n)
def add_range(p, l, r, ql, qr, shift):
    if ql <= l and r <= qr:
        mark(p, shift)
        return
    spread(p)
    mid = (l + r) // 2
    if ql < mid:
        add_range(p * 2, l, mid, ql, qr, shift)
    if mid < qr:
        add_range(p * 2 + 1, mid, r, ql, qr, shift)
    merge(p)

def get_range(p, l, r, ql, qr):
    if ql <= l and r <= qr:
        return seg[p]
    spread(p)
    mid = (l + r) // 2
    ret = 0
    if ql < mid:
        ret |= get_range(p * 2, l, mid, ql, qr)
    if mid < qr:
        ret |= get_range(p * 2 + 1, mid, r, ql, qr)
    return ret

q = arr[ptr]
ptr += 1
res = []
for _ in range(q):
    typ = arr[ptr]
    v = arr[ptr + 1]
    ptr += 2
    # CLAUSE: execute_subtree_updates
    if typ == 1:
        x = arr[ptr]
        ptr += 1
        add_range(1, 0, n, tin[v], tout[v] + 1, x)
    # CLAUSE: answer_prime_presence_queries
    else:
        res.append(str((get_range(1, 0, n, tin[v], tout[v] + 1) & prime_mask).bit_count()))
sys.stdout.write("\n".join(res))
