# CLAUSE: setup_environment
import sys
from collections import deque

INF = 10 ** 9

class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]
        self.level = [0] * n
        self.it = [0] * n

    def add_edge(self, v, u, c):
        self.g[v].append([u, c, len(self.g[u])])
        self.g[u].append([v, 0, len(self.g[v]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * len(self.g)
        self.level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for u, c, r in self.g[v]:
                if c and self.level[u] < 0:
                    self.level[u] = self.level[v] + 1
                    q.append(u)
        return self.level[t] >= 0

    def dfs(self, v, t, f):
        if v == t:
            return f
        while self.it[v] < len(self.g[v]):
            e = self.g[v][self.it[v]]
            u, c, r = e
            if c and self.level[u] == self.level[v] + 1:
                got = self.dfs(u, t, min(f, c))
                if got:
                    e[1] -= got
                    self.g[u][r][1] += got
                    return got
            self.it[v] += 1
        return 0

    def maxflow(self, s, t):
        ans = 0
        while self.bfs(s, t):
            self.it = [0] * len(self.g)
            while True:
                pushed = self.dfs(s, t, INF)
                if pushed == 0:
                    break
                ans += pushed
        return ans

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    limit = int(data[1])
    a = data[2:2 + n]
    b = data[2 + n:2 + 2 * n]
    scientists = []
    capsules = []
    start = (-1, -1)
    for i in range(n):
        for j, ch in enumerate(a[i]):
            if ch == "Z":
                start = (i, j)
            elif ch != "Y" and int(ch) > 0:
                capsules.append((i, j, int(ch)))
            ch2 = b[i][j]
            if ch2 not in "YZ" and int(ch2) > 0:
                scientists.append((i, j, int(ch2)))
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    poison = [[INF] * n for _ in range(n)]
    q = deque()
    if start[0] != -1:
        poison[start[0]][start[1]] = 0
        q.append(start)
    while q:
        x, y = q.popleft()
        nd = poison[x][y] + 1
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and a[nx][ny] not in "YZ" and poison[nx][ny] == INF:
                poison[nx][ny] = nd
                q.append((nx, ny))
    ns = len(scientists)
    nc = len(capsules)
    source = ns + nc
    sink = source + 1
    flow = Dinic(sink + 1)
    for i, item in enumerate(scientists):
        flow.add_edge(source, i, item[2])
    for j, item in enumerate(capsules):
        flow.add_edge(ns + j, sink, item[2])
    for i, (sx, sy, cnt) in enumerate(scientists):
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        if poison[sx][sy] > 0:
            dist[sx][sy] = 0
            q.append((sx, sy))
        while q:
            x, y = q.popleft()
            nd = dist[x][y] + 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and a[nx][ny] not in "YZ" and dist[nx][ny] < 0 and nd <= limit and nd < poison[nx][ny]:
                    dist[nx][ny] = nd
                    q.append((nx, ny))
        for j, (cx, cy, cap) in enumerate(capsules):
            if dist[cx][cy] >= 0:
                flow.add_edge(i, ns + j, INF)
    sys.stdout.write(str(flow.maxflow(source, sink)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
