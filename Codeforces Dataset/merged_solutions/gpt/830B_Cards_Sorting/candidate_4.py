# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from bisect import bisect_left
    from collections import defaultdict

    class Fenwick:
        def __init__(self, n):
            self.n = n
            self.bit = [0] * (n + 1)

        def add(self, i, v):
            i += 1
            while i <= self.n:
                self.bit[i] += v
                i += i & -i

        def sum(self, i):
            s = 0
            i += 1
            while i > 0:
                s += self.bit[i]
                i -= i & -i
            return s

        def range_sum(self, l, r):
            if l > r:
                return 0
            return self.sum(r) - (self.sum(l - 1) if l else 0)

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        n = data[0]
        a = data[1:1 + n]

        positions = defaultdict(list)
        for i, x in enumerate(a):
            positions[x].append(i)

        fw = Fenwick(n)
        for i in range(n):
            fw.add(i, 1)

        ans = 0
        cur = 0

        for value in sorted(positions):
            pos = positions[value]
            k = bisect_left(pos, cur)
            order = pos[k:] + pos[:k]

            for p in order:
                if p >= cur:
                    ans += fw.range_sum(cur, p)
                else:
                    ans += fw.range_sum(cur, n - 1) + fw.range_sum(0, p)
                fw.add(p, -1)
                cur = p

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
