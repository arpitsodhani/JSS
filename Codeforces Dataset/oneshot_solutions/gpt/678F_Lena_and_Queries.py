import sys

input = sys.stdin.readline
INF_NEG = -10**30

n = int(input())
queries = [None] * (n + 1)
added = {}
intervals = []
xs_query = []

for i in range(1, n + 1):
    parts = list(map(int, input().split()))
    queries[i] = parts
    if parts[0] == 1:
        added[i] = (parts[1], parts[2], i)
    elif parts[0] == 2:
        _, idx = parts
        x, y, l = added.pop(idx)
        intervals.append((l, i - 1, (x, y)))
    else:
        xs_query.append(parts[1])

for x, y, l in added.values():
    intervals.append((l, n, (x, y)))

xs = sorted(set(xs_query))
m = len(xs)

seg = [[] for _ in range(4 * n + 5)]

def add_interval(v, tl, tr, l, r, line):
    if l > r:
        return
    if l == tl and r == tr:
        seg[v].append(line)
        return
    tm = (tl + tr) // 2
    add_interval(v * 2, tl, tm, l, min(r, tm), line)
    add_interval(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, line)

for l, r, line in intervals:
    if l <= r:
        add_interval(1, 1, n, l, r, line)

tree = [None] * (4 * max(1, m) + 5)
history = []

def val(line, x):
    return line[0] * x + line[1]

def set_node(pos, line):
    history.append((pos, tree[pos]))
    tree[pos] = line

def lichao_add(line, v=1, l=0, r=None):
    if r is None:
        r = m - 1
    if tree[v] is None:
        set_node(v, line)
        return

    mid = (l + r) // 2
    cur = tree[v]

    if val(line, xs[mid]) > val(cur, xs[mid]):
        set_node(v, line)
        line = cur
        cur = tree[v]

    if l == r:
        return

    if val(line, xs[l]) > val(cur, xs[l]):
        lichao_add(line, v * 2, l, mid)
    elif val(line, xs[r]) > val(cur, xs[r]):
        lichao_add(line, v * 2 + 1, mid + 1, r)

def lichao_query(idx):
    x = xs[idx]
    res = INF_NEG
    v, l, r = 1, 0, m - 1
    while True:
        if tree[v] is not None:
            res = max(res, val(tree[v], x))
        if l == r:
            break
        mid = (l + r) // 2
        if idx <= mid:
            v = v * 2
            r = mid
        else:
            v = v * 2 + 1
            l = mid + 1
    return res

x_to_idx = {x: i for i, x in enumerate(xs)}
ans = []

def rollback(size):
    while len(history) > size:
        pos, old = history.pop()
        tree[pos] = old

def dfs(v, tl, tr):
    snap = len(history)
    if m:
        for line in seg[v]:
            lichao_add(line)

    if tl == tr:
        q = queries[tl]
        if q[0] == 3:
            res = lichao_query(x_to_idx[q[1]]) if m else INF_NEG
            ans.append("EMPTY SET" if res == INF_NEG else str(res))
    else:
        tm = (tl + tr) // 2
        dfs(v * 2, tl, tm)
        dfs(v * 2 + 1, tm + 1, tr)

    rollback(snap)

dfs(1, 1, n)
sys.stdout.write("\n".join(ans))
