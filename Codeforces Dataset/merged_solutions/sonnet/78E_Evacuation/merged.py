# Clause setup_environment [Confidence: 0.60]
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


# Clause solve_logic [Confidence: 0.80]
def safe_bfs(starts, grid, n):
    d = [[BIG] * n for _ in range(n)]
    q = deque()
    for x, y in starts:
        d[x][y] = 0
        q.append((x, y))
    while q:
        x, y = q.popleft()
        v = d[x][y] + 1
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] not in "YZ" and d[nx][ny] == BIG:
                d[nx][ny] = v
                q.append((nx, ny))
    return d

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    n, t = map(int, tokens[:2])
    cap_grid = tokens[2:2 + n]
    sci_grid = tokens[2 + n:2 + 2 * n]
    leak = []
    people = []
    seats = []
    for r in range(n):
        for c in range(n):
            cell = cap_grid[r][c]
            if cell == "Z":
                leak.append((r, c))
            elif cell != "Y":
                val = ord(cell) - 48
                if val:
                    seats.append((r, c, val))
            here = sci_grid[r][c]
            if here not in "YZ":
                val = ord(here) - 48
                if val:
                    people.append((r, c, val))
    poison = safe_bfs(leak, cap_grid, n)
    left = len(people)
    right = len(seats)
    src = left + right
    dst = src + 1
    net = Network(dst + 1)
    for i, p in enumerate(people):
        net.link(src, i, p[2])
    for j, s in enumerate(seats):
        net.link(left + j, dst, s[2])
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for i, (sx, sy, amount) in enumerate(people):
        reach = [[-1] * n for _ in range(n)]
        q = deque()
        if poison[sx][sy] != 0:
            reach[sx][sy] = 0
            q.append((sx, sy))
        while q:
            x, y = q.popleft()
            step = reach[x][y] + 1
            if step > t:
                continue
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if cap_grid[nx][ny] not in "YZ" and reach[nx][ny] == -1 and step < poison[nx][ny]:
                        reach[nx][ny] = step
                        q.append((nx, ny))
        for j, (cx, cy, room) in enumerate(seats):
            if reach[cx][cy] != -1:
                net.link(i, left + j, BIG)
    print(net.run(src, dst))


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


