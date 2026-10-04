import sys
sys.setrecursionlimit(300000)

vals = list(map(int, sys.stdin.buffer.read().split()))
pos = 0
n, m = vals[pos], vals[pos + 1]
pos += 2
a = [0] + vals[pos:pos + n]
pos += n
sons = [[] for _ in range(n + 1)]
for node in range(2, n + 1):
    parent = vals[pos]
    pos += 1
    sons[parent].append(node)

# CLAUSE: flatten_subtree_intervals
tin = [0] * (n + 1)
tout = [0] * (n + 1)
flat = [0] * (n + 1)
time = 0
stack = [(1, 0)]
while stack:
    v, state = stack.pop()
    if state == 0:
        time += 1
        tin[v] = time
        flat[time] = v
        stack.append((v, 1))
        for u in reversed(sons[v]):
            stack.append((u, 0))
    else:
        tout[v] = time

# CLAUSE: sieve_prime_residues
prime = [1] * m
if m >= 1:
    prime[0] = 0
if m >= 2:
    prime[1] = 0
for d in range(2, m):
    if d * d >= m:
        break
    if prime[d]:
        step_start = d * d
        prime[step_start:m:d] = [0] * (((m - 1 - step_start) // d) + 1)
prime_mask = 0
for i, ok in enumerate(prime):
    if ok:
        prime_mask += 1 << i

# CLAUSE: encode_residue_masks
limit = (1 << m) - 1
tree = [0] * (4 * n + 8)
add = [0] * (4 * n + 8)
def turn(mask, by):
    by %= m
    return mask if by == 0 else ((mask << by) & limit) | (mask >> (m - by))

def make(node, lo, hi):
    if lo == hi:
        tree[node] = 1 << (a[flat[lo]] % m)
    else:
        mid = (lo + hi) >> 1
        make(node << 1, lo, mid)
        make(node << 1 | 1, mid + 1, hi)

# CLAUSE: apply_cyclic_shift_lazy
def put(node, by):
    by %= m
    if by:
        tree[node] = turn(tree[node], by)
        add[node] = (add[node] + by) % m

def down(node):
    by = add[node]
    if by:
        put(node << 1, by)
        put(node << 1 | 1, by)
        add[node] = 0

# CLAUSE: merge_segment_masks
def unite(node):
    tree[node] = tree[node << 1] | tree[node << 1 | 1]

make(1, 1, n)
def change(node, lo, hi, left, right, by):
    if left <= lo and hi <= right:
        put(node, by)
        return
    down(node)
    mid = (lo + hi) >> 1
    if left <= mid:
        change(node << 1, lo, mid, left, right, by)
    if right > mid:
        change(node << 1 | 1, mid + 1, hi, left, right, by)
    unite(node)

def collect(node, lo, hi, left, right):
    if left <= lo and hi <= right:
        return tree[node]
    down(node)
    mid = (lo + hi) >> 1
    res = 0
    if left <= mid:
        res |= collect(node << 1, lo, mid, left, right)
    if right > mid:
        res |= collect(node << 1 | 1, mid + 1, hi, left, right)
    return res

q = vals[pos]
pos += 1
ans = []
for _ in range(q):
    t = vals[pos]
    v = vals[pos + 1]
    pos += 2
    # CLAUSE: execute_subtree_updates
    if t == 1:
        x = vals[pos]
        pos += 1
        change(1, 1, n, tin[v], tout[v], x)
    # CLAUSE: answer_prime_presence_queries
    else:
        ans.append(str((collect(1, 1, n, tin[v], tout[v]) & prime_mask).bit_count()))
print("\n".join(ans))
