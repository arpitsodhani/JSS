# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    n = values[0]
    graph = [[] for _ in range(n)]
    p = 1
    for _ in range(n - 1):
        u = values[p]
        v = values[p + 1]
        w = values[p + 2] % MOD
        p += 3
        graph[u].append((v, w))
        graph[v].append((u, w))

    parent = [-1] * n
    edge_to_parent = [0] * n
    parent[0] = 0
    order = [0]

    for node in order:
        for nxt, cost in graph[node]:
            if nxt != parent[node]:
                parent[nxt] = node
                edge_to_parent[nxt] = cost
                order.append(nxt)

    coef = [0] * n
    const = [0] * n

    for node in order[:0:-1]:
        if len(graph[node]) == 1:
            continue
        a = 0
        b = edge_to_parent[node]
        for nxt, cost in graph[node]:
            if nxt == parent[node]:
                continue
            a += coef[nxt]
            b += cost + const[nxt]
        a %= MOD
        b %= MOD
        inv = pow((len(graph[node]) - a) % MOD, MOD - 2, MOD)
        coef[node] = inv
        const[node] = b * inv % MOD

    a = 0
    b = 0
    for nxt, cost in graph[0]:
        a += coef[nxt]
        b += cost + const[nxt]
    a %= MOD
    b %= MOD
    print(b * pow((len(graph[0]) - a) % MOD, MOD - 2, MOD) % MOD)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
