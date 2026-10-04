# CLAUSE: setup_environment
import sys

class Bit:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, v):
        n = self.n
        tree = self.tree
        while i <= n:
            tree[i] += v
            i += i & -i

    def pref(self, i):
        s = 0
        tree = self.tree
        while i:
            s += tree[i]
            i -= i & -i
        return s

    def kth(self, k):
        i = 0
        step = 1 << (self.n.bit_length() - 1)
        tree = self.tree
        n = self.n
        while step:
            j = i + step
            if j <= n and tree[j] < k:
                i = j
                k -= tree[j]
            step >>= 1
        return i + 1

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
