# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def find(parent, x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(parent, size, a, b):
        ra = find(parent, a)
        rb = find(parent, b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    it = iter(data)
    n = next(it)
    m = next(it)
    k = next(it)

    c = [next(it) for _ in range(k)]

    typ = [0] * (n + 1)
    ranges = []
    pos = 1
    for i, cnt in enumerate(c):
        start = pos
        end = pos + cnt - 1
        ranges.append((start, end))
        for v in range(start, end + 1):
            typ[v] = i
        pos = end + 1

    parent = list(range(n + 1))
    size = [1] * (n + 1)
    edges = []

    INF = 10 ** 18
    dist = [[INF] * k for _ in range(k)]
    for i in range(k):
        dist[i][i] = 0

    for _ in range(m):
        u = next(it)
        v = next(it)
        x = next(it)
        edges.append((u, v, x))
        if x == 0:
            union(parent, size, u, v)

    for start, end in ranges:
        root = find(parent, start)
        for v in range(start + 1, end + 1):
            if find(parent, v) != root:
                print("No")
                sys.exit()

    for u, v, x in edges:
        a = typ[u]
        b = typ[v]
        if x < dist[a][b]:
            dist[a][b] = x
            dist[b][a] = x

    for mid in range(k):
        dm = dist[mid]
        for i in range(k):
            via = dist[i][mid]
            if via == INF:
                continue
            row = dist[i]
            for j in range(k):
                nd = via + dm[j]
                if nd < row[j]:
                    row[j] = nd

    out = ["Yes"]
    for i in range(k):
        out.append(" ".join("-1" if dist[i][j] == INF else str(dist[i][j]) for j in range(k)))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
