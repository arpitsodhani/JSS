# CLAUSE: setup_environment
import sys
from bisect import bisect_right

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    it = iter(raw)
    n = int(next(it))
    m = int(next(it))

    factors = []
    for _ in range(n):
        a = int(next(it))
        h = int(next(it))
        left = int(next(it))
        right = int(next(it))

        if left != 100:
            q = (100 - left) / 100.0
            factors.append((a - h, 0, q))
            factors.append((a, 1, q))

        if right != 100:
            q = (100 - right) / 100.0
            factors.append((a + 1, 0, q))
            factors.append((a + h + 1, 1, q))

    mushrooms = [(int(next(it)), int(next(it))) for _ in range(m)]
    mushrooms.sort()

    points = sorted(set([x for x, _ in mushrooms] + [x for x, _, _ in factors]))
    pos = {x: i for i, x in enumerate(points)}
    changes = [[] for _ in points]

    for x, typ, q in factors:
        changes[pos[x]].append((typ, q))

    ans = 0.0
    cur = 1.0
    mi = 0
    mm = len(mushrooms)

    for x in points:
        for typ, q in changes[pos[x]]:
            if typ == 0:
                cur *= q
            else:
                cur /= q
        while mi < mm and mushrooms[mi][0] == x:
            ans += mushrooms[mi][1] * cur
            mi += 1
        if mi < mm:
            nxt = mushrooms[mi][0]
            jump = bisect_right(points, x)
            if jump < len(points) and points[jump] > nxt:
                continue

    print("{:.10f}".format(ans))

# CLAUSE: finish_program
main()
