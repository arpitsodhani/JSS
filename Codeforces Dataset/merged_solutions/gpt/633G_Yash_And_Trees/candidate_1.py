import sys
sys.setrecursionlimit(300000)

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
n = next(it)
m = next(it)
a = [0] + [next(it) for _ in range(n)]
children = [[] for _ in range(n + 1)]
for v in range(2, n + 1):
    children[next(it)].append(v)

# CLAUSE: flatten_subtree_intervals
tin = [0] * (n + 1)
tout = [0] * (n + 1)
order = [0] * n
timer = 0
def dfs(v):
    global timer
    tin[v] = timer
    order[timer] = v
    timer += 1
    for u in children[v]:
        dfs(u)
    tout[v] = timer - 1
dfs(1)

# CLAUSE: sieve_prime_residues
is_prime = [True] * m
if m > 0:
    is_prime[0] = False
if m > 1:
    is_prime[1] = False
p = 2
while p * p < m:
    if is_prime[p]:
        for j in range(p * p, m, p):
            is_prime[j] = False
    p += 1
prime_mask = 0
for r in range(m):
    if is_prime[r]:
        prime_mask |= 1 << r

# CLAUSE: encode_residue_masks
full_mask = (1 << m) - 1
seg = [0] * (4 * n + 5)
lazy = [0] * (4 * n + 5)
def rotate(mask, shift):
    shift %= m
    if shift == 0:
        return mask
    return ((mask << shift) | (mask >> (m - shift))) & full_mask

def build(idx, left, right):
    if left == right:
        seg[idx] = 1 << (a[order[left]] % m)
        return
    mid = (left + right) // 2
    build(idx * 2, left, mid)
    build(idx * 2 + 1, mid + 1, right)

# CLAUSE: apply_cyclic_shift_lazy
def apply(idx, shift):
    shift %= m
    if shift:
        seg[idx] = rotate(seg[idx], shift)
        lazy[idx] = (lazy[idx] + shift) % m

def push(idx):
    shift = lazy[idx]
    if shift:
        apply(idx * 2, shift)
        apply(idx * 2 + 1, shift)
        lazy[idx] = 0

# CLAUSE: merge_segment_masks
def pull(idx):
    seg[idx] = seg[idx * 2] | seg[idx * 2 + 1]

build(1, 0, n - 1)
def update(idx, left, right, ql, qr, shift):
    if ql <= left and right <= qr:
        apply(idx, shift)
        return
    push(idx)
    mid = (left + right) // 2
    if ql <= mid:
        update(idx * 2, left, mid, ql, qr, shift)
    if mid < qr:
        update(idx * 2 + 1, mid + 1, right, ql, qr, shift)
    pull(idx)

def query(idx, left, right, ql, qr):
    if ql <= left and right <= qr:
        return seg[idx]
    push(idx)
    mid = (left + right) // 2
    ans = 0
    if ql <= mid:
        ans |= query(idx * 2, left, mid, ql, qr)
    if mid < qr:
        ans |= query(idx * 2 + 1, mid + 1, right, ql, qr)
    return ans

q = next(it)
out = []
for _ in range(q):
    typ = next(it)
    v = next(it)
    # CLAUSE: execute_subtree_updates
    if typ == 1:
        x = next(it)
        update(1, 0, n - 1, tin[v], tout[v], x)
    # CLAUSE: answer_prime_presence_queries
    else:
        out.append(str((query(1, 0, n - 1, tin[v], tout[v]) & prime_mask).bit_count()))
sys.stdout.write("\n".join(out))
