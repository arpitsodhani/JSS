import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    ends = [int(token) for token in data[2:2 + 2 * m]]
    return n, m, ends


# --- clause: build_adj :: (n: int, m: int, ends: list[int]) -> tuple[list[int], list[int]] ---
def build_adj(n, m, ends):
    degree = [0] * (n + 2)
    for value in ends:
        degree[value] += 1
    start = [0] * (n + 2)
    for v in range(1, n + 1):
        start[v + 1] = start[v] + degree[v]
    fill = start[:]
    adj = [0] * (2 * m)
    for i in range(m):
        u = ends[2 * i]
        v = ends[2 * i + 1]
        adj[fill[u]] = v
        fill[u] += 1
        adj[fill[v]] = u
        fill[v] += 1
    return start, adj


# --- clause: build_tree :: (n: int, start: list[int], adj: list[int]) -> list[str] ---
def build_tree(n, start, adj):
    hub = 1
    for v in range(2, n + 1):
        if start[v + 1] - start[v] > start[hub + 1] - start[hub]:
            hub = v
    seen = [False] * (n + 1)
    seen[hub] = True
    out = []
    frontier = []
    for idx in range(start[hub], start[hub + 1]):
        nxt = adj[idx]
        seen[nxt] = True
        out.append("%d %d" % (hub, nxt))
        frontier.append(nxt)
    head = 0
    while head < len(frontier):
        node = frontier[head]
        head += 1
        for idx in range(start[node], start[node + 1]):
            nxt = adj[idx]
            if not seen[nxt]:
                seen[nxt] = True
                out.append("%d %d" % (node, nxt))
                frontier.append(nxt)
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, ends = read_input()
    start, adj = build_adj(n, m, ends)
    sys.stdout.write("\n".join(build_tree(n, start, adj)) + "\n")


if __name__ == "__main__":
    main()
