import sys


# --- clause: read_input :: () -> tuple[int, list[int], list[int], list[int], list[list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    cost = [0] * (n + 1)
    start = [0] * (n + 1)
    goal = [0] * (n + 1)
    offset = 1
    for v in range(1, n + 1):
        cost[v] = fields[offset]
        start[v] = fields[offset + 1]
        goal[v] = fields[offset + 2]
        offset += 3
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = fields[offset]
        v = fields[offset + 1]
        offset += 2
        adj[u].append(v)
        adj[v].append(u)
    return n, cost, start, goal, adj


# --- clause: walk_order :: (n: int, adj: list[list[int]]) -> tuple[list[int], list[int]] ---
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


# --- clause: shuffle_cost :: (n: int, cost: list[int], start: list[int], goal: list[int], order: list[int], parent: list[int]) -> int ---
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


# --- clause: main :: () -> None ---
def main():
    n, cost, start, goal, adj = read_input()
    order, parent = walk_order(n, adj)
    sys.stdout.write("%d\n" % shuffle_cost(n, cost, start, goal, order, parent))


if __name__ == "__main__":
    main()
