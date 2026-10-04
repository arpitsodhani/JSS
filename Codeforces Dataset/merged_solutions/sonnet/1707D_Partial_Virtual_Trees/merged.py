# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 1.00]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, p = data[0], data[1]
    g = [[] for _ in range(n + 1)]
    at = 2
    for _ in range(n - 1):
        a = data[at]
        b = data[at + 1]
        at += 2
        g[a].append(b)
        g[b].append(a)

    m = n - 1
    if m == 0:
        print()
        return

    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    order = [1]
    parent[1] = -1
    for v in order:
        pv = parent[v]
        for u in g[v]:
            if u != pv:
                parent[u] = v
                children[v].append(u)
                order.append(u)

    dp = [None] * (n + 1)
    leaf = [0] + [i % p for i in range(1, m + 1)]
    root_values = None

    for v in order[::-1]:
        ch = children[v]
        if v == 1:
            root_values = [1] * (m + 1)
            for c in ch:
                arr = dp[c]
                for t in range(m + 1):
                    root_values[t] = root_values[t] * arr[t] % p
            break

        if not ch:
            dp[v] = leaf
        elif len(ch) == 1:
            arr = dp[ch[0]]
            dp[v] = [0] + [t * arr[t] % p for t in range(1, m + 1)]
        else:
            arrs = [dp[c] for c in ch]
            d = len(arrs)
            pref = [1] * (d + 1)
            extra = [0] * d
            res = [0] * (m + 1)
            total_products = 0
            coef = (1 - d) % p
            for t in range(1, m + 1):
                for i in range(d):
                    pref[i + 1] = pref[i] * arrs[i][t] % p
                total_products = (total_products + pref[d]) % p
                suffix = 1
                subtotal = 0
                for i in range(d - 1, -1, -1):
                    value = arrs[i][t]
                    without = pref[i] * suffix % p
                    extra[i] = (extra[i] + without) % p
                    subtotal = (subtotal + value * extra[i]) % p
                    suffix = suffix * value % p
                res[t] = (subtotal + coef * total_products) % p
            dp[v] = res

    choose = [0] * (m + 1)
    choose[0] = 1
    out = []
    for k in range(1, m + 1):
        j = k
        while j:
            choose[j] = (choose[j] + choose[j - 1]) % p
            j -= 1
        cur = 0
        sign = 1 if k % 2 == 0 else -1
        for s in range(k + 1):
            cur += sign * choose[s] * root_values[s]
            sign = -sign
        out.append(str(cur % p))
    sys.stdout.write(" ".join(out))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


