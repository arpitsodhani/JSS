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
    incoming = [0] * (n + 1)
    for kind, x, y in edges:
        if kind:
            adj[x].append(y)
            incoming[y] += 1
    stack = []
    for v in range(1, n + 1):
        if incoming[v] == 0:
            stack.append(v)
    rank = [0] * (n + 1)
    seen = 0
    while stack:
        node = stack.pop()
        seen += 1
        rank[node] = seen
        for nxt in adj[node]:
            incoming[nxt] -= 1
            if incoming[nxt] == 0:
                stack.append(nxt)
    if seen != n:
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
            if kind or rank[x] < rank[y]:
                out.append("%d %d" % (x, y))
            else:
                out.append("%d %d" % (y, x))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
