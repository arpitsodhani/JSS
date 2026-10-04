# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MAXC = 10 ** 6

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)

    def add(self, i, v):
        i += 1
        n = self.n + 1
        while i <= n:
            self.bit[i] += v
            i += i & -i

    def sum(self, i):
        if i < 0:
            return 0
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        if l > r:
            return 0
        return self.sum(r) - self.sum(l - 1)


def count_intersections(horiz, vert):
    events = []
    queries = []

    for y, x1, x2 in horiz:
        events.append((x1, 0, y))
        events.append((x2 + 1, 2, y))

    for x, y1, y2 in vert:
        queries.append((x, y1, y2))

    events.sort()
    queries.sort()

    fw = Fenwick(MAXC + 1)
    ans = 0
    p = 0

    for x, y1, y2 in queries:
        while p < len(events) and events[p][0] <= x:
            _, typ, y = events[p]
            if typ == 0:
                fw.add(y, 1)
            else:
                fw.add(y, -1)
            p += 1
        ans += fw.range_sum(y1, y2)

    return ans


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    idx = 2

    horizontals = []
    verticals = []
    full_h = 0
    full_v = 0

    for _ in range(n):
        y, x1, x2 = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        horizontals.append((y, x1, x2))
        if x1 == 0 and x2 == MAXC:
            full_h += 1

    for _ in range(m):
        x, y1, y2 = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        verticals.append((x, y1, y2))
        if y1 == 0 and y2 == MAXC:
            full_v += 1

    intersections = count_intersections(horizontals, verticals)
    print(intersections + full_h + full_v + 1)


if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
