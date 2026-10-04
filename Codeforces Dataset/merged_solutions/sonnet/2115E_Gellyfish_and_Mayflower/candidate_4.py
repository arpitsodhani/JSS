# CLAUSE: setup_environment
import sys
from math import gcd

NEG = -10**30

def max_join(x, y):
    if y is None:
        return x
    if x is None:
        return y[:]
    for i, yi in enumerate(y):
        if yi > x[i]:
            x[i] = yi
    return x

def residue_closure(a, mod, base, c, w):
    res = [NEG] * mod
    g = gcd(mod, c)
    for s in range(g):
        residues = []
        r = s
        while True:
            residues.append(r)
            r += c
            r %= mod
            if r == s:
                break
        ln = len(residues)
        delta = []
        for r in residues:
            delta.append(w - ((r + c) // mod) * base)
        pref = [0] * (2 * ln)
        for i in range(1, 2 * ln):
            pref[i] = pref[i - 1] + delta[(i - 1) % ln]
        queue = [0] * (2 * ln)
        head = 0
        tail = 0
        for i in range(2 * ln - 1):
            rr = residues[i % ln]
            av = a[rr]
            key = av - pref[i] if av > NEG // 2 else NEG
            while tail > head:
                j = queue[tail - 1]
                bv = a[residues[j % ln]]
                old = bv - pref[j] if bv > NEG // 2 else NEG
                if old >= key:
                    break
                tail -= 1
            queue[tail] = i
            tail += 1
            low = i - ln + 1
            while tail > head and queue[head] < low:
                head += 1
            if i >= ln - 1:
                j = queue[head]
                bv = a[residues[j % ln]]
                if bv > NEG // 2:
                    res[rr] = bv - pref[j] + pref[i]
    return res

def parse():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    n, m = nums[pos], nums[pos + 1]
    pos += 2
    c = [0] * (n + 1)
    w = [0] * (n + 1)
    for i in range(1, n + 1):
        c[i], w[i] = nums[pos], nums[pos + 1]
        pos += 2
    nxt = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = nums[pos], nums[pos + 1]
        pos += 2
        nxt[u].append(v)
    q = nums[pos]
    pos += 1
    queries = []
    for i in range(q):
        queries.append((nums[pos], nums[pos + 1]))
        pos += 2
    return n, c, w, nxt, queries

# CLAUSE: solve_logic
def small_phase(n, c, w, nxt, bound):
    dp = [[NEG] * (bound + 1) for _ in range(n + 1)]
    dp[1] = [0] * (bound + 1)
    for u in range(1, n + 1):
        row = dp[u]
        cu = c[u]
        wu = w[u]
        x = cu
        while x <= bound:
            y = row[x - cu] + wu
            if y > row[x]:
                row[x] = y
            x += 1
        for v in nxt[u]:
            other = dp[v]
            x = 0
            while x <= bound:
                if row[x] > other[x]:
                    other[x] = row[x]
                x += 1
    return dp

def build_for_pivot(n, c, w, nxt, pivot):
    mod = c[pivot]
    base = w[pivot]
    no = [None] * (n + 1)
    yes = [None] * (n + 1)
    if w[1] * mod <= base * c[1]:
        z = [NEG] * mod
        z[0] = 0
        if pivot == 1:
            yes[1] = z
        else:
            no[1] = z
    for u in range(1, n + 1):
        if w[u] * mod > base * c[u]:
            continue
        if u == pivot:
            yes[u] = max_join(yes[u], no[u])
            no[u] = None
        else:
            if no[u] is not None:
                no[u] = residue_closure(no[u], mod, base, c[u], w[u])
            if yes[u] is not None:
                yes[u] = residue_closure(yes[u], mod, base, c[u], w[u])
        for v in nxt[u]:
            if w[v] * mod <= base * c[v]:
                no[v] = max_join(no[v], no[u])
                yes[v] = max_join(yes[v], yes[u])
    ans_rows = [None] * (n + 1)
    for p in range(1, n + 1):
        arr = yes[p]
        if arr is None:
            ans_rows[p] = [NEG] * mod
        else:
            pref = [NEG] * mod
            best = NEG
            for i in range(mod):
                ai = arr[i]
                if ai > best:
                    best = ai
                pref[i] = best
            suff = [NEG] * (mod + 1)
            best = NEG
            for i in range(mod - 1, -1, -1):
                ai = arr[i]
                if ai > best:
                    best = ai
                suff[i] = best
            compact = [NEG] * mod
            for i in range(mod):
                value = pref[i]
                high = suff[i + 1]
                if high > NEG // 2:
                    high -= base
                    if high > value:
                        value = high
                compact[i] = value
            ans_rows[p] = compact
    return ans_rows

def main():
    n, c, w, nxt, queries = parse()
    threshold = max(c) ** 2
    max_small = 0
    need_large = False
    for p, r in queries:
        if r <= threshold:
            if r > max_small:
                max_small = r
        else:
            need_large = True
    small = small_phase(n, c, w, nxt, max_small) if max_small else None
    tables = [None] * (n + 1)
    if need_large:
        for pivot in range(1, n + 1):
            tables[pivot] = build_for_pivot(n, c, w, nxt, pivot)
    out = []
    for p, r in queries:
        if r <= threshold:
            out.append(str(small[p][r]))
        else:
            best = NEG
            for pivot in range(1, n + 1):
                mod = c[pivot]
                got = tables[pivot][p][r % mod]
                if got > NEG // 2:
                    total = (r // mod) * w[pivot] + got
                    if total > best:
                        best = total
            out.append(str(best))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
