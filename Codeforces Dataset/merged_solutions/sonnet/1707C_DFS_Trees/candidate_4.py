import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    edges = []
    for i in range(m):
        edges.append((numbers[2 + 2 * i], numbers[3 + 2 * i]))
    return n, edges


# --- clause: split_edges :: (n: int, edges: list[tuple[int, int]]) -> tuple[list[list[int]], list[tuple[int, int]]] ---
def split_edges(n, edges):
    parent = list(range(n + 1))
    adj = [[] for _ in range(n + 1)]
    extra = []
    for u, v in edges:
        a = u
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        b = v
        while parent[b] != b:
            parent[b] = parent[parent[b]]
            b = parent[b]
        if a == b:
            extra.append((u, v))
        else:
            parent[a] = b
            adj[u].append(v)
            adj[v].append(u)
    return adj, extra


# --- clause: root_tree :: (n: int, adj: list[list[int]]) -> tuple[list[int], list[int], list[int]] ---
def root_tree(n, adj):
    up = [0 for _ in range(n + 1)]
    depth = [0 for _ in range(n + 1)]
    known = [False] * (n + 1)
    up[1] = 1
    known[1] = True
    order = [1]
    head = 0
    while head < len(order):
        v = order[head]
        head += 1
        for u in adj[v]:
            if not known[u]:
                known[u] = True
                up[u] = v
                depth[u] = depth[v] + 1
                order.append(u)
    return up, depth, order


# --- clause: lifting_table :: (n: int, up: list[int], order: list[int]) -> list[list[int]] ---
def lifting_table(n, up, order):
    levels = 1
    while (1 << levels) <= n:
        levels += 1
    table = [up]
    for step in range(1, levels):
        below = table[step - 1]
        row = [0 for _ in range(n + 1)]
        for v in range(1, n + 1):
            row[v] = below[below[v]]
        table.append(row)
    return table


# --- clause: mark_roots :: (n: int, extra: list[tuple[int, int]], up: list[int], depth: list[int], table: list[list[int]]) -> list[int] ---
def mark_roots(n, extra, up, depth, table):
    diff = [0 for _ in range(n + 1)]
    for u, v in extra:
        top = u
        low = v
        if depth[top] > depth[low]:
            top, low = low, top
        walker = low
        gap = depth[low] - depth[top]
        for step in range(len(table)):
            if (gap >> step) & 1:
                walker = table[step][walker]
        if walker == top:
            child = low
            gap = depth[low] - depth[top] - 1
            for step in range(len(table)):
                if (gap >> step) & 1:
                    child = table[step][child]
            diff[1] += 1
            diff[child] -= 1
            diff[low] += 1
        else:
            diff[u] += 1
            diff[v] += 1
    return diff


# --- clause: collect_answer :: (n: int, diff: list[int], up: list[int], order: list[int], needed: int) -> str ---
def collect_answer(n, diff, up, order, needed):
    total = [0 for _ in range(n + 1)]
    total[1] = diff[1]
    for i in range(1, len(order)):
        v = order[i]
        total[v] = total[up[v]] + diff[v]
    letters = []
    for v in range(1, n + 1):
        letters.append("1" if total[v] == needed else "0")
    return "".join(letters)


# --- clause: main :: () -> None ---
def main():
    n, edges = read_input()
    adj, extra = split_edges(n, edges)
    up, depth, order = root_tree(n, adj)
    table = lifting_table(n, up, order)
    diff = mark_roots(n, extra, up, depth, table)
    sys.stdout.write(collect_answer(n, diff, up, order, len(extra)) + "\n")


if __name__ == "__main__":
    main()
