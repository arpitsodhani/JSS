# CLAUSE: setup_environment
import sys
from bisect import bisect_right

# CLAUSE: solve_logic
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
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        idx = 0
        bitmask = 1 << (self.n.bit_length() - 1)
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bitmask >>= 1
        return idx

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:]
    if len(a) != n:
        print("Impossible")
        return

    buckets = [{} for _ in range(3)]
    for i, x in enumerate(a, 1):
        r = x % 3
        q = x // 3
        buckets[r].setdefault(q, []).append(i)

    vals = []
    trees = []
    for r in range(3):
        v = sorted(buckets[r])
        vals.append(v)
        fw = Fenwick(len(v))
        for j, q in enumerate(v):
            fw.add(j, len(buckets[r][q]))
        trees.append(fw)

    ans = []
    limit = 0

    for pos in range(n):
        r = pos % 3
        p = bisect_right(vals[r], limit)
        if p == 0:
            print("Impossible")
            return

        cnt = trees[r].sum(p)
        if cnt == 0:
            print("Impossible")
            return

        j = trees[r].kth(cnt)
        q = vals[r][j]
        idx = buckets[r][q].pop()
        trees[r].add(j, -1)
        ans.append(idx)

        if r == 2:
            limit = q + 1
        else:
            limit = q

    print("Possible")
    print(*ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
