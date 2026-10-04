# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class Segment:
    def __init__(self, n):
        self.n = n
        self.maxima = [0] * (4 * n + 12)
        self.delayed = [0] * (4 * n + 12)
        self._init(1, 1, n)

    def _init(self, pos, low, high):
        if low == high:
            self.maxima[pos] = low
        else:
            mid = (low + high) >> 1
            self._init(pos << 1, low, mid)
            self._init(pos << 1 | 1, mid + 1, high)
            self.maxima[pos] = self.maxima[pos << 1 | 1]

    def _mark(self, pos, delta):
        self.maxima[pos] += delta
        self.delayed[pos] += delta

    def _down(self, pos):
        delta = self.delayed[pos]
        if delta != 0:
            self._mark(pos << 1, delta)
            self._mark(pos << 1 | 1, delta)
            self.delayed[pos] = 0

    def add_prefix(self, end, pos=1, low=1, high=0):
        if high == 0:
            high = self.n
        if end >= high:
            self._mark(pos, 1)
            return
        self._down(pos)
        mid = (low + high) >> 1
        self.add_prefix(end, pos << 1, low, mid)
        if end > mid:
            self.add_prefix(end, pos << 1 | 1, mid + 1, high)
        a = self.maxima[pos << 1]
        b = self.maxima[pos << 1 | 1]
        self.maxima[pos] = a if a >= b else b

    def suffix_max(self, start, pos=1, low=1, high=0):
        if high == 0:
            high = self.n
        if start <= low:
            return self.maxima[pos]
        self._down(pos)
        mid = (low + high) >> 1
        ans = self.suffix_max(start, pos << 1 | 1, mid + 1, high)
        if start <= mid:
            got = self.suffix_max(start, pos << 1, low, mid)
            if got > ans:
                ans = got
        return ans

def check(m, entries, zeros, colors):
    if m == 0:
        return True
    if colors < m or zeros < 2 * m:
        return False
    ranges = [[] for _ in range(m + 2)]
    for positions in entries:
        p = 0
        s = m + 1
        found = False
        for z in positions:
            if m <= z <= zeros - m:
                found = True
                break
            if z < m:
                p = z if z > p else p
            else:
                value = z - zeros + m + 1
                s = value if value < s else s
        if not found and p + 1 <= s - 1:
            ranges[p + 1].append(s - 1)
    seg = Segment(m)
    for left, ends in enumerate(ranges[1:], 1):
        if left > m:
            break
        for right in ends:
            seg.add_prefix(right)
        if seg.suffix_max(left) > colors + left - 1:
            return False
    return True

def solve_case(a):
    zeros = 0
    index = {}
    entries = []
    for x in a:
        if x == 0:
            zeros += 1
        else:
            pos = index.get(x)
            if pos is None:
                index[x] = len(entries)
                entries.append([])
                pos = index[x]
            entries[pos].append(zeros)
    colors = len(entries)
    lo = 0
    hi = min(colors, zeros // 2)
    while lo != hi:
        mid = (lo + hi + 1) >> 1
        if check(mid, entries, zeros, colors):
            lo = mid
        else:
            hi = mid - 1
    return lo

# CLAUSE: finish_program
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    vals = [int(x) for x in data]
    t = vals[0]
    ptr = 1
    out = []
    for _ in range(t):
        n = vals[ptr]
        ptr += 1
        out.append(str(solve_case(vals[ptr:ptr + n])))
        ptr += n
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
