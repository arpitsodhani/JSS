import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    edges = []
    p = 2
    for _ in range(m):
        edges.append((data[p], data[p + 1]))
        p += 2

    def ok(k):
        adj = [[] for _ in range(n + 1)]
        indeg = [0] * (n + 1)

        for i in range(k):
            a, b = edges[i]
            adj[a].append(b)
            indeg[b] += 1

        q = deque(i for i in range(1, n + 1) if indeg[i] == 0)
        seen = 0

        while q:
            if len(q) > 1:
                return False
            v = q.popleft()
            seen += 1
            for to in adj[v]:
                indeg[to] -= 1
                if indeg[to] == 0:
                    q.append(to)

        return seen == n

    if not ok(m):
        print(-1)
        return

    lo, hi = 1, m
    ans = m

    while lo <= hi:
        mid = (lo + hi) // 2
        if ok(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)

if __name__ == "__main__":
    main()
