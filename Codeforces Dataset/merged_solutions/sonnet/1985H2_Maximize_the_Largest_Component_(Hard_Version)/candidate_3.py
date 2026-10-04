# CLAUSE: setup_environment
import sys

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

def main():
    tokens = sys.stdin.read().split()
    ptr = 0
    t = int(tokens[ptr])
    ptr += 1
    out = []

# CLAUSE: solve_logic
    for _ in range(t):
        n = int(tokens[ptr])
        m = int(tokens[ptr + 1])
        ptr += 2
        grid = tokens[ptr:ptr + n]
        ptr += n
        dsu = DSU(n * m)
        for r in range(n):
            base = r * m
            for c in range(m):
                if grid[r][c] == '#':
                    if c and grid[r][c - 1] == '#':
                        dsu.union(base + c, base + c - 1)
                    if r and grid[r - 1][c] == '#':
                        dsu.union(base + c, base + c - m)
        info = {}
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '#':
                    root = dsu.find(r * m + c)
                    if root not in info:
                        info[root] = [0, r, r, c, c]
                    item = info[root]
                    item[0] += 1
                    if r < item[1]:
                        item[1] = r
                    if r > item[2]:
                        item[2] = r
                    if c < item[3]:
                        item[3] = c
                    if c > item[4]:
                        item[4] = c
        row_total = [0] * n
        col_total = [0] * m
        col_dots = [0] * m
        for r, s in enumerate(grid):
            row_total[r] = s.count('.')
            for c, ch in enumerate(s):
                if ch == '.':
                    col_dots[c] += 1
        col_total[:] = col_dots[:]
        diff = [[0] * (m + 1) for _ in range(n + 1)]
        best = 0
        for size, min_r, max_r, min_c, max_c in info.values():
            if size > best:
                best = size
            a = min_r - 1
            b = max_r + 1
            x = min_c - 1
            y = max_c + 1
            if a < 0:
                a = 0
            if b >= n:
                b = n - 1
            if x < 0:
                x = 0
            if y >= m:
                y = m - 1
            for r in range(a, b + 1):
                row_total[r] += size
            for c in range(x, y + 1):
                col_total[c] += size
            diff[a][x] += size
            diff[b + 1][x] -= size
            diff[a][y + 1] -= size
            diff[b + 1][y + 1] += size
        above = [0] * m
        for r in range(n):
            left = 0
            for c in range(m):
                left += diff[r][c]
                above[c] += left
                val = row_total[r] + col_total[c] - above[c]
                if grid[r][c] == '.':
                    val -= 1
                if val > best:
                    best = val
        out.append(str(best))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(out))

main()
