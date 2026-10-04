# CLAUSE: setup_environment
import sys

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, v):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    segs = []
    rights = []
    p = 1
    for i in range(n):
        l = data[p]
        r = data[p + 1]
        p += 2
        segs.append((l, r, i))
        rights.append(r)

    rank = {v: i + 1 for i, v in enumerate(sorted(rights))}
    segs.sort(key=lambda x: -x[0])

    tree = Fenwick(n)
    ans = [0] * n
    for l, r, i in segs:
        k = rank[r]
        ans[i] = tree.query(k - 1)
        tree.add(k, 1)

    sys.stdout.write("\n".join(map(str, ans)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
