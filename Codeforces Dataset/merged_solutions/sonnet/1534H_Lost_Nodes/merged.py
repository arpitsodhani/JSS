# Clause setup_environment [Confidence: 0.80]
import sys

BAD = -10 ** 18


# Clause solve_logic [Confidence: 1.00]
def value_all(values):
    values.sort(reverse=True)
    ans = len(values)
    for pos, val in enumerate(values):
        cur = val + pos
        if cur > ans:
            ans = cur
    return ans

def value_one(group):
    if not group:
        return 0
    base = value_all([x for x, y in group])
    ans = base
    size = len(group)
    for skip in range(size):
        remaining = []
        for i in range(size):
            if i != skip:
                remaining.append(group[i][0])
        cand = value_all(remaining)
        if group[skip][1] > cand:
            cand = group[skip][1]
        if cand < ans:
            ans = cand
    return ans

def transitions(group):
    size = len(group)
    if size == 1:
        return [0]
    order = sorted(range(size), key=lambda i: (-group[i][0], i))
    rank = [0] * size
    c = [0] * size
    e = [0] * size
    for pos, old in enumerate(order):
        rank[old] = pos
        c[pos] = group[old][0]
        e[pos] = group[old][1]
    a0 = [c[i] + i for i in range(size)]
    a1 = [c[i] + i - 1 for i in range(size)]
    a2 = [c[i] + i - 2 for i in range(size)]
    p0 = [0] * size
    p1 = [0] * size
    p2 = [0] * size
    s1 = [0] * size
    s2 = [0] * size
    for i in range(size):
        p0[i] = a0[i] if i == 0 else max(p0[i - 1], a0[i])
        p1[i] = a1[i] if i == 0 else max(p1[i - 1], a1[i])
        p2[i] = a2[i] if i == 0 else max(p2[i - 1], a2[i])
    for i in range(size - 1, -1, -1):
        s1[i] = a1[i] if i == size - 1 else max(s1[i + 1], a1[i])
        s2[i] = a2[i] if i == size - 1 else max(s2[i + 1], a2[i])
    def without_one(x):
        ans = size - 1
        if x:
            ans = max(ans, p0[x - 1])
        if x + 1 < size:
            ans = max(ans, s1[x + 1])
        return ans
    def without_two(x, y):
        if x > y:
            x, y = y, x
        ans = size - 2
        if x:
            ans = max(ans, p0[x - 1])
        if x + 1 < y:
            ans = max(ans, p1[y - 1] if x + 1 == 0 else max(a1[x + 1:y]))
        if y + 1 < size:
            ans = max(ans, s2[y + 1])
        return ans
    by_rank = [0] * size
    for x in range(size):
        best = without_one(x)
        for y in range(size):
            if x == y:
                continue
            got = without_two(x, y)
            if e[y] > got:
                got = e[y]
            if got < best:
                best = got
        by_rank[x] = best
    return [by_rank[rank[i]] for i in range(size)]

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    adj = [[] for _ in range(n)]
    k = 1
    for _ in range(n - 1):
        u = data[k] - 1
        v = data[k + 1] - 1
        k += 2
        adj[u].append(v)
        adj[v].append(u)
    if n == 1:
        print(0)
        return
    parent = [-1] * n
    order = [0]
    for v in order:
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)
    cmsg = {}
    dmsg = {}
    for v in order[:0:-1]:
        group = []
        pv = parent[v]
        for u in adj[v]:
            if u != pv:
                group.append((cmsg[(u, v)], dmsg[(u, v)]))
        val = value_one(group)
        dmsg[(v, pv)] = val
        cmsg[(v, pv)] = val + 1
    for v in order:
        group = []
        ok = True
        for u in adj[v]:
            key = (u, v)
            if key not in cmsg:
                ok = False
                break
            group.append((cmsg[key], dmsg[key]))
        if ok:
            out = transitions(group)
            for i, u in enumerate(adj[v]):
                dmsg[(v, u)] = out[i]
                cmsg[(v, u)] = out[i] + 1
    ans = 0
    for v in range(n):
        arr = [cmsg[(u, v)] for u in adj[v]]
        arr.sort(reverse=True)
        cur = len(arr)
        if arr:
            cur = max(cur, len(arr) - 1 + arr[0])
        for i in range(1, len(arr)):
            cur = max(cur, i - 1 + arr[0] + arr[i])
        ans = max(ans, cur)
    print(ans)


# Clause finish_program [Confidence: 0.40]
main()


