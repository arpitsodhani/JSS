import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[tuple[int, int, int]]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        edges = []
        for _ in range(m):
            edges.append((data[pos], data[pos + 1], data[pos + 2]))
            pos += 3
        cases.append((n, m, edges))
    return cases


# --- clause: topological_rank :: (n: int, edges: list[tuple[int, int, int]]) -> list[int] | None ---
def topological_rank(n, edges):
    adj = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for kind, x, y in edges:
        if kind == 1:
            adj[x].append(y)
            indegree[y] += 1
    order = [v for v in range(1, n + 1) if indegree[v] == 0]
    head = 0
    rank = [0] * (n + 1)
    while head < len(order):
        node = order[head]
        head += 1
        rank[node] = head
        for nxt in adj[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                order.append(nxt)
    if len(order) != n:
        return None
    return rank


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m, edges in read_input():
        rank = topological_rank(n, edges)
        if rank is None:
            out.append("NO")
            continue
        out.append("YES")
        for kind, x, y in edges:
            if kind == 1 or rank[x] < rank[y]:
                out.append("%d %d" % (x, y))
            else:
                out.append("%d %d" % (y, x))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
