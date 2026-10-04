# CLAUSE: setup_environment
import sys
from bisect import bisect_left, bisect_right

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
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        if r < l:
            return 0
        left = bisect_left(cols, l)
        right = bisect_right(cols, r) - 1
        if right < left:
            return 0
        return self.sum(right) - (self.sum(left - 1) if left else 0)


data = list(map(int, sys.stdin.buffer.read().split()))
p = 0
n = data[p]
m = data[p + 1]
p += 2

by_row = {}
shortcuts = set()
all_cols = []
for _ in range(n):
    x = data[p]
    y = data[p + 1]
    p += 2
    shortcuts.add((x, y))
    by_row.setdefault(x, []).append(y)
    all_cols.append(y)

queries = []
events = set(by_row)
for i in range(m):
    a = data[p]
    b = data[p + 1]
    p += 2
    queries.append((a, b))
    events.add(a)

cols = sorted(set(all_cols))
fenwick = Fenwick(len(cols))
active = set()

for x in by_row:
    by_row[x].sort()

def kth_unblocked(start, kth):
    lo = start
    hi = start + kth + len(cols) + 5
    while lo < hi:
        mid = (lo + hi) // 2
        blocked = fenwick.range_sum(start, mid)
        free = mid - start + 1 - blocked
        if free >= kth:
            hi = mid
        else:
            lo = mid + 1
    return lo

queries_by_row = {}
for i, item in enumerate(queries):
    queries_by_row.setdefault(item[0], []).append((i, item[1]))

answers = [None] * m
mex = 0
previous = -1

for row in sorted(events):
    if row > previous + 1:
        mex = kth_unblocked(mex, row - previous)
    first_shortcut = by_row[row][0] if row in by_row else None
    generated = mex if first_shortcut is None or mex < first_shortcut else None

    for idx, col in queries_by_row.get(row, []):
        if (row, col) in shortcuts or col == generated:
            answers[idx] = "LOSE"
        else:
            answers[idx] = "WIN"

    if generated is not None:
        mex = kth_unblocked(mex, 2)

    for col in by_row.get(row, []):
        if col not in active:
            active.add(col)
            fenwick.add(bisect_left(cols, col), 1)

    mex = kth_unblocked(mex, 1)
    previous = row

# CLAUSE: finish_program
sys.stdout.write("\n".join(answers))
