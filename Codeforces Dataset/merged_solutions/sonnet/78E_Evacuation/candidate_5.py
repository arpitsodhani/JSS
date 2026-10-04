# CLAUSE: setup_environment
import sys
from collections import deque

INF = 10 ** 8

class Dinic:
    def __init__(self, n):
        self.n = n
        self.to = []
        self.cap = []
        self.next = []
        self.head = [-1] * n

    def add_arc(self, v, u, c):
        self.to.append(u)
        self.cap.append(c)
        self.next.append(self.head[v])
        self.head[v] = len(self.to) - 1
        self.to.append(v)
        self.cap.append(0)
        self.next.append(self.head[u])
        self.head[u] = len(self.to) - 1

    def build_level(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            e = self.head[v]
            while e != -1:
                u = self.to[e]
                if self.cap[e] > 0 and self.level[u] == -1:
                    self.level[u] = self.level[v] + 1
                    q.append(u)
                e = self.next[e]
        return self.level[t] != -1

    def push(self, v, t, f):
        if v == t:
            return f
        e = self.cur[v]
        while e != -1:
            self.cur[v] = e
            u = self.to[e]
            if self.cap[e] > 0 and self.level[u] == self.level[v] + 1:
                got = self.push(u, t, min(f, self.cap[e]))
                if got:
                    self.cap[e] -= got
                    self.cap[e ^ 1] += got
                    return got
            e = self.next[e]
            self.cur[v] = e
        return 0

    def flow(self, s, t):
        ans = 0
        while self.build_level(s, t):
            self.cur = self.head[:]
            while True:
                got = self.push(s, t, INF)
                if not got:
                    break
                ans += got
        return ans

# CLAUSE: solve_logic
def neighbors(x, y, n):
    if x:
        yield x - 1, y
    if x + 1 < n:
        yield x + 1, y
    if y:
        yield x, y - 1
    if y + 1 < n:
        yield x, y + 1

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    limit = int(data[1])
    cg = data[2:2 + n]
    sg = data[2 + n:2 + 2 * n]
    start = None
    labs = []
    scientists = []
    capsules = []
    for x in range(n):
        for y in range(n):
            if cg[x][y] == "Z":
                start = (x, y)
            if cg[x][y] not in "YZ":
                labs.append((x, y))
                z = int(cg[x][y])
                if z > 0:
                    capsules.append((x, y, z))
            if sg[x][y] not in "YZ":
                z = int(sg[x][y])
                if z > 0:
                    scientists.append((x, y, z))
    poison = [[INF] * n for _ in range(n)]
    q = deque()
    if start is not None:
        poison[start[0]][start[1]] = 0
        q.append(start)
    while q:
        x, y = q.popleft()
        for nx, ny in neighbors(x, y, n):
            if cg[nx][ny] not in "YZ" and poison[nx][ny] == INF:
                poison[nx][ny] = poison[x][y] + 1
                q.append((nx, ny))
    s_count = len(scientists)
    c_count = len(capsules)
    source = s_count + c_count
    sink = source + 1
    din = Dinic(sink + 1)
    for i, value in enumerate(scientists):
        din.add_arc(source, i, value[2])
    for i, value in enumerate(capsules):
        din.add_arc(s_count + i, sink, value[2])
    capsule_at = {}
    for i, (x, y, cap) in enumerate(capsules):
        capsule_at.setdefault((x, y), []).append(i)
    for i, (sx, sy, cnt) in enumerate(scientists):
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        if poison[sx][sy] > 0:
            dist[sx][sy] = 0
            q.append((sx, sy))
        while q:
            x, y = q.popleft()
            here = (x, y)
            if here in capsule_at:
                for j in capsule_at[here]:
                    din.add_arc(i, s_count + j, INF)
            nd = dist[x][y] + 1
            if nd > limit:
                continue
            for nx, ny in neighbors(x, y, n):
                if cg[nx][ny] in "YZ":
                    continue
                if dist[nx][ny] != -1:
                    continue
                if nd >= poison[nx][ny]:
                    continue
                dist[nx][ny] = nd
                q.append((nx, ny))
    sys.stdout.write(str(din.flow(source, sink)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
