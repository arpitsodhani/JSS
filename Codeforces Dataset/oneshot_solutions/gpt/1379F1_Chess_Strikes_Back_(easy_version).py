import sys

class FenwickMin:
    def __init__(self, n):
        self.n = n
        self.bit = [10**18] * (n + 2)

    def update(self, i, v):
        n = self.n
        while i <= n:
            if v < self.bit[i]:
                self.bit[i] = v
            i += i & -i

    def query(self, i):
        res = 10**18
        while i > 0:
            if self.bit[i] < res:
                res = self.bit[i]
            i -= i & -i
        return res


class FenwickMax:
    def __init__(self, n):
        self.n = n
        self.bit = [-1] * (n + 2)

    def update(self, i, v):
        n = self.n
        while i <= n:
            if v > self.bit[i]:
                self.bit[i] = v
            i += i & -i

    def query(self, i):
        res = -1
        while i > 0:
            if self.bit[i] > res:
                res = self.bit[i]
            i -= i & -i
        return res


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, q = data[0], data[1], data[2]
    a_min = FenwickMin(n)
    b_max_rev = FenwickMax(n)

    bad = False
    out = []
    idx = 3

    for _ in range(q):
        x, y = data[idx], data[idx + 1]
        idx += 2

        if (x + y) % 2 == 0 and not bad:
            if x % 2 == 1:
                r = (x + 1) // 2
                c = (y + 1) // 2

                rev = n - r + 1
                if b_max_rev.query(rev) >= c:
                    bad = True

                a_min.update(r, c)
            else:
                r = x // 2
                c = y // 2

                if a_min.query(r) <= c:
                    bad = True

                rev = n - r + 1
                b_max_rev.update(rev, c)

        out.append("NO" if bad else "YES")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
