import sys


# --- clause: read_input :: () -> tuple[int, list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a = data[1 + 2 * i]
        b = data[2 + 2 * i]
        adj[a].append(b)
        adj[b].append(a)
    return n, adj


# --- clause: greedy_matching :: (n: int, adj: list[list[int]]) -> tuple[list[int], list[int], list[int]] ---
def greedy_matching(n, adj):
    parent = [0] * (n + 1)
    parent[1] = 1
    order = [1]
    seen = [False] * (n + 1)
    seen[1] = True
    head = 0
    while head < len(order):
        v = order[head]
        head += 1
        for u in adj[v]:
            if not seen[u]:
                seen[u] = True
                parent[u] = v
                order.append(u)
    mate = [0] * (n + 1)
    for i in range(len(order) - 1, 0, -1):
        v = order[i]
        p = parent[v]
        if mate[v] == 0 and mate[p] == 0:
            mate[v] = p
            mate[p] = v
    return order, parent, mate


# --- clause: build_moves :: (n: int, adj: list[list[int]], mate: list[int]) -> tuple[int, list[int]] ---
def build_moves(n, adj, mate):
    pairs = 0
    for v in range(1, n + 1):
        if mate[v] > v:
            pairs += 1
    extras = {}
    for v in range(1, n + 1):
        if mate[v]:
            continue
        host = 0
        for u in adj[v]:
            if mate[u]:
                host = u
                break
        if host not in extras:
            extras[host] = []
        extras[host].append(v)
    moves = [0] * (n + 1)
    for p in range(1, n + 1):
        q = mate[p]
        if q == 0 or q < p:
            continue
        cycle = [p, q] + extras.get(q, []) + extras.get(p, [])
        for i in range(len(cycle)):
            moves[cycle[i]] = cycle[(i + 1) % len(cycle)]
    return 2 * (n - pairs), moves


# --- clause: main :: () -> None ---
def main():
    n, adj = read_input()
    order, parent, mate = greedy_matching(n, adj)
    total, moves = build_moves(n, adj, mate)
    sys.stdout.write("%d\n%s\n" % (total, " ".join(map(str, moves[1:]))))


if __name__ == "__main__":
    main()
