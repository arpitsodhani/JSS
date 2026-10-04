# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return

    n = int(raw[0])
    graph = [[] for _ in range(n)]
    it = iter(raw[1:])
    for a, b, c in zip(it, it, it):
        u = int(a)
        v = int(b)
        w = int(c) % MOD
        graph[u].append((v, w))
        graph[v].append((u, w))

    parent = [n] * n
    back_cost = [0] * n
    children = [[] for _ in range(n)]
    parent[0] = 0
    stack = [0]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)
        for nxt, cost in graph[node]:
            if parent[nxt] == n:
                parent[nxt] = node
                back_cost[nxt] = cost
                children[node].append((nxt, cost))
                stack.append(nxt)

    linear = [0] * n
    fixed = [0] * n

    for node in order[::-1]:
        if node == 0 or not children[node]:
            continue
        ca = sum(linear[ch] for ch, _ in children[node]) % MOD
        cb = (back_cost[node] + sum((cost + fixed[ch]) % MOD for ch, cost in children[node])) % MOD
        inv = pow((len(graph[node]) - ca) % MOD, MOD - 2, MOD)
        linear[node] = inv
        fixed[node] = cb * inv % MOD

    root_a = sum(linear[ch] for ch, _ in children[0]) % MOD
    root_b = sum((cost + fixed[ch]) % MOD for ch, cost in children[0]) % MOD
    ans = root_b * pow((len(graph[0]) - root_a) % MOD, MOD - 2, MOD) % MOD
    print(ans)

# CLAUSE: finish_program
main()
