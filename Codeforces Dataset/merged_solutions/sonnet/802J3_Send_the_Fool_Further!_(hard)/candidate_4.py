# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def main():
    data = tuple(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    neighbors = [[] for _ in range(n)]
    weights = [[] for _ in range(n)]

    pos = 1
    while pos < len(data):
        u = data[pos]
        v = data[pos + 1]
        w = data[pos + 2] % MOD
        pos += 3
        neighbors[u].append(v)
        weights[u].append(w)
        neighbors[v].append(u)
        weights[v].append(w)

    parent = [-1] * n
    parent[0] = 0
    parent_cost = [0] * n
    order = [0]
    head = 0

    while head < len(order):
        v = order[head]
        head += 1
        for i, to in enumerate(neighbors[v]):
            if to == parent[v]:
                continue
            parent[to] = v
            parent_cost[to] = weights[v][i]
            order.append(to)

    c = [0] * n
    k = [0] * n

    for v in reversed(order):
        if v == 0 or len(neighbors[v]) == 1:
            continue
        sc = 0
        sk = parent_cost[v]
        for i, to in enumerate(neighbors[v]):
            if parent[to] == v:
                sc += c[to]
                sk += weights[v][i] + k[to]
        sc %= MOD
        sk %= MOD
        den = (len(neighbors[v]) - sc) % MOD
        inv_den = pow(den, MOD - 2, MOD)
        c[v] = inv_den
        k[v] = sk * inv_den % MOD

    sc = 0
    sk = 0
    for i, to in enumerate(neighbors[0]):
        sc += c[to]
        sk += weights[0][i] + k[to]
    sc %= MOD
    sk %= MOD

    sys.stdout.write(str(sk * pow((len(neighbors[0]) - sc) % MOD, MOD - 2, MOD) % MOD))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
