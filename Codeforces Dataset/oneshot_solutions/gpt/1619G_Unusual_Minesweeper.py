import sys

input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.p[b] = a
        self.sz[a] += self.sz[b]


def solve():
    t = int(input())
    out = []
    INF = 10 ** 30

    for _ in range(t):
        n, k = map(int, input().split())
        mines = []
        timers = [0] * n

        for i in range(n):
            x, y, tm = map(int, input().split())
            mines.append((x, y, i))
            timers[i] = tm

        dsu = DSU(n)

        mines.sort(key=lambda v: (v[0], v[1]))
        for i in range(1, n):
            x1, y1, id1 = mines[i - 1]
            x2, y2, id2 = mines[i]
            if x1 == x2 and y2 - y1 <= k:
                dsu.union(id1, id2)

        mines.sort(key=lambda v: (v[1], v[0]))
        for i in range(1, n):
            x1, y1, id1 = mines[i - 1]
            x2, y2, id2 = mines[i]
            if y1 == y2 and x2 - x1 <= k:
                dsu.union(id1, id2)

        mn = {}
        for i in range(n):
            r = dsu.find(i)
            if r not in mn or timers[i] < mn[r]:
                mn[r] = timers[i]

        vals = sorted(mn.values())
        m = len(vals)
        ans = m - 1

        for i, v in enumerate(vals):
            ans = min(ans, max(v, m - i - 2))

        out.append(str(ans))

    print("\n".join(out))


if __name__ == "__main__":
    solve()
