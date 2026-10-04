# CLAUSE: setup_environment
import sys
from math import gcd

NEG = -10**30

class Scanner:
    def __init__(self):
        self.a = list(map(int, sys.stdin.buffer.read().split()))
        self.i = 0
    def next(self):
        x = self.a[self.i]
        self.i += 1
        return x

def combine(left, right):
    if right is None:
        return left
    if left is None:
        return right[:]
    for k, v in enumerate(right):
        if v > left[k]:
            left[k] = v
    return left

def relax_residues(source, mod, main_power, price, value):
    target = [NEG] * mod
    parts = gcd(mod, price)
    for start in range(parts):
        path = []
        now = start
        while True:
            path.append(now)
            now = (now + price) % mod
            if now == start:
                break
        length = len(path)
        gain = [value - ((r + price) // mod) * main_power for r in path]
        pref = [0] * (2 * length)
        for k in range(1, 2 * length):
            pref[k] = pref[k - 1] + gain[(k - 1) % length]
        stack = []
        first = 0
        for k in range(2 * length - 1):
            residue = path[k % length]
            raw = source[residue]
            here = raw - pref[k] if raw > NEG // 2 else NEG
            while len(stack) > first:
                t = stack[-1]
                raw_t = source[path[t % length]]
                there = raw_t - pref[t] if raw_t > NEG // 2 else NEG
                if there >= here:
                    break
                stack.pop()
            stack.append(k)
            while len(stack) > first and stack[first] < k - length + 1:
                first += 1
            if k >= length - 1:
                t = stack[first]
                raw_t = source[path[t % length]]
                if raw_t > NEG // 2:
                    target[residue] = raw_t - pref[t] + pref[k]
    return target

def input_data():
    sc = Scanner()
    n = sc.next()
    m = sc.next()
    cost = [0] * (n + 1)
    power = [0] * (n + 1)
    for i in range(1, n + 1):
        cost[i] = sc.next()
        power[i] = sc.next()
    graph = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for _ in range(m):
        u = sc.next()
        v = sc.next()
        graph[u].append(v)
        indeg[v] += 1
    q = sc.next()
    qs = []
    for _ in range(q):
        qs.append((sc.next(), sc.next()))
    return n, cost, power, graph, qs

# CLAUSE: solve_logic
def finite_dp(n, cost, power, graph, limit):
    table = [[NEG] * (limit + 1) for _ in range(n + 1)]
    table[1] = [0] * (limit + 1)
    for u in range(1, n + 1):
        arr = table[u]
        c = cost[u]
        w = power[u]
        for money in range(c, limit + 1):
            nv = arr[money - c] + w
            if nv > arr[money]:
                arr[money] = nv
        for v in graph[u]:
            dst = table[v]
            for money, val in enumerate(arr):
                if val > dst[money]:
                    dst[money] = val
    return table

def residue_offsets(arr, mod, power):
    if arr is None:
        return [NEG] * mod
    pref = [NEG] * mod
    best = NEG
    for i in range(mod):
        if arr[i] > best:
            best = arr[i]
        pref[i] = best
    suff = [NEG] * (mod + 1)
    best = NEG
    for i in range(mod - 1, -1, -1):
        if arr[i] > best:
            best = arr[i]
        suff[i] = best
    out = [NEG] * mod
    for i in range(mod):
        a = pref[i]
        b = suff[i + 1]
        if b > NEG // 2 and b - power > a:
            a = b - power
        out[i] = a
    return out

def infinite_dp(n, cost, power, graph):
    result = [None] * (n + 1)
    for key in range(1, n + 1):
        mod = cost[key]
        value = power[key]
        pre = [None] * (n + 1)
        post = [None] * (n + 1)
        if power[1] * mod <= value * cost[1]:
            zero = [NEG] * mod
            zero[0] = 0
            if key == 1:
                post[1] = zero
            else:
                pre[1] = zero
        for u in range(1, n + 1):
            if power[u] * mod > value * cost[u]:
                continue
            if u == key:
                post[u] = combine(post[u], pre[u])
                pre[u] = None
            else:
                if pre[u] is not None:
                    pre[u] = relax_residues(pre[u], mod, value, cost[u], power[u])
                if post[u] is not None:
                    post[u] = relax_residues(post[u], mod, value, cost[u], power[u])
            pu = pre[u]
            qu = post[u]
            for v in graph[u]:
                if power[v] * mod <= value * cost[v]:
                    pre[v] = combine(pre[v], pu)
                    post[v] = combine(post[v], qu)
        rows = [None] * (n + 1)
        for p in range(1, n + 1):
            rows[p] = residue_offsets(post[p], mod, value)
        result[key] = rows
    return result

def main():
    n, cost, power, graph, queries = input_data()
    small_border = max(cost) * max(cost)
    small_limit = 0
    large_exists = False
    for p, r in queries:
        if r <= small_border:
            small_limit = max(small_limit, r)
        else:
            large_exists = True
    small = finite_dp(n, cost, power, graph, small_limit) if small_limit > 0 else None
    large = infinite_dp(n, cost, power, graph) if large_exists else None
    answer = []
    for p, r in queries:
        if r <= small_border:
            answer.append(str(small[p][r]))
        else:
            best = NEG
            for key in range(1, n + 1):
                mod = cost[key]
                shift = large[key][p][r % mod]
                if shift > NEG // 2:
                    cand = (r // mod) * power[key] + shift
                    if cand > best:
                        best = cand
            answer.append(str(best))
    sys.stdout.write("\n".join(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
