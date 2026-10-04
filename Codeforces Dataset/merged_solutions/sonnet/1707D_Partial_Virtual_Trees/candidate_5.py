# CLAUSE: setup_environment
import sys
sys.setrecursionlimit(1000000)

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    p = data[1]
    top = n - 1
    if top == 0:
        print()
        return

    adj = [[] for _ in range(n + 1)]
    q = 2
    for _ in range(top):
        x = data[q]
        y = data[q + 1]
        q += 2
        adj[x].append(y)
        adj[y].append(x)

    leaf = [0] + [i % p for i in range(1, top + 1)]

    def merge(items):
        size = len(items)
        if size == 0:
            return leaf
        if size == 1:
            arr = items[0]
            out = [0] * (top + 1)
            for t in range(1, top + 1):
                out[t] = t * arr[t] % p
            return out

        pref = [1] * (size + 1)
        saved = [0] * size
        out = [0] * (top + 1)
        running = 0
        fix = (1 - size) % p
        for t in range(1, top + 1):
            i = 0
            for arr in items:
                pref[i + 1] = pref[i] * arr[t] % p
                i += 1
            running = (running + pref[size]) % p
            suffix = 1
            total = 0
            for i in range(size - 1, -1, -1):
                current = items[i][t]
                without = pref[i] * suffix % p
                saved[i] = (saved[i] + without) % p
                total = (total + current * saved[i]) % p
                suffix = suffix * current % p
            out[t] = (total + fix * running) % p
        return out

    def dfs(v, par):
        parts = []
        for u in adj[v]:
            if u != par:
                parts.append(dfs(u, v))
        if v == 1:
            product = [1] * (top + 1)
            for arr in parts:
                for t, val in enumerate(arr):
                    product[t] = product[t] * val % p
            return product
        return merge(parts)

    root_values = dfs(1, 0)
    comb = [0] * (top + 1)
    comb[0] = 1
    ans = []

    for k in range(1, top + 1):
        j = k
        while j > 0:
            comb[j] = (comb[j] + comb[j - 1]) % p
            j -= 1
        res = 0
        parity = k & 1
        for s in range(k + 1):
            term = comb[s] * root_values[s]
            if (s & 1) == parity:
                res += term
            else:
                res -= term
        ans.append(str(res % p))

    print(" ".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
