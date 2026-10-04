# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from bisect import bisect_left

        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def add(self, i, v):
                n = self.n
                while i <= n:
                    self.bit[i] += v
                    i += i & -i

            def sum(self, i):
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s

        def solve():
            data = list(map(int, sys.stdin.buffer.read().split()))
            t = data[0]
            idx = 1
            ans = []

            for _ in range(t):
                n = data[idx]
                idx += 1
                a = data[idx:idx + n]
                idx += n

                vals = sorted(set(a))
                fw = Fenwick(len(vals))
                inv = 0

                for i, x in enumerate(a):
                    r = bisect_left(vals, x) + 1
                    less = fw.sum(r - 1)
                    leq = fw.sum(r)
                    greater = i - leq
                    inv += min(less, greater)
                    fw.add(r, 1)

                ans.append(str(inv))

            sys.stdout.write("\n".join(ans))

        if __name__ == "__main__":
            solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
