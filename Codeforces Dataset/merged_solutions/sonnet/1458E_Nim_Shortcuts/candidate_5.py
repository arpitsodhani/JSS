# CLAUSE: setup_environment
import sys
import bisect

# CLAUSE: solve_logic
class Solver:
    def __init__(self, data):
        self.data = data
        self.ptr = 0
        self.n = self.take()
        self.m = self.take()
        self.rows = {}
        self.shortcut = set()
        self.columns = []
        self.queries = []
        self.query_rows = {}
        self.events = set()
        self.answer = []

    def take(self):
        value = self.data[self.ptr]
        self.ptr += 1
        return value

    def read(self):
        for _ in range(self.n):
            x = self.take()
            y = self.take()
            self.shortcut.add((x, y))
            self.rows.setdefault(x, []).append(y)
            self.columns.append(y)
        self.events.update(self.rows)
        for i in range(self.m):
            x = self.take()
            y = self.take()
            self.queries.append((x, y))
            self.query_rows.setdefault(x, []).append((i, y))
            self.events.add(x)
        for x in self.rows:
            self.rows[x].sort()
        self.columns = sorted(set(self.columns))
        self.answer = ["WIN"] * self.m
        self.bit = [0] * (len(self.columns) + 1)
        self.marked = set()

    def add_column(self, y):
        if y in self.marked:
            return
        self.marked.add(y)
        i = bisect.bisect_left(self.columns, y) + 1
        while i <= len(self.columns):
            self.bit[i] += 1
            i += i & -i

    def pref(self, i):
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s

    def blocked(self, left, right):
        l = bisect.bisect_left(self.columns, left)
        r = bisect.bisect_right(self.columns, right)
        return self.pref(r) - self.pref(l)

    def free_at(self, start, count):
        low = start
        high = start + count + len(self.columns) + 4
        while low < high:
            mid = (low + high) // 2
            if mid - start + 1 - self.blocked(start, mid) >= count:
                high = mid
            else:
                low = mid + 1
        return low

    def run(self):
        self.read()
        mex = 0
        previous = -1
        for row in sorted(self.events):
            mex = self.free_at(mex, row - previous)
            limits = self.rows.get(row, [])
            generated = mex if not limits or mex < limits[0] else None

            for idx, col in self.query_rows.get(row, []):
                if (row, col) in self.shortcut or col == generated:
                    self.answer[idx] = "LOSE"

            if generated is not None:
                mex = self.free_at(mex, 2)

            for col in limits:
                self.add_column(col)

            mex = self.free_at(mex, 1)
            previous = row
        return "\n".join(self.answer)

# CLAUSE: finish_program
values = list(map(int, sys.stdin.buffer.read().split()))
sys.stdout.write(Solver(values).run())
