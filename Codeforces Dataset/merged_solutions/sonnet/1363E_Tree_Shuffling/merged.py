import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    cost = [0] * (n + 1)
    start = [0] * (n + 1)
    goal = [0] * (n + 1)
    pos = 1
    for v in range(1, n + 1):
        cost[v] = data[pos]
        start[v] = data[pos + 1]
        goal[v] = data[pos + 2]
        pos += 3
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = data[pos]
        v = data[pos + 1]
        pos += 2
        adj[u].append(v)
        adj[v].append(u)
    return n, cost, start, goal, adj

# Clause walk_order [Confidence: 1.00]
def walk_order(n, adj):
    parent = [0] * (n + 1)
    parent[1] = 1
    seen = [False] * (n + 1)
    seen[1] = True
    order = [1]
    front = 0
    while front < len(order):
        v = order[front]
        front += 1
        for u in adj[v]:
            if not seen[u]:
                seen[u] = True
                parent[u] = v
                order.append(u)
    return order, parent

# Clause shuffle_cost [Confidence: 1.00]
def shuffle_cost(n, cost, start, goal, order, parent):
    for i in range(1, len(order)):
        v = order[i]
        if cost[parent[v]] < cost[v]:
            cost[v] = cost[parent[v]]
    ones = [0] * (n + 1)
    zeros = [0] * (n + 1)
    total = 0
    for v in range(1, n + 1):
        if start[v] != goal[v]:
            if start[v]:
                ones[v] = 1
            else:
                zeros[v] = 1
    for i in range(len(order) - 1, -1, -1):
        v = order[i]
        pairs = ones[v] if ones[v] < zeros[v] else zeros[v]
        total += 2 * pairs * cost[v]
        ones[v] -= pairs
        zeros[v] -= pairs
        if v != 1:
            p = parent[v]
            ones[p] += ones[v]
            zeros[p] += zeros[v]
    if ones[1] or zeros[1]:
        return -1
    return total

# Clause main [Confidence: 1.00]
def main():
    n, cost, start, goal, adj = read_input()
    order, parent = walk_order(n, adj)
    sys.stdout.write("%d\n" % shuffle_cost(n, cost, start, goal, order, parent))


if __name__ == "__main__":
    main()

