# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 1.00]
class Tree:
    def __init__(self, n):
        self.n = n
        self.mx = [0] * (4 * n + 8)
        self.lazy = [0] * (4 * n + 8)
        self.build(1, 1, n)

    def build(self, v, l, r):
        if l == r:
            self.mx[v] = l
            return
        mid = (l + r) // 2
        self.build(v * 2, l, mid)
        self.build(v * 2 + 1, mid + 1, r)
        self.mx[v] = self.mx[v * 2 + 1]

    def put(self, v, val):
        self.mx[v] += val
        self.lazy[v] += val

    def push(self, v):
        val = self.lazy[v]
        if val:
            self.put(v * 2, val)
            self.put(v * 2 + 1, val)
            self.lazy[v] = 0

    def add(self, ql, qr, val, v=1, l=1, r=0):
        if r == 0:
            r = self.n
        if ql <= l and r <= qr:
            self.put(v, val)
            return
        self.push(v)
        mid = (l + r) // 2
        if ql <= mid:
            self.add(ql, qr, val, v * 2, l, mid)
        if mid < qr:
            self.add(ql, qr, val, v * 2 + 1, mid + 1, r)
        self.mx[v] = self.mx[v * 2] if self.mx[v * 2] >= self.mx[v * 2 + 1] else self.mx[v * 2 + 1]

    def query(self, ql, qr, v=1, l=1, r=0):
        if r == 0:
            r = self.n
        if ql <= l and r <= qr:
            return self.mx[v]
        self.push(v)
        mid = (l + r) // 2
        ans = -10**18
        if ql <= mid:
            ans = self.query(ql, qr, v * 2, l, mid)
        if mid < qr:
            other = self.query(ql, qr, v * 2 + 1, mid + 1, r)
            if other > ans:
                ans = other
        return ans

def ok(m, places, zeros, kinds):
    if m == 0:
        return True
    if zeros < 2 * m or kinds < m:
        return False
    events = [[] for _ in range(m + 2)]
    for arr in places.values():
        lo = 0
        hi = m + 1
        inside = False
        for z in arr:
            if m <= z <= zeros - m:
                inside = True
                break
            if z < m and z > lo:
                lo = z
            if z > zeros - m:
                cur = z - zeros + m + 1
                if cur < hi:
                    hi = cur
        if not inside:
            left = lo + 1
            right = hi - 1
            if left <= right:
                events[left].append(right)
    tree = Tree(m)
    for left in range(1, m + 1):
        for right in events[left]:
            tree.add(1, right, 1)
        if tree.query(left, m) - left + 1 > kinds:
            return False
    return True

def solve(arr):
    zeros = 0
    places = {}
    for x in arr:
        if x:
            if x not in places:
                places[x] = []
            places[x].append(zeros)
        else:
            zeros += 1
    kinds = len(places)
    low, high = 0, min(zeros // 2, kinds)
    while low < high:
        mid = (low + high + 1) // 2
        if ok(mid, places, zeros, kinds):
            low = mid
        else:
            high = mid - 1
    return low


# Clause finish_program [Confidence: 0.80]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    out = []
    for _ in range(t):
        n = data[p]
        p += 1
        out.append(str(solve(data[p:p + n])))
        p += n
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()


