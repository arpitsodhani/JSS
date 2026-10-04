# CLAUSE: setup_environment
import sys
from collections import defaultdict, deque

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out = []

    for _ in range(t):
        n = next(it)
        m = n - 2

        tris = [None] * (m + 1)
        edge_tris = defaultdict(list)

        for i in range(1, m + 1):
            a = next(it)
            b = next(it)
            c = next(it)
            edges = []
            for x, y in ((a, b), (b, c), (c, a)):
                if x > y:
                    x, y = y, x
                e = (x, y)
                edges.append(e)
                edge_tris[e].append(i)
            tris[i] = edges

        adj = [[] for _ in range(n + 1)]
        boundary = set()

        for e, owners in edge_tris.items():
            if len(owners) == 1:
                boundary.add(e)
                a, b = e
                adj[a].append(b)
                adj[b].append(a)

        p = [1]
        prev = 0
        cur = 1
        while len(p) < n:
            a, b = adj[cur]
            nxt = a if a != prev else b
            p.append(nxt)
            prev, cur = cur, nxt

        border_count = [0] * (m + 1)
        q = deque()

        for i in range(1, m + 1):
            cnt = 0
            for e in tris[i]:
                if e in boundary:
                    cnt += 1
            border_count[i] = cnt
            if cnt >= 2:
                q.append(i)

        removed = [False] * (m + 1)
        order = []

        while q:
            v = q.popleft()
            if removed[v] or border_count[v] < 2:
                continue

            removed[v] = True
            order.append(v)

            for e in tris[v]:
                if e in boundary:
                    continue
                boundary.add(e)
                owners = edge_tris[e]
                other = owners[0] ^ owners[1] ^ v
                if not removed[other]:
                    border_count[other] += 1
                    if border_count[other] >= 2:
                        q.append(other)

        out.append(" ".join(map(str, p)))
        out.append(" ".join(map(str, order)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
