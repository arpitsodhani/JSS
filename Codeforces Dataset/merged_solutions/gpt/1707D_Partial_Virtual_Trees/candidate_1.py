# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def batch_inv(a, mod):
    n = len(a) - 1
    inv = [0] * (n + 1)
    idx = []
    pref = [1]
    cur = 1
    for i in range(1, n + 1):
        if a[i]:
            idx.append(i)
            cur = cur * a[i] % mod
            pref.append(cur)
    if idx:
        cur = pow(cur, mod - 2, mod)
        for j in range(len(idx) - 1, -1, -1):
            inv[idx[j]] = cur * pref[j] % mod
            cur = cur * a[idx[j]] % mod
    return inv

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, mod = data[0], data[1]
    g = [[] for _ in range(n)]
    it = 2
    for _ in range(n - 1):
        u = data[it] - 1
        v = data[it + 1] - 1
        it += 2
        g[u].append(v)
        g[v].append(u)

    parent = [-1] * n
    parent[0] = -2
    order = [0]
    for v in order:
        for u in g[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)

    children = [[] for _ in range(n)]
    for v in range(1, n):
        children[parent[v]].append(v)

    lim = n - 1
    dp = [[0] * (lim + 1) for _ in range(n)]

    for v in reversed(order[1:]):
        ch = children[v]
        d = len(ch)
        zero = [0] * (lim + 1)
        prod = [1] * (lim + 1)

        for c in ch:
            arr = dp[c]
            for x in range(1, lim + 1):
                val = arr[x]
                if val:
                    prod[x] = prod[x] * val % mod
                else:
                    zero[x] += 1

        full = [0] * (lim + 1)
        for x in range(1, lim + 1):
            if zero[x] == 0:
                full[x] = prod[x]

        res = [0] * (lim + 1)
        pref = 0
        coef = (1 - d) % mod
        for m in range(1, lim + 1):
            pref = (pref + full[m]) % mod
            res[m] = coef * pref % mod

        for c in ch:
            arr = dp[c]
            inv = batch_inv(arr, mod)
            prefq = 0
            for m in range(1, lim + 1):
                val = arr[m]
                if zero[m] == 0:
                    q = full[m] * inv[m] % mod
                elif zero[m] == 1 and val == 0:
                    q = prod[m]
                else:
                    q = 0
                prefq = (prefq + q) % mod
                res[m] = (res[m] + val * prefq) % mod

        dp[v] = res

    f = [0] * (lim + 1)
    for m in range(1, lim + 1):
        val = 1
        for c in children[0]:
            val = val * dp[c][m] % mod
        f[m] = val

    fact = [1] * (lim + 1)
    for i in range(1, lim + 1):
        fact[i] = fact[i - 1] * i % mod
    invfact = [1] * (lim + 1)
    invfact[lim] = pow(fact[lim], mod - 2, mod)
    for i in range(lim, 0, -1):
        invfact[i - 1] = invfact[i] * i % mod

    ans = []
    for k in range(1, lim + 1):
        cur = 0
        fk = fact[k]
        for s in range(1, k + 1):
            comb = fk * invfact[s] % mod * invfact[k - s] % mod
            term = comb * f[s] % mod
            if (k - s) & 1:
                cur -= term
            else:
                cur += term
        ans.append(str(cur % mod))

    print(" ".join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
