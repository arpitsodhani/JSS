# CLAUSE: setup_environment
import sys

BIG = 10 ** 30
BAD = -10 ** 18

# CLAUSE: solve_logic
def better_put(table, key, value):
    old = table.get(key)
    if old is None or value > old:
        table[key] = value

def compact(table):
    if not table:
        return {}
    arr = sorted((d, r, s) for (d, r), s in table.items())
    needs = []
    last = None
    for _, r, _ in arr:
        if r != last:
            needs.append(r)
            last = r
    needs = sorted(set(needs))
    rank = {v: i + 1 for i, v in enumerate(needs)}
    bit = [BAD] * (len(needs) + 1)
    kept = {}
    for d, r, s in sorted(arr, key=lambda p: (p[0], p[1], -p[2])):
        i = rank[r]
        best = BAD
        j = i
        while j > 0:
            if bit[j] > best:
                best = bit[j]
            j -= j & -j
        if best >= s:
            continue
        kept[(d, r)] = s
        j = i
        while j <= len(needs):
            if s > bit[j]:
                bit[j] = s
            j += j & -j
    return kept

def lifted_layers(layers, dist, x):
    res = []
    for table in layers:
        nt = {}
        for (near, wait), score in table.items():
            if near == BIG:
                nd = BIG
            else:
                val = near + dist
                nd = val if val <= x else BIG
            if wait == -1:
                nw = -1
            else:
                nw = wait + dist
                if nw > x:
                    continue
            better_put(nt, (nd, nw), score)
        res.append(nt)
    return res

def combine(left, right, cap, x):
    out = [{} for _ in range(cap + 1)]
    for i in range(len(left)):
        a = left[i]
        if not a:
            continue
        upto = min(len(right) - 1, cap - i)
        for j in range(upto + 1):
            b = right[j]
            if not b:
                continue
            target = out[i + j]
            for (d1, q1), s1 in a.items():
                for (d2, q2), s2 in b.items():
                    closest = d1 if d1 < d2 else d2
                    ql = -1
                    if q1 != -1 and (d2 == BIG or q1 + d2 > x):
                        ql = q1
                    qr = -1
                    if q2 != -1 and (d1 == BIG or q2 + d1 > x):
                        qr = q2
                    need = ql if ql > qr else qr
                    better_put(target, (closest, need), s1 + s2)
    return [compact(t) for t in out]

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return
    n, x = nums[0], nums[1]
    colors = [0] + nums[2:2 + n]
    black = sum(colors)
    graph = [[] for _ in range(n + 1)]
    p = 2 + n
    for _ in range(n - 1):
        u, v, w = nums[p], nums[p + 1], nums[p + 2]
        p += 3
        graph[u].append((v, w))
        graph[v].append((u, w))

    parent = [-2] * (n + 1)
    parent[1] = 0
    stack = [1]
    order = []
    while stack:
        v = stack.pop()
        order.append(v)
        for to, _ in graph[v]:
            if parent[to] == -2:
                parent[to] = v
                stack.append(to)

    dp = [None] * (n + 1)
    sub = [1] * (n + 1)
    for v in order[::-1]:
        base = [{(BIG, 0): 0}]
        if black:
            base.append({(0, -1): colors[v]})
        cur = base
        used = 1
        for to, w in graph[v]:
            if parent[to] != v:
                continue
            shifted = lifted_layers(dp[to], w, x)
            used += sub[to]
            cur = combine(cur, shifted, min(black, used), x)
        sub[v] = used
        dp[v] = cur

    answer = BAD
    root = dp[1]
    if black < len(root):
        for state, val in root[black].items():
            if state[1] == -1 and val > answer:
                answer = val
    print(-1 if answer == BAD else black - answer)

# CLAUSE: finish_program
main()
