import sys

MOD = 1000000007

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    adj = [[] for _ in range(n)]
    idx = 1

    for _ in range(n - 1):
        u = data[idx]
        v = data[idx + 1]
        c = data[idx + 2]
        idx += 3
        adj[u].append((v, c))
        adj[v].append((u, c))

    parent = [-2] * n
    parent[0] = -1
    parent_cost = [0] * n
    order = [0]

    for u in order:
        for v, c in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_cost[v] = c
                order.append(v)

    a = [0] * n
    b = [0] * n

    for u in reversed(order[1:]):
        if len(adj[u]) == 1:
            continue

        sum_a = 0
        sum_b = 0

        for v, c in adj[u]:
            if parent[v] == u:
                sum_a += a[v]
                sum_b += c + b[v]

        sum_a %= MOD
        sum_b %= MOD
        den = (len(adj[u]) - sum_a) % MOD
        inv = pow(den, MOD - 2, MOD)

        a[u] = inv
        b[u] = (parent_cost[u] + sum_b) * inv % MOD

    sum_a = 0
    sum_b = 0

    for v, c in adj[0]:
        sum_a += a[v]
        sum_b += c + b[v]

    sum_a %= MOD
    sum_b %= MOD
    ans = sum_b * pow((len(adj[0]) - sum_a) % MOD, MOD - 2, MOD) % MOD
    print(ans)

if __name__ == "__main__":
    main()
