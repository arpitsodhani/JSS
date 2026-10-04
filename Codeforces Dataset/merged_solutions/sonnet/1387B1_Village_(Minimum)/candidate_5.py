import sys


# --- clause: read_input :: () -> tuple[int, list[list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a = raw[1 + 2 * i]
        b = raw[2 + 2 * i]
        adj[a].append(b)
        adj[b].append(a)
    return n, adj


# --- clause: greedy_matching :: (n: int, adj: list[list[int]]) -> tuple[list[int], list[int], list[int]] ---
def greedy_matching(n, adj):
    parent = [0] * (n + 1)
    parent[1] = 1
    sorted_items = [1]
    met = [False] * (n + 1)
    met[1] = True
    head = 0
    while head < len(sorted_items):
        v = sorted_items[head]
        head += 1
        for u in adj[v]:
            if not met[u]:
                met[u] = True
                parent[u] = v
                sorted_items.append(u)
    mate = [0] * (n + 1)
    for i in range(len(sorted_items) - 1, 0, -1):
        v = sorted_items[i]
        p = parent[v]
        if mate[v] == 0 and mate[p] == 0:
            mate[v] = p
            mate[p] = v
    return sorted_items, parent, mate


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
        for i in range(0, len(cycle)):
            moves[cycle[i]] = cycle[(i + 1) % len(cycle)]
    return 2 * (n - pairs), moves


# --- clause: main :: () -> None ---
def main():
    n, adj = read_input()
    sorted_items, parent, mate = greedy_matching(n, adj)
    total, moves = build_moves(n, adj, mate)
    sys.stdout.write("%d\n%s\n" % (total, " ".join(map(str, moves[1:]))))


if __name__ == "__main__":
    main()
