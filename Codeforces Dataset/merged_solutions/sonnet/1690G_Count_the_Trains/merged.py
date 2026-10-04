# Clause setup_environment [Confidence: 0.40]
import sys

class SegmentTree:
    def __init__(self, n):
        self.n = n
        size = 1
        while size < n:
            size <<= 1
        self.size = size
        self.data = [0] * (size << 1)

    def set_one(self, pos):
        i = pos + self.size - 1
        if self.data[i] == 1:
            return
        self.data[i] = 1
        i >>= 1
        while i:
            self.data[i] = self.data[i << 1] + self.data[i << 1 | 1]
            i >>= 1

    def set_zero(self, pos):
        i = pos + self.size - 1
        if self.data[i] == 0:
            return
        self.data[i] = 0
        i >>= 1
        while i:
            self.data[i] = self.data[i << 1] + self.data[i << 1 | 1]
            i >>= 1

    def prefix(self, right):
        if right <= 0:
            return 0
        l = self.size
        r = self.size + right
        s = 0
        data = self.data
        while l < r:
            if l & 1:
                s += data[l]
                l += 1
            if r & 1:
                r -= 1
                s += data[r]
            l >>= 1
            r >>= 1
        return s

    def kth(self, order):
        node = 1
        while node < self.size:
            left = node << 1
            if self.data[left] >= order:
                node = left
            else:
                order -= self.data[left]
                node = left | 1
        return node - self.size + 1


# Clause solve_logic [Confidence: 0.80]
def solve():
    values = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = values[p]
    p += 1
    out = []
    for _ in range(t):
        n, m = values[p], values[p + 1]
        p += 2
        a = [0] + values[p:p + n]
        p += n
        bit = Bit(n)
        active = [False] * (n + 1)
        best = 10 ** 30
        total = 0
        for i in range(1, n + 1):
            if a[i] < best:
                best = a[i]
                active[i] = True
                bit.add(i, 1)
                total += 1
        ans = []
        for _ in range(m):
            k, d = values[p], values[p + 1]
            p += 2
            a[k] -= d
            if not active[k]:
                left_count = bit.pref(k - 1)
                left_pos = bit.kth(left_count)
                if a[k] < a[left_pos]:
                    active[k] = True
                    bit.add(k, 1)
                    total += 1
                else:
                    ans.append(str(total))
                    continue
            rank = bit.pref(k)
            while rank < total:
                nxt = bit.kth(rank + 1)
                if a[nxt] < a[k]:
                    break
                active[nxt] = False
                bit.add(nxt, -1)
                total -= 1
            ans.append(str(total))
        out.append(" ".join(ans))
    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.40]
main()


