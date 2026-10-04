import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    values = data[1:1 + n]
    adj = [[] for _ in range(n + 1)]
    pos = 1 + n
    for _ in range(n - 1):
        u = data[pos]
        v = data[pos + 1]
        pos += 2
        adj[u].append(v)
        adj[v].append(u)
    return n, values, adj

# Clause root_order [Confidence: 1.00]
def root_order(n, adj):
    parent = [0] * (n + 1)
    parent[1] = 1
    order = [1]
    marked = [False] * (n + 1)
    marked[1] = True
    head = 0
    while head < len(order):
        v = order[head]
        head += 1
        for u in adj[v]:
            if not marked[u]:
                marked[u] = True
                parent[u] = v
                order.append(u)
    return order, parent

# Clause subtree_stats [Confidence: 1.00]
def subtree_stats(n, order, parent):
    size = [1] * (n + 1)
    signs = [1] * (n + 1)
    size[0] = 0
    signs[0] = 0
    for i in range(len(order) - 1, 0, -1):
        v = order[i]
        p = parent[v]
        size[p] += size[v]
        signs[p] -= signs[v]
    return size, signs

# Clause outer_signs [Confidence: 1.00]
def outer_signs(n, order, parent, adj, signs):
    outer = [0] * (n + 1)
    for v in order:
        below = 0
        for u in adj[v]:
            if u != parent[v]:
                below += signs[u]
        for u in adj[v]:
            if u != parent[v]:
                outer[u] = 1 - (below - signs[u]) - outer[v]
    return outer

# Clause total_sum [Confidence: 1.00]
def total_sum(n, values, order, parent, adj, size, signs, outer):
    mod = 1000000007
    total = 0
    for v in range(1, n + 1):
        weight = n
        for u in adj[v]:
            if u == parent[v]:
                weight -= size[v] * outer[v]
            else:
                weight -= (n - size[u]) * signs[u]
        total = (total + values[v - 1] * weight) % mod
    return total % mod

# Clause main [Confidence: 1.00]
def main():
    n, values, adj = read_input()
    order, parent = root_order(n, adj)
    size, signs = subtree_stats(n, order, parent)
    outer = outer_signs(n, order, parent, adj, signs)
    sys.stdout.write("%d\n" % total_sum(n, values, order, parent, adj, size, signs, outer))


if __name__ == "__main__":
    main()

