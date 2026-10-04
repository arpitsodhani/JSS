# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class Segments:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = [1] * n
        self.used = [False] * n
        self.odd = 0

    def find(self, x):
        parent = self.parent
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def activate(self, x):
        self.used[x] = True
        self.odd += 1

    def unite(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.count[ra] < self.count[rb]:
            ra, rb = rb, ra
        self.odd -= self.count[ra] % 2
        self.odd -= self.count[rb] % 2
        self.parent[rb] = ra
        self.count[ra] += self.count[rb]
        self.odd += self.count[ra] % 2

def main():
    items = list(map(int, sys.stdin.buffer.read().split()))
    n = items[0]
    wall = items[1:]

    pairs = sorted((wall[i], i) for i in range(n))
    segments = Segments(n)

    k = 0
    while k < n:
        height = pairs[k][0]
        batch = []
        while k < n and pairs[k][0] == height:
            batch.append(pairs[k][1])
            k += 1

        for pos in batch:
            segments.activate(pos)
            if pos > 0 and segments.used[pos - 1]:
                segments.unite(pos, pos - 1)
            if pos + 1 < n and segments.used[pos + 1]:
                segments.unite(pos, pos + 1)

        if k != n and segments.odd:
            sys.stdout.write("NO\n")
            return

    sys.stdout.write("YES\n")

# CLAUSE: finish_program
main()
