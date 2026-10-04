import sys
import heapq

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, m = data[0], data[1]
parent = list(range(n + 1))
rank = [0] * (n + 1)
dist = [0] * (n + 1)

mn = [0] * (n + 1)
mx = [0] * (n + 1)
has1 = [False] * (n + 1)
hasn = [False] * (n + 1)
v1 = [0] * (n + 1)
vn = [0] * (n + 1)
mx_non1 = [0] * (n + 1)
mn_nonn = [0] * (n + 1)
ver = [0] * (n + 1)

INF = 10**30

heap = []
for i in range(1, n + 1):
    has1[i] = (i == 1)
    hasn[i] = (i == n)
    mx_non1[i] = -INF if i == 1 else 0
    mn_nonn[i] = INF if i == n else 0
    heapq.heappush(heap, (0, i, 0))

def find(x):
    if parent[x] == x:
        return x, 0
    r, d = find(parent[x])
    dist[x] += d
    parent[x] = r
    return parent[x], dist[x]

def push_root(r):
    ver[r] += 1
    heapq.heappush(heap, (-(mx[r] - mn[r]), r, ver[r]))

def bad_now():
    r1, p1 = find(1)
    rn, pn = find(n)

    roots = {r1, rn}
    for r in roots:
        if has1[r] and mx_non1[r] >= v1[r]:
            return True
        if hasn[r] and mn_nonn[r] <= vn[r]:
            return True

    if r1 == rn:
        d = v1[r1] - vn[r1]
        if d <= 0:
            return True
        while heap:
            negw, r, z = heap[0]
            rr, _ = find(r)
            if rr != r or z != ver[r] or has1[r] or hasn[r]:
                heapq.heappop(heap)
            else:
                break
        if heap and -heap[0][0] >= d:
            return True

    return False

def unite(a, b, d):
    ra, pa = find(a)
    rb, pb = find(b)

    if ra == rb:
        return pa - pb == d

    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
        a, b = b, a
        pa, pb = pb, pa
        d = -d

    delta = pa - pb - d
    parent[rb] = ra
    dist[rb] = delta

    if rank[ra] == rank[rb]:
        rank[ra] += 1

    mn[ra] = min(mn[ra], mn[rb] + delta)
    mx[ra] = max(mx[ra], mx[rb] + delta)

    if has1[rb]:
        has1[ra] = True
        v1[ra] = v1[rb] + delta
    if hasn[rb]:
        hasn[ra] = True
        vn[ra] = vn[rb] + delta

    mx_non1[ra] = max(mx_non1[ra], mx_non1[rb] + delta)
    mn_nonn[ra] = min(mn_nonn[ra], mn_nonn[rb] + delta)

    push_root(ra)
    return True

idx = 2
for i in range(1, m + 1):
    f = data[idx]
    t = data[idx + 1]
    w = data[idx + 2]
    b = data[idx + 3]
    idx += 4

    if not unite(f, t, w * b) or bad_now():
        print("BAD", i)
        sys.exit()

r1, _ = find(1)
rn, _ = find(n)
if r1 == rn:
    print(v1[r1] - vn[r1])
else:
    print("UNKNOWN")
