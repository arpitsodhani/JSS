import sys


# --- clause: read_input :: () -> tuple[int, list[int], list[list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    values = fields[1:1 + n]
    adj = [[] for _ in range(n + 1)]
    cursor = 1 + n
    for _ in range(n - 1):
        u = fields[cursor]
        v = fields[cursor + 1]
        cursor += 2
        adj[u].append(v)
        adj[v].append(u)
    return n, values, adj


# --- clause: root_order :: (n: int, adj: list[list[int]]) -> tuple[list[int], list[int]] ---
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


# --- clause: subtree_stats :: (n: int, order: list[int], parent: list[int]) -> tuple[list[int], list[int]] ---
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


# --- clause: outer_signs :: (n: int, order: list[int], parent: list[int], adj: list[list[int]], signs: list[int]) -> list[int] ---
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


# --- clause: total_sum :: (n: int, values: list[int], order: list[int], parent: list[int], adj: list[list[int]], size: list[int], signs: list[int], outer: list[int]) -> int ---
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


# --- clause: main :: () -> None ---
def main():
    n, values, adj = read_input()
    order, parent = root_order(n, adj)
    size, signs = subtree_stats(n, order, parent)
    outer = outer_signs(n, order, parent, adj, signs)
    sys.stdout.write("%d\n" % total_sum(n, values, order, parent, adj, size, signs, outer))


if __name__ == "__main__":
    main()
