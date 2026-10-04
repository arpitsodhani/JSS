# CLAUSE: setup_environment
import sys

BAD = -10 ** 18

# CLAUSE: solve_logic
def arrange(v):
    v = sorted(v, reverse=True)
    ans = len(v)
    for i in range(len(v)):
        ans = max(ans, v[i] + i)
    return ans

def shrink(a):
    if len(a) == 0:
        return 0
    ans = arrange([x[0] for x in a])
    for i in range(len(a)):
        b = [a[j][0] for j in range(len(a)) if j != i]
        ans = min(ans, max(arrange(b), a[i][1]))
    return ans

def reroot(a):
    m = len(a)
    if m == 1:
        return [0]
    p = sorted(range(m), key=lambda i: (-a[i][0], i))
    inv = [0] * m
    x = [0] * m
    y = [0] * m
    for i in range(m):
        inv[p[i]] = i
        x[i] = a[p[i]][0]
        y[i] = a[p[i]][1]
    f0 = [x[i] + i for i in range(m)]
    f1 = [x[i] + i - 1 for i in range(m)]
    f2 = [x[i] + i - 2 for i in range(m)]
    pref0 = f0[:]
    suff1 = f1[:]
    suff2 = f2[:]
    for i in range(1, m):
        pref0[i] = max(pref0[i], pref0[i - 1])
    for i in range(m - 2, -1, -1):
        suff1[i] = max(suff1[i], suff1[i + 1])
        suff2[i] = max(suff2[i], suff2[i + 1])
    def rem1(i):
        z = m - 1
        if i > 0:
            z = max(z, pref0[i - 1])
        if i + 1 < m:
            z = max(z, suff1[i + 1])
        return z
    def rem2(i, j):
        if i > j:
            i, j = j, i
        z = m - 2
        if i > 0:
            z = max(z, pref0[i - 1])
        t = BAD
        for k in range(i + 1, j):
            if f1[k] > t:
                t = f1[k]
        z = max(z, t)
        if j + 1 < m:
            z = max(z, suff2[j + 1])
        return z
    z = [0] * m
    for i in range(m):
        best = rem1(i)
        for j in range(m):
            if i != j:
                cur = max(rem2(i, j), y[j])
                if cur < best:
                    best = cur
        z[i] = best
    ans = [0] * m
    for i in range(m):
        ans[i] = z[inv[i]]
    return ans

def main():
    raw = sys.stdin.buffer.read()
    if not raw:
        return
    nums = list(map(int, raw.split()))
    n = nums[0]
    g = [[] for _ in range(n)]
    e = 1
    for _ in range(n - 1):
        u = nums[e] - 1
        v = nums[e + 1] - 1
        e += 2
        g[u].append(v)
        g[v].append(u)
    if n < 2:
        print(0)
        return
    parent = [-1] * n
    q = [0]
    for v in q:
        for u in g[v]:
            if u != parent[v]:
                parent[u] = v
                q.append(u)
    c = {}
    d = {}
    for v in reversed(q):
        if v == 0:
            continue
        children = []
        for u in g[v]:
            if parent[u] == v:
                children.append((c[(u, v)], d[(u, v)]))
        res = shrink(children)
        d[(v, parent[v])] = res
        c[(v, parent[v])] = res + 1
    for v in q:
        items = []
        for u in g[v]:
            if (u, v) not in c:
                break
            items.append((c[(u, v)], d[(u, v)]))
        else:
            out = reroot(items)
            for i in range(len(g[v])):
                u = g[v][i]
                d[(v, u)] = out[i]
                c[(v, u)] = out[i] + 1
    ans = 0
    for v in range(n):
        h = []
        for u in g[v]:
            h.append(c[(u, v)])
        h.sort(reverse=True)
        cur = len(h)
        if h:
            cur = max(cur, len(h) - 1 + h[0])
        for i, val in enumerate(h[1:], 1):
            cur = max(cur, h[0] + val + i - 1)
        ans = max(ans, cur)
    sys.stdout.write("%d\n" % ans)

# CLAUSE: finish_program
main()
