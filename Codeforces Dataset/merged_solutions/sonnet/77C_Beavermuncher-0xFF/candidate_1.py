import sys


# --- clause: read_input :: () -> tuple[int, list[int], list[list[int]], int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    beavers = [0] + data[1:1 + n]
    adj = [[] for _ in range(n + 1)]
    pos = 1 + n
    for _ in range(n - 1):
        u = data[pos]
        v = data[pos + 1]
        pos += 2
        adj[u].append(v)
        adj[v].append(u)
    return n, beavers, adj, data[pos]


# --- clause: post_order :: (n: int, adj: list[list[int]], root: int) -> tuple[list[int], list[int]] ---
def post_order(n, adj, root):
    parent = [0] * (n + 1)
    parent[root] = root
    order = [root]
    head = 0
    while head < len(order):
        v = order[head]
        head += 1
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)
    return order, parent


# --- clause: eat_beavers :: (beavers: list[int], adj: list[list[int]], root: int, order: list[int], parent: list[int]) -> int ---
def eat_beavers(beavers, adj, root, order, parent):
    n = len(beavers) - 1
    best = [0] * (n + 1)
    rest = [0] * (n + 1)
    for i in range(len(order) - 1, -1, -1):
        v = order[i]
        cap = beavers[v] if v == root else beavers[v] - 1
        children = [u for u in adj[v] if u != parent[v]]
        children.sort(key=lambda u: best[u], reverse=True)
        taken = cap if cap < len(children) else len(children)
        total = 0
        pool = 0
        for index in range(len(children)):
            u = children[index]
            if index < taken:
                total += best[u] + 2
                pool += rest[u]
            else:
                pool += beavers[u]
        cap -= taken
        extra = pool if pool < cap else cap
        total += 2 * extra
        cap -= extra
        best[v] = total
        rest[v] = cap
    return best[root]


# --- clause: main :: () -> None ---
def main():
    n, beavers, adj, root = read_input()
    order, parent = post_order(n, adj, root)
    sys.stdout.write("%d\n" % eat_beavers(beavers, adj, root, order, parent))


if __name__ == "__main__":
    main()
