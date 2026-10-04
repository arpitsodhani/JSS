# CLAUSE: setup_environment
import sys
from collections import deque

BIG = 1 << 30

class Edge:
    __slots__ = ("to", "rev", "cap")
    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap

class Network:
    def __init__(self, size):
        self.adj = [[] for _ in range(size)]

    def link(self, x, y, c):
        self.adj[x].append(Edge(y, len(self.adj[y]), c))
        self.adj[y].append(Edge(x, len(self.adj[x]) - 1, 0))

    def levels(self, s, t):
        lv = [-1] * len(self.adj)
        lv[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for e in self.adj[v]:
                if e.cap > 0 and lv[e.to] == -1:
                    lv[e.to] = lv[v] + 1
                    q.append(e.to)
        self.lv = lv
        return lv[t] != -1

    def send(self, v, t, amount):
        if v == t:
            return amount
        adjv = self.adj[v]
        while self.work[v] < len(adjv):
            e = adjv[self.work[v]]
            if e.cap > 0 and self.lv[e.to] == self.lv[v] + 1:
                ret = self.send(e.to, t, amount if amount < e.cap else e.cap)
                if ret:
                    e.cap -= ret
                    self.adj[e.to][e.rev].cap += ret
                    return ret
            self.work[v] += 1
        return 0

    def run(self, s, t):
        total = 0
        while self.levels(s, t):
            self.work = [0] * len(self.adj)
            got = self.send(s, t, BIG)
            while got:
                total += got
                got = self.send(s, t, BIG)
        return total

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
