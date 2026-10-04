# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def apply_item(arr, C, cu, wu, W):
    g = gcd(cu, C)
    for st in range(g):
        res = []
        x = st
        while True:
            res.append(x)
            x = (x + cu) % C
            if x == st:
                break
        L = len(res)
        vals = [arr[x] for x in res]
        edge = [wu - (x + cu) // C * W for x in res]
        pref = [0] * (2 * L + 1)
        for i in range(2 * L):
            pref[i + 1] = pref[i] + edge[i % L]
        qi = [0] * (2 * L + 2)
        qv = [0] * (2 * L + 2)
        head = 0
        tail = 0
        for i in range(1, L + 1):
            val = vals[i % L] - pref[i]
            while tail > head and qv[tail - 1] <= val:
                tail -= 1
            qi[tail] = i
            qv[tail] = val
            tail += 1
        for t in range(L):
            T = t + L
            lim = T - L + 1
            while qi[head] < lim:
                head += 1
            arr[res[t]] = pref[T] + qv[head]
            ni = t + L + 1
            if ni < 2 * L:
                val = vals[ni % L] - pref[ni]
                while tail > head and qv[tail - 1] <= val:
                    tail -= 1
                qi[tail] = ni
                qv[tail] = val
                tail += 1

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n = next(it)
    m = next(it)
    c = [0] * n
    w = [0] * n
    for i in range(n):
        c[i] = next(it)
        w[i] = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
    q = next(it)
    queries = []
    for i in range(q):
        p = next(it) - 1
        r = next(it)
        queries.append((p, r, i))
    maxc = max(c)
    B = maxc * maxc
    S = B + 1
    neg = -10 ** 30
    dp = [[neg] * S for _ in range(n)]
    dp[0][0] = 0
    for u in range(n):
        arr = dp[u]
        cu = c[u]
        wu = w[u]
        for x in range(cu, S):
            val = arr[x - cu] + wu
            if val > arr[x]:
                arr[x] = val
        for v in adj[u]:
            to = dp[v]
            for x in range(S):
                val = arr[x]
                if val > to[x]:
                    to[x] = val
    for u in range(n):
        arr = dp[u]
        best = neg
        for x in range(S):
            if arr[x] > best:
                best = arr[x]
            else:
                arr[x] = best
    ans = [0] * q
    large = []
    for p, r, idx in queries:
        if r <= B:
            ans[idx] = dp[p][r]
        else:
            large.append((p, r, idx))
    if large:
        for z in range(n):
            C = c[z]
            W = w[z]
            dp0 = [None] * n
            dp1 = [None] * n
            if z == 0:
                dp1[0] = [0] * C
            else:
                dp0[0] = [0] * C
            for u in range(n):
                if C * w[u] > W * c[u]:
                    continue
                if u == z:
                    a = dp0[u]
                    if a is not None:
                        b = dp1[u]
                        if b is None:
                            dp1[u] = a[:]
                        else:
                            for i in range(C):
                                if a[i] > b[i]:
                                    b[i] = a[i]
                else:
                    a = dp0[u]
                    if a is not None:
                        apply_item(a, C, c[u], w[u], W)
                    a = dp1[u]
                    if a is not None:
                        apply_item(a, C, c[u], w[u], W)
                for v in adj[u]:
                    if C * w[v] > W * c[v]:
                        continue
                    a = dp0[u]
                    if a is not None:
                        b = dp0[v]
                        if b is None:
                            dp0[v] = a[:]
                        else:
                            for i in range(C):
                                if a[i] > b[i]:
                                    b[i] = a[i]
                    a = dp1[u]
                    if a is not None:
                        b = dp1[v]
                        if b is None:
                            dp1[v] = a[:]
                        else:
                            for i in range(C):
                                if a[i] > b[i]:
                                    b[i] = a[i]
            for p, r, idx in large:
                arr = dp1[p]
                if arr is not None:
                    val = r // C * W + arr[r % C]
                    if val > ans[idx]:
                        ans[idx] = val
    sys.stdout.write('\n'.join(map(str, ans)))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
