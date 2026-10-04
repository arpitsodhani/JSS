# CLAUSE: setup_environment
import sys
from math import gcd
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right

EPS = 1e-10

# CLAUSE: solve_logic
def direction(x, y):
    d = gcd(abs(x), abs(y))
    return x // d, y // d

def rotate_point(u, v, x, y):
    return u * x + v * y, u * y - v * x

def solve_for_direction(u, v, segments, queries, answer):
    y_values = {0}
    starts = []

    for a, b, c, d in segments:
        x1, y1 = rotate_point(u, v, a, b)
        x2, y2 = rotate_point(u, v, c, d)
        if x2 < x1:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        starts.append((x1, y1, x2, y2))
        y_values.add(y1)
        y_values.add(y2)

    asks = []
    for qi, (x, y) in enumerate(queries):
        tx, ty = rotate_point(u, v, x, y)
        y_values.add(ty)
        if tx >= 0:
            asks.append((tx, ty, qi))

    ys = sorted(y_values)
    where = {y: i for i, y in enumerate(ys)}
    good = [False] * len(ys)
    good[where[0]] = True

    by_start = {}
    for item in starts:
        by_start.setdefault(item[0], []).append(item)

    by_query = {}
    for item in asks:
        by_query.setdefault(item[0], []).append(item)

    heap = []
    for cur in sorted(set(by_start) | set(by_query)):
        while heap and heap[0][0] <= cur + EPS:
            _, yi, value = heappop(heap)
            good[yi] = value

        for x1, y1, x2, y2 in by_start.get(cur, ()):
            can_continue = x2 - x1 > abs(y2 - y1) and good[where[y1]]
            low = y1 if y1 < y2 else y2
            high = y2 if y1 < y2 else y1
            l = bisect_left(ys, low)
            r = bisect_right(ys, high)

            if y1 == y2:
                for yi in range(l, r):
                    heappush(heap, (float(x1), yi, can_continue))
            else:
                inv = 1.0 / (y2 - y1)
                length = x2 - x1
                for yi in range(l, r):
                    cross = x1 + length * (ys[yi] - y1) * inv
                    if cross >= cur - EPS:
                        heappush(heap, (cross, yi, can_continue))

        while heap and heap[0][0] <= cur + EPS:
            _, yi, value = heappop(heap)
            good[yi] = value

        for _, ty, qi in by_query.get(cur, ()):
            if good[where[ty]]:
                answer[qi] = True

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    i = 0
    n = nums[i]
    i += 1

    segments = []
    dirs = set()
    for _ in range(n):
        ax, ay, bx, by = nums[i], nums[i + 1], nums[i + 2], nums[i + 3]
        i += 4
        segments.append((ax, ay, bx, by))
        dirs.add(direction(ax, ay))
        dirs.add(direction(bx, by))

    q = nums[i]
    i += 1
    queries = []
    for _ in range(q):
        x, y = nums[i], nums[i + 1]
        i += 2
        queries.append((x, y))
        dirs.add(direction(x, y))

    answer = [False] * q
    for u, v in dirs:
        solve_for_direction(u, v, segments, queries, answer)

    sys.stdout.write("\n".join(("YES" if x else "NO") for x in answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
