import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    g = [[] for _ in range(n)]
    it = 1
    for _ in range(n - 1):
        a = data[it] - 1
        b = data[it + 1] - 1
        it += 2
        g[a].append(b)
        g[b].append(a)

    dist = [[0] * n for _ in range(n)]
    for s in range(n):
        d = [-1] * n
        d[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for to in g[v]:
                if d[to] == -1:
                    d[to] = d[v] + 1
                    q.append(to)
        dist[s] = d

    m = 1
    while m < n:
        m <<= 1

    inf = 10 ** 18
    u = [[inf] * (m + 1) for _ in range(n + 1)]
    p = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                u[i][j] = dist[i - 1][j - 1]

    for i in range(1, n + 1):
        links = [0] * (m + 1)
        mins = [inf] * (m + 1)
        used = [False] * (m + 1)
        marked_i = 0
        marked_j = 0
        j = 0
        p[0][0] = i
        while True:
            used[j] = True
            i0 = p[i][j] if i != 0 else p[0][j]
            delta = inf
            j1 = 0
            for j2 in range(1, m + 1):
                if not used[j2]:
                    cur = u[i0][j2] - mins[j2]
                    if cur < delta:
                        delta = cur
                        j1 = j2
            for j2 in range(m + 1):
                if used[j2]:
                    mins[j2] += delta
                else:
                    links[j2] -= delta
            j = j1
            if p[i][j] == 0:
                break
        while True:
            j1 = links[j]
            p[i][j] = p[i][j1]
            j = j1
            if j == 0:
                break

    ans = [0] * n
    for j in range(1, n + 1):
        if p[n][j] != 0:
            ans[p[n][j] - 1] = j

    total = sum(dist[i][ans[i] - 1] for i in range(n))
    print(total)
    print(*ans)

if __name__ == "__main__":
    main()
