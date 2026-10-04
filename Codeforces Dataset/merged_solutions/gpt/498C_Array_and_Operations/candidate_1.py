# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, v, to, cap):
        self.g[v].append([to, cap, len(self.g[to])])
        self.g[to].append([v, 0, len(self.g[v]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            v = q.popleft()
            for to, cap, rev in self.g[v]:
                if cap > 0 and self.level[to] == -1:
                    self.level[to] = self.level[v] + 1
                    q.append(to)
        return self.level[t] != -1

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.it[v], len(self.g[v])):
            self.it[v] = i
            to, cap, rev = self.g[v][i]
            if cap > 0 and self.level[v] + 1 == self.level[to]:
                ret = self.dfs(to, t, min(f, cap))
                if ret:
                    self.g[v][i][1] -= ret
                    self.g[to][rev][1] += ret
                    return ret
        return 0

    def max_flow(self, s, t):
        flow = 0
        inf = 10 ** 18
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, inf)
                if not f:
                    break
                flow += f
        return flow

def factorize(x):
    res = {}
    d = 2
    while d * d <= x:
        while x % d == 0:
            res[d] = res.get(d, 0) + 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        res[x] = res.get(x, 0) + 1
    return res

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    a = data[2:2 + n]
    pos = 2 + n

    edges = []
    for _ in range(m):
        u, v = data[pos] - 1, data[pos + 1] - 1
        pos += 2
        edges.append((u, v))

    factors = [factorize(x) for x in a]
    primes = set()
    for f in factors:
        primes.update(f.keys())

    ans = 0
    s, t = n, n + 1
    inf = 10 ** 9

    for p in primes:
        dinic = Dinic(n + 2)

        for i in range(n):
            c = factors[i].get(p, 0)
            if c:
                if (i + 1) % 2 == 1:
                    dinic.add_edge(s, i, c)
                else:
                    dinic.add_edge(i, t, c)

        for u, v in edges:
            if (u + 1) % 2 == 1:
                dinic.add_edge(u, v, inf)
            else:
                dinic.add_edge(v, u, inf)

        ans += dinic.max_flow(s, t)

    print(ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
