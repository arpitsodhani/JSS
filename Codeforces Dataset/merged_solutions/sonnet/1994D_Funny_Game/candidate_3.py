# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def root(self, x):
        trail = []
        while self.parent[x] != x:
            trail.append(x)
            x = self.parent[x]
        for y in trail:
            self.parent[y] = x
        return x

    def join(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

def construct(n, values):
    dsu = DSU(n)
    by_step = []

    mod = n - 1
    while mod >= 1:
        bucket = [-1] * mod
        edge = None

        for idx in range(n):
            r = values[idx] % mod
            other = bucket[r]
            if other == -1:
                bucket[r] = idx
            elif dsu.root(idx) != dsu.root(other):
                dsu.join(idx, other)
                edge = (idx + 1, other + 1)
                break

        if edge is None:
            return []
        by_step.append(edge)
        mod -= 1

    return by_step[::-1]

# CLAUSE: finish_program
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    cases = nums[pos]
    pos += 1
    out = []

    for _ in range(cases):
        n = nums[pos]
        pos += 1
        values = nums[pos:pos + n]
        pos += n
        result = construct(n, values)

        if len(result) != n - 1:
            out.append("NO")
        else:
            out.append("YES")
            for edge in result:
                out.append("{} {}".format(edge[0], edge[1]))

    print("\n".join(out))

if __name__ == "__main__":
    main()
