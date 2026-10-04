# CLAUSE: setup_environment
import sys
from math import gcd
from collections import deque

NEG = -10**30

def improve_cycle(state, modulus, dominant_value, item_cost, item_value):
    out = [NEG] * modulus
    step_count = gcd(modulus, item_cost)
    for first in range(step_count):
        orbit = []
        cur = first
        while cur not in orbit:
            orbit.append(cur)
            cur = (cur + item_cost) % modulus
        size = len(orbit)
        gain = [item_value - ((r + item_cost) // modulus) * dominant_value for r in orbit]
        pref = [0]
        for i in range(2 * size - 1):
            pref.append(pref[-1] + gain[i % size])
        keep = deque()
        for t in range(2 * size - 1):
            r = orbit[t % size]
            base = state[r]
            score = base - pref[t] if base > NEG // 2 else NEG
            while keep:
                old = keep[-1]
                old_base = state[orbit[old % size]]
                old_score = old_base - pref[old] if old_base > NEG // 2 else NEG
                if old_score >= score:
                    break
                keep.pop()
            keep.append(t)
            min_allowed = t - size + 1
            while keep and keep[0] < min_allowed:
                keep.popleft()
            if t + 1 >= size:
                chosen = keep[0]
                chosen_base = state[orbit[chosen % size]]
                if chosen_base > NEG // 2:
                    out[r] = chosen_base - pref[chosen] + pref[t]
    return out

def absorb(a, b):
    if b is None:
        return a
    if a is None:
        return b.copy()
    for i in range(len(a)):
        if b[i] > a[i]:
            a[i] = b[i]
    return a

def read_case():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(raw)
    n = next(it)
    m = next(it)
    c = [0]
    w = [0]
    for _ in range(n):
        c.append(next(it))
        w.append(next(it))
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        graph[next(it)].append(next(it))
    q = next(it)
    asks = [(next(it), next(it)) for _ in range(q)]
    return n, c, w, graph, asks

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
