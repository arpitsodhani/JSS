# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    k = int(input())

    bits = []
    i = 0
    while (1 << i) <= k:
        if k >> i & 1:
            bits.append(i)
        i += 1

    L = max(bits) if bits else 0
    n = 2 + 2 * (L + 1) + L
    g = [['N'] * n for _ in range(n)]

    def add(u, v):
        g[u][v] = g[v][u] = 'Y'

    s = 0
    t = 1

    def layer(i):
        return 2 + 2 * i, 3 + 2 * i

    for i in range(L):
        a, b = layer(i)
        c, d = layer(i + 1)
        add(a, c)
        add(a, d)
        add(b, c)
        add(b, d)

    a, b = layer(L)
    add(a, t)
    add(b, t)

    extra = 2 + 2 * (L + 1)
    for p in bits:
        cur = s
        for _ in range(L - p):
            add(cur, extra)
            cur = extra
            extra += 1
        a, b = layer(p)
        add(cur, a)
        add(cur, b)

    print(n)
    for row in g:
        print(''.join(row))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
