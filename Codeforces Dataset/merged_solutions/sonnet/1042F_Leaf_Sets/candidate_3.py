import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    ends = [int(token) for token in data[2:2 * n]]
    return n, k, ends


# --- clause: build_adj :: (n: int, ends: list[int]) -> tuple[list[int], list[int]] ---
def build_adj(n, ends):
    degree = [0] * (n + 2)
    for value in ends:
        degree[value] += 1
    start = [0] * (n + 2)
    for v in range(1, n + 1):
        start[v + 1] = start[v] + degree[v]
    fill = start[:]
    adj = [0] * len(ends)
    for i in range(0, len(ends), 2):
        u = ends[i]
        v = ends[i + 1]
        adj[fill[u]] = v
        fill[u] += 1
        adj[fill[v]] = u
        fill[v] += 1
    return start, adj


# --- clause: count_sets :: (n: int, k: int, start: list[int], adj: list[int]) -> int ---
def count_sets(n, k, start, adj):
    root = 1
    v = 1
    while v <= n:
        if start[v + 1] - start[v] >= 2:
            root = v
            break
        v += 1
    parent = [0] * (n + 1)
    order = []
    seen = [False] * (n + 1)
    seen[root] = True
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        for idx in range(start[node], start[node + 1]):
            nxt = adj[idx]
            if not seen[nxt]:
                seen[nxt] = True
                parent[nxt] = node
                stack.append(nxt)
    reach = [0] * (n + 1)
    pending = [[] for _ in range(n + 1)]
    total = 0
    for i in range(len(order) - 1, -1, -1):
        node = order[i]
        values = pending[node]
        if values:
            values.sort()
            while len(values) >= 2 and values[-1] + values[-2] > k:
                total += 1
                values.pop()
            reach[node] = values[-1]
        else:
            reach[node] = 0
        pending[node] = None
        up = parent[node]
        if up:
            pending[up].append(reach[node] + 1)
    return total + 1


# --- clause: main :: () -> None ---
def main():
    n, k, ends = read_input()
    start, adj = build_adj(n, ends)
    print(count_sets(n, k, start, adj))


if __name__ == "__main__":
    main()
