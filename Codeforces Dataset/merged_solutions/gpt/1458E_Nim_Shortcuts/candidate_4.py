# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from bisect import bisect_left

    INF = 10 ** 30
    seed_value = 123456789123456789


    class Node:
        __slots__ = ("l", "r", "p", "left", "right")

        def __init__(self, l, r, p):
            self.l = l
            self.r = r
            self.p = p
            self.left = None
            self.right = None


    def priority():
        global seed_value
        seed_value = (seed_value + 0x9E3779B97F4A7C15) & ((1 << 64) - 1)
        z = seed_value
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & ((1 << 64) - 1)
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & ((1 << 64) - 1)
        return z ^ (z >> 31)


    def merge(a, b):
        if a is None or b is None:
            return a or b
        if a.p < b.p:
            a.right = merge(a.right, b)
            return a
        b.left = merge(a, b.left)
        return b


    def split(t, key):
        if t is None:
            return None, None
        if t.l < key:
            a, b = split(t.right, key)
            t.right = a
            return t, b
        a, b = split(t.left, key)
        t.left = b
        return a, t


    class IntervalSet:
        def __init__(self, query_columns):
            self.root = Node(0, INF, priority())
            self.cols = sorted(query_columns)
            self.count = len(self.cols)
            self.parent = list(range(self.count + 1))
            self.column_time = {}

        def find(self, x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def assign_range(self, left, right, base):
            i = self.find(bisect_left(self.cols, left))
            while i < self.count and self.cols[i] <= right:
                value = self.cols[i]
                self.column_time[value] = base + value
                self.parent[i] = self.find(i + 1)
                i = self.parent[i]

        def assign_point(self, value, row):
            i = bisect_left(self.cols, value)
            if i < self.count and self.cols[i] == value and self.find(i) == i:
                self.column_time[value] = row
                self.parent[i] = self.find(i + 1)

        def insert(self, left, right):
            if left > right:
                return
            node = Node(left, right, priority())
            a, b = split(self.root, left)
            self.root = merge(merge(a, node), b)

        def delete_key(self, key):
            a, b = split(self.root, key)
            c, d = split(b, key + 1)
            self.root = merge(a, d)

        def predecessor(self, value):
            t = self.root
            result = None
            while t is not None:
                if t.l <= value:
                    result = t
                    t = t.right
                else:
                    t = t.left
            return result

        def leftmost(self):
            t = self.root
            while t.left is not None:
                t = t.left
            return t

        def min_value(self):
            return self.leftmost().l

        def remove_point(self, value, row):
            node = self.predecessor(value)
            if node is None or node.r < value:
                return
            left, right = node.l, node.r
            self.delete_key(left)
            self.insert(left, value - 1)
            self.insert(value + 1, right)
            self.assign_point(value, row)

        def remove_prefix(self, amount, start_row):
            done = 0
            while amount > 0:
                node = self.leftmost()
                left, right = node.l, node.r
                length = right - left + 1
                if length <= amount:
                    self.delete_key(left)
                    self.assign_range(left, right, start_row + done - left)
                    amount -= length
                    done += length
                else:
                    self.delete_key(left)
                    self.insert(left + amount, right)
                    self.assign_range(left, left + amount - 1, start_row + done - left)
                    break


    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        ptr = 0
        n = data[ptr]
        m = data[ptr + 1]
        ptr += 2

        shortcuts_by_row = {}
        shortcut_min = {}
        shortcut_set = set()

        for _ in range(n):
            x = data[ptr]
            y = data[ptr + 1]
            ptr += 2
            shortcut_set.add((x, y))
            shortcuts_by_row.setdefault(x, []).append(y)
            if y < shortcut_min.get(x, INF):
                shortcut_min[x] = y

        queries = []
        query_rows = set()
        query_columns = set()

        for _ in range(m):
            a = data[ptr]
            b = data[ptr + 1]
            ptr += 2
            queries.append((a, b))
            query_rows.add(a)
            query_columns.add(b)

        intervals = IntervalSet(query_columns)
        row_first = {}
        current_row = 0

        for row in sorted(set(shortcuts_by_row) | query_rows):
            if row > current_row:
                intervals.remove_prefix(row - current_row, current_row)

            mex = intervals.min_value()
            forced = shortcut_min.get(row, INF)

            if row in query_rows:
                row_first[row] = mex if mex < forced else forced

            if mex < forced:
                intervals.remove_point(mex, row)

            for col in shortcuts_by_row.get(row, ()):
                intervals.remove_point(col, row)

            current_row = row + 1

        out = []
        for a, b in queries:
            if (a, b) in shortcut_set:
                out.append("LOSE")
            elif row_first[a] < b or intervals.column_time.get(b, INF) < a:
                out.append("WIN")
            else:
                out.append("LOSE")

        sys.stdout.write("\n".join(out))


    if __name__ == "__main__":
        sys.setrecursionlimit(1_000_000)
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
