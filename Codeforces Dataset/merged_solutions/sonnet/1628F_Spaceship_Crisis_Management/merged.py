# Clause setup_environment [Confidence: 0.80]
import sys
import heapq
from math import gcd
from bisect import bisect_left, bisect_right

EPS = 1e-10


# Clause solve_logic [Confidence: 1.00]
def norm_dir(x, y):
    g = gcd(abs(x), abs(y))
    return x // g, y // g

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    n = data[p]
    p += 1

    segments = []
    directions = set()
    for _ in range(n):
        ax, ay, bx, by = data[p], data[p + 1], data[p + 2], data[p + 3]
        p += 4
        segments.append((ax, ay, bx, by))
        directions.add(norm_dir(ax, ay))
        directions.add(norm_dir(bx, by))

    q = data[p]
    p += 1
    queries = []
    for _ in range(q):
        x, y = data[p], data[p + 1]
        p += 2
        queries.append((x, y))
        directions.add(norm_dir(x, y))

    answer = [False] * q

    for ux, uy in directions:
        starts = []
        y_values = {0}

        for ax, ay, bx, by in segments:
            x1 = ux * ax + uy * ay
            y1 = ux * ay - uy * ax
            x2 = ux * bx + uy * by
            y2 = ux * by - uy * bx
            if x2 < x1:
                x1, y1, x2, y2 = x2, y2, x1, y1
            starts.append((x1, y1, x2, y2))
            y_values.add(y1)
            y_values.add(y2)

        events = []
        for i, (x, y) in enumerate(queries):
            tx = ux * x + uy * y
            ty = ux * y - uy * x
            y_values.add(ty)
            if tx >= 0:
                events.append((tx, ty, i))

        y_list = sorted(y_values)
        y_id = {v: i for i, v in enumerate(y_list)}
        reachable = [False] * len(y_list)
        reachable[y_id[0]] = True

        starts.sort()
        events.sort()
        xs = sorted(set([x for x, _, _ in events] + [x for x, _, _, _ in starts]))
        heap = []
        si = 0
        ei = 0

        def flush(limit):
            while heap and heap[0][0] <= limit + EPS:
                _, pos, val = heapq.heappop(heap)
                reachable[pos] = val

        for cur in xs:
            flush(cur)

            while si < len(starts) and starts[si][0] == cur:
                x1, y1, x2, y2 = starts[si]
                si += 1
                active = x2 - x1 > abs(y2 - y1) and reachable[y_id[y1]]
                lo, hi = sorted((y1, y2))
                left = bisect_left(y_list, lo)
                right = bisect_right(y_list, hi)

                if y1 == y2:
                    for pos in range(left, right):
                        heapq.heappush(heap, (float(x1), pos, active))
                else:
                    for pos in range(left, right):
                        yy = y_list[pos]
                        cross = x1 + (x2 - x1) * (yy - y1) / (y2 - y1)
                        if cross >= cur - EPS:
                            heapq.heappush(heap, (cross, pos, active))

            flush(cur)

            while ei < len(events) and events[ei][0] == cur:
                _, ty, qi = events[ei]
                ei += 1
                if reachable[y_id[ty]]:
                    answer[qi] = True

    sys.stdout.write("\n".join("YES" if v else "NO" for v in answer))


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


