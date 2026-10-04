# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if len(nums) < 2:
        return
    n = nums[0]
    p = nums[1]
    kmax = n - 1
    if kmax < 1:
        print()
        return

    head = [-1] * (n + 1)
    to = [0] * (2 * kmax)
    nxt = [0] * (2 * kmax)
    e = 0
    idx = 2
    for _ in range(kmax):
        a = nums[idx]
        b = nums[idx + 1]
        idx += 2
        to[e] = b
        nxt[e] = head[a]
        head[a] = e
        e += 1
        to[e] = a
        nxt[e] = head[b]
        head[b] = e
        e += 1

    parent = [0] * (n + 1)
    parent[1] = -1
    order = [1]
    ptr = 0
    while ptr < len(order):
        v = order[ptr]
        ptr += 1
        edge = head[v]
        while edge != -1:
            u = to[edge]
            if u != parent[v]:
                parent[u] = v
                order.append(u)
            edge = nxt[edge]

    table = [None] * (n + 1)
    base = [0] + [i % p for i in range(1, kmax + 1)]
    root = None

    for v in reversed(order):
        arrays = []
        edge = head[v]
        while edge != -1:
            u = to[edge]
            if parent[u] == v:
                arrays.append(table[u])
            edge = nxt[edge]

        if v == 1:
            root = [1] * (kmax + 1)
            for arr in arrays:
                t = 0
                while t <= kmax:
                    root[t] = root[t] * arr[t] % p
                    t += 1
        elif len(arrays) == 0:
            table[v] = base
        elif len(arrays) == 1:
            arr = arrays[0]
            made = [0] * (kmax + 1)
            t = 1
            while t <= kmax:
                made[t] = t * arr[t] % p
                t += 1
            table[v] = made
        else:
            d = len(arrays)
            made = [0] * (kmax + 1)
            prefix = [1] * (d + 1)
            stored = [0] * d
            seen_products = 0
            coefficient = (1 - d) % p
            for t in range(1, kmax + 1):
                for i, arr in enumerate(arrays):
                    prefix[i + 1] = prefix[i] * arr[t] % p
                seen_products = (seen_products + prefix[d]) % p
                suffix = 1
                now = 0
                i = d - 1
                while i >= 0:
                    x = arrays[i][t]
                    part = prefix[i] * suffix % p
                    stored[i] = (stored[i] + part) % p
                    now = (now + x * stored[i]) % p
                    suffix = suffix * x % p
                    i -= 1
                made[t] = (now + coefficient * seen_products) % p
            table[v] = made

    binom = [0] * (kmax + 1)
    binom[0] = 1
    pieces = []
    for k in range(1, kmax + 1):
        for j in range(k, 0, -1):
            binom[j] = (binom[j] + binom[j - 1]) % p
        value = 0
        for s in range(k + 1):
            add = binom[s] * root[s]
            if (k - s) % 2:
                value -= add
            else:
                value += add
        pieces.append(str(value % p))
    sys.stdout.write(" ".join(pieces))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
