# Clause setup_environment [Confidence: 0.60]
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


# Clause solve_logic [Confidence: 0.80]
def bounded_answers(n, c, w, graph, asks, cap):
    if cap == 0:
        return None
    dp = [[NEG] * (cap + 1) for _ in range(n + 1)]
    dp[1] = [0] * (cap + 1)
    for u in range(1, n + 1):
        row = dp[u]
        cu = c[u]
        wu = w[u]
        for coins in range(cu, cap + 1):
            candidate = row[coins - cu] + wu
            if candidate > row[coins]:
                row[coins] = candidate
        for v in graph[u]:
            target = dp[v]
            for coins in range(cap + 1):
                value = row[coins]
                if value > target[coins]:
                    target[coins] = value
    return dp

def asymptotic_tables(n, c, w, graph):
    all_tables = [None] * (n + 1)
    for pivot in range(1, n + 1):
        mod = c[pivot]
        slope = w[pivot]
        unseen = [None] * (n + 1)
        seen = [None] * (n + 1)
        if w[1] * mod <= slope * c[1]:
            initial = [NEG] * mod
            initial[0] = 0
            if pivot == 1:
                seen[1] = initial
            else:
                unseen[1] = initial
        for u in range(1, n + 1):
            if w[u] * mod > slope * c[u]:
                continue
            if u == pivot:
                seen[u] = absorb(seen[u], unseen[u])
                unseen[u] = None
            else:
                if unseen[u] is not None:
                    unseen[u] = improve_cycle(unseen[u], mod, slope, c[u], w[u])
                if seen[u] is not None:
                    seen[u] = improve_cycle(seen[u], mod, slope, c[u], w[u])
            next_unseen = unseen[u]
            next_seen = seen[u]
            for v in graph[u]:
                if w[v] * mod <= slope * c[v]:
                    unseen[v] = absorb(unseen[v], next_unseen)
                    seen[v] = absorb(seen[v], next_seen)
        table = [None] * (n + 1)
        for p in range(1, n + 1):
            arr = seen[p]
            if arr is None:
                table[p] = [NEG] * mod
                continue
            left = [NEG] * mod
            best = NEG
            for i, x in enumerate(arr):
                if x > best:
                    best = x
                left[i] = best
            right = [NEG] * (mod + 1)
            best = NEG
            for i in range(mod - 1, -1, -1):
                if arr[i] > best:
                    best = arr[i]
                right[i] = best
            row = [NEG] * mod
            for rem in range(mod):
                value = left[rem]
                if right[rem + 1] > NEG // 2 and right[rem + 1] - slope > value:
                    value = right[rem + 1] - slope
                row[rem] = value
            table[p] = row
        all_tables[pivot] = table
    return all_tables

def main():
    n, c, w, graph, asks = read_case()
    border = max(c) * max(c)
    cap = 0
    need_big = False
    for _, r in asks:
        if r <= border:
            cap = max(cap, r)
        else:
            need_big = True
    small = bounded_answers(n, c, w, graph, asks, cap)
    big = asymptotic_tables(n, c, w, graph) if need_big else None
    lines = []
    for p, r in asks:
        if r <= border:
            lines.append(str(small[p][r]))
            continue
        best = NEG
        for pivot in range(1, n + 1):
            mod = c[pivot]
            extra = big[pivot][p][r % mod]
            if extra > NEG // 2:
                value = (r // mod) * w[pivot] + extra
                if value > best:
                    best = value
        lines.append(str(best))
    sys.stdout.write("\n".join(lines))


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


