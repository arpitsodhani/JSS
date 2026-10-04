import sys

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

n = next(it)
m = next(it)

a = [0] + [next(it) % m for _ in range(n)]

g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u = next(it)
    v = next(it)
    g[u].append(v)
    g[v].append(u)

tin = [0] * (n + 1)
tout = [0] * (n + 1)
order = []
timer = 0
stack = [(1, 0, 0)]

while stack:
    v, p, state = stack.pop()
    if state == 0:
        tin[v] = timer
        order.append(v)
        timer += 1
        stack.append((v, p, 1))
        for to in reversed(g[v]):
            if to != p:
                stack.append((to, v, 0))
    else:
        tout[v] = timer

full = (1 << m) - 1

def rot(mask, s):
    s %= m
    if s == 0:
        return mask
    return ((mask << s) | (mask >> (m - s))) & full

prime = [True] * m
if m > 0:
    prime[0] = False
if m > 1:
    prime[1] = False
for i in range(2, m):
    if prime[i]:
        step = i
        start = i * i
        if start < m:
            for j in range(start, m, step):
                prime[j] = False

prime_mask = 0
for i in range(m):
    if prime[i]:
        prime_mask |= 1 << i

size = 4 * n + 5
seg = [0] * size
lazy = [0] * size
base = [1 << a[v] for v in order]

sys.setrecursionlimit(300000)

def build(idx, l, r):
    if l == r:
        seg[idx] = base[l]
        return
    mid = (l + r) >> 1
    build(idx << 1, l, mid)
    build(idx << 1 | 1, mid + 1, r)
    seg[idx] = seg[idx << 1] | seg[idx << 1 | 1]

def apply(idx, x):
    x %= m
    if x:
        seg[idx] = rot(seg[idx], x)
        lazy[idx] = (lazy[idx] + x) % m

def push(idx):
    z = lazy[idx]
    if z:
        apply(idx << 1, z)
        apply(idx << 1 | 1, z)
        lazy[idx] = 0

def update(idx, l, r, ql, qr, x):
    if ql <= l and r <= qr:
        apply(idx, x)
        return
    push(idx)
    mid = (l + r) >> 1
    if ql <= mid:
        update(idx << 1, l, mid, ql, qr, x)
    if qr > mid:
        update(idx << 1 | 1, mid + 1, r, ql, qr, x)
    seg[idx] = seg[idx << 1] | seg[idx << 1 | 1]

def query(idx, l, r, ql, qr):
    if ql <= l and r <= qr:
        return seg[idx]
    push(idx)
    mid = (l + r) >> 1
    res = 0
    if ql <= mid:
        res |= query(idx << 1, l, mid, ql, qr)
    if qr > mid:
        res |= query(idx << 1 | 1, mid + 1, r, ql, qr)
    return res

build(1, 0, n - 1)

q = next(it)
out = []

for _ in range(q):
    typ = next(it)
    v = next(it)
    l = tin[v]
    r = tout[v] - 1
    if typ == 1:
        x = next(it) % m
        update(1, 0, n - 1, l, r, x)
    else:
        out.append(str((query(1, 0, n - 1, l, r) & prime_mask).bit_count()))

sys.stdout.write("\n".join(out))
