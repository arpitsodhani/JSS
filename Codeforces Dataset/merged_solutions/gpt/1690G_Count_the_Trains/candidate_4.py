# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

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

        def kth(self, k):
            idx = 0
            step = 1 << (self.n.bit_length() - 1)
            while step:
                nxt = idx + step
                if nxt <= self.n and self.bit[nxt] < k:
                    idx = nxt
                    k -= self.bit[nxt]
                step >>= 1
            return idx + 1

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        it = iter(data)
        t = next(it)
        ans = []

        for _ in range(t):
            n = next(it)
            m = next(it)
            a = [0] + [next(it) for _ in range(n)]

            fw = Fenwick(n)
            active = [False] * (n + 1)
            cur = 10 ** 30
            total = 0

            for i in range(1, n + 1):
                if a[i] < cur:
                    active[i] = True
                    fw.add(i, 1)
                    total += 1
                    cur = a[i]

            out = []

            for _ in range(m):
                k = next(it)
                d = next(it)
                a[k] -= d

                changed = False

                if active[k]:
                    changed = True
                else:
                    c = fw.sum(k)
                    if c == 0 or a[fw.kth(c)] > a[k]:
                        active[k] = True
                        fw.add(k, 1)
                        total += 1
                        changed = True

                if changed:
                    c = fw.sum(k)
                    while c < total:
                        nxt = fw.kth(c + 1)
                        if a[nxt] < a[k]:
                            break
                        active[nxt] = False
                        fw.add(nxt, -1)
                        total -= 1

                out.append(str(total))

            ans.append(" ".join(out))

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
