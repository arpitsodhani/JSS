import sys
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

MAX_LCM = 100000

class SegmentTree:
    def __init__(self, a, n):
        self.n = n
        self.a = a
        self.tree = [None] * (4 * n)
        self.build(1, 1, n)

    def build(self, node, l, r):
        if l == r:
            period = self.a[l]
            L = period
            g = [0] * L
            for t in range(L):
                g[t] = 2 if t % period == 0 else 1
            self.tree[node] = (L, g)
        else:
            mid = (l + r) // 2
            self.build(2 * node, l, mid)
            self.build(2 * node + 1, mid + 1, r)
            self.tree[node] = self.merge(self.tree[2 * node], self.tree[2 * node + 1])

    def merge(self, func1, func2):
        if func1 is None:
            return func2
        if func2 is None:
            return func1

        L1, g1 = func1
        L2, g2 = func2
        L = lcm(L1, L2)

        if L > MAX_LCM:
            return None

        g = [0] * L
        for r in range(L):
            t_mid = r + g1[r % L1]
            g[r] = g1[r % L1] + g2[t_mid % L2]
        return (L, g)

    def update(self, node, l, r, pos, val):
        if l == r:
            period = val
            L = period
            g = [0] * L
            for t in range(L):
                g[t] = 2 if t % period == 0 else 1
            self.tree[node] = (L, g)
        else:
            mid = (l + r) // 2
            if pos <= mid:
                self.update(2 * node, l, mid, pos, val)
            else:
                self.update(2 * node + 1, mid + 1, r, pos, val)
            self.tree[node] = self.merge(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return None
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        left = self.query(2 * node, l, mid, ql, qr)
        right = self.query(2 * node + 1, mid + 1, r, ql, qr)
        return self.merge(left, right)

    def range_query(self, ql, qr):
        if ql > qr:
            return 0
        result = self.query(1, 1, self.n, ql, qr)
        if result is None:
            t = 0
            for i in range(ql, qr + 1):
                if t % self.a[i] == 0:
                    t += 2
                else:
                    t += 1
            return t
        else:
            L, g = result
            return g[0]

    def point_update(self, pos, val):
        self.a[pos] = val
        self.update(1, 1, self.n, pos, val)

def main():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0

    n = int(input_data[idx])
    idx += 1

    a = [0] + [int(input_data[idx + i]) for i in range(n)]
    idx += n

    q = int(input_data[idx])
    idx += 1

    st = SegmentTree(a, n)

    results = []
    for _ in range(q):
        query_type = input_data[idx]
        idx += 1
        if query_type == 'C':
            i = int(input_data[idx])
            idx += 1
            val = int(input_data[idx])
            idx += 1
            st.point_update(i, val)
        else:
            x = int(input_data[idx])
            idx += 1
            y = int(input_data[idx])
            idx += 1
            results.append(st.range_query(x, y - 1))

    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    main()
