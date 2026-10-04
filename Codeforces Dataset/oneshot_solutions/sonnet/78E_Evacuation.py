import sys
from collections import deque

INF = 10 ** 9

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, v, to, cap):
        self.graph[v].append([to, cap, len(self.graph[to])])
        self.graph[to].append([v, 0, len(self.graph[v]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0

        while q:
            v = q.popleft()
            for to, cap, rev in self.graph[v]:
                if cap > 0 and self.level[to] == -1:
                    self.level[to] = self.level[v] + 1
                    q.append(to)

        return self.level[t] != -1

    def dfs(self, v, t, pushed):
        if v == t:
            return pushed

        while self.ptr[v] < len(self.graph[v]):
            edge = self.graph[v][self.ptr[v]]
            to, cap, rev = edge

            if cap > 0 and self.level[to] == self.level[v] + 1:
                tr = self.dfs(to, t, min(pushed, cap))
                if tr:
                    edge[1] -= tr
                    self.graph[to][rev][1] += tr
                    return tr

            self.ptr[v] += 1

        return 0

    def flow(self, s, t):
        result = 0

        while self.bfs(s, t):
            self.ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, INF)
                if not pushed:
                    break
                result += pushed

        return result


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    n = int(data[idx])
    time_limit = int(data[idx + 1])
    idx += 2

    capsules_grid = data[idx:idx + n]
    idx += n
    scientists_grid = data[idx:idx + n]

    start = None
    labs = []
    capsules = []
    scientists = []

    for i in range(n):
        for j in range(n):
            c = capsules_grid[i][j]
            if c == 'Z':
                start = (i, j)
            if c not in 'YZ':
                labs.append((i, j))
                if int(c) > 0:
                    capsules.append((i, j, int(c)))

            s = scientists_grid[i][j]
            if s not in 'YZ' and int(s) > 0:
                scientists.append((i, j, int(s)))

    poison = [[INF] * n for _ in range(n)]
    q = deque()

    if start is not None:
        x, y = start
        poison[x][y] = 0
        q.append((x, y))

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if capsules_grid[nx][ny] in 'YZ':
                    continue
                if poison[nx][ny] == INF:
                    poison[nx][ny] = poison[x][y] + 1
                    q.append((nx, ny))

    s_count = len(scientists)
    c_count = len(capsules)
    source = s_count + c_count
    sink = source + 1

    dinic = Dinic(sink + 1)

    for i, (x, y, cnt) in enumerate(scientists):
        dinic.add_edge(source, i, cnt)

    for i, (x, y, cnt) in enumerate(capsules):
        dinic.add_edge(s_count + i, sink, cnt)

    for i, (sx, sy, cnt) in enumerate(scientists):
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        if poison[sx][sy] > 0:
            dist[sx][sy] = 0
            q.append((sx, sy))

        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                nd = dist[x][y] + 1

                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if capsules_grid[nx][ny] in 'YZ':
                    continue
                if dist[nx][ny] != -1:
                    continue
                if nd > time_limit or nd >= poison[nx][ny]:
                    continue

                dist[nx][ny] = nd
                q.append((nx, ny))

        for j, (cx, cy, cap) in enumerate(capsules):
            if dist[cx][cy] != -1:
                dinic.add_edge(i, s_count + j, INF)

    print(dinic.flow(source, sink))


if __name__ == "__main__":
    main()
