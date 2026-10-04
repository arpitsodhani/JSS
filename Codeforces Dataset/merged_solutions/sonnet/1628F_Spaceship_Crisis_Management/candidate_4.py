# CLAUSE: setup_environment
import sys
import heapq
from math import gcd
from bisect import bisect_left, bisect_right

EPS = 1e-10

# CLAUSE: solve_logic
def norm(x, y):
    g = gcd(abs(x), abs(y))
    return x // g, y // g

def main():
    arr = list(map(int, sys.stdin.buffer.read().split()))
    k = 0
    n = arr[k]
    k += 1

    segs = []
    dirs = set()
    for _ in range(n):
        a = arr[k]
        b = arr[k + 1]
        c = arr[k + 2]
        d = arr[k + 3]
        k += 4
        segs.append((a, b, c, d))
        dirs.add(norm(a, b))
        dirs.add(norm(c, d))

    q = arr[k]
    k += 1
    qs = []
    for _ in range(q):
        x = arr[k]
        y = arr[k + 1]
        k += 2
        qs.append((x, y))
        dirs.add(norm(x, y))

    ans = [0] * q

    for u, v in dirs:
        ys = [0]
        line_events = []
        query_events = []

        for ax, ay, bx, by in segs:
            x1 = u * ax + v * ay
            y1 = u * ay - v * ax
            x2 = u * bx + v * by
            y2 = u * by - v * bx
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            line_events.append((x1, y1, x2, y2))
            ys.append(y1)
            ys.append(y2)

        for qi in range(q):
            sx, sy = qs[qi]
            tx = u * sx + v * sy
            ty = u * sy - v * sx
            ys.append(ty)
            if tx >= 0:
                query_events.append((tx, ty, qi))

        ys = sorted(set(ys))
        pos_of = {value: pos for pos, value in enumerate(ys)}
        state = bytearray(len(ys))
        state[pos_of[0]] = 1

        timeline = {}
        for seg in line_events:
            timeline.setdefault(seg[0], [[], []])[0].append(seg)
        for qry in query_events:
            timeline.setdefault(qry[0], [[], []])[1].append(qry)

        heap = []
        for x in sorted(timeline):
            while heap and heap[0][0] <= x + EPS:
                _, y_index, value = heapq.heappop(heap)
                state[y_index] = value

            starts, checks = timeline[x]
            for x1, y1, x2, y2 in starts:
                value = 1 if x2 - x1 > abs(y2 - y1) and state[pos_of[y1]] else 0
                if y1 <= y2:
                    lo, hi = y1, y2
                else:
                    lo, hi = y2, y1
                left = bisect_left(ys, lo)
                right = bisect_right(ys, hi)

                if y1 == y2:
                    for j in range(left, right):
                        heapq.heappush(heap, (float(x1), j, value))
                else:
                    dx = x2 - x1
                    dy = y2 - y1
                    for j in range(left, right):
                        cross = x1 + dx * (ys[j] - y1) / dy
                        if cross >= x - EPS:
                            heapq.heappush(heap, (cross, j, value))

            while heap and heap[0][0] <= x + EPS:
                _, y_index, value = heapq.heappop(heap)
                state[y_index] = value

            for _, ty, qi in checks:
                if state[pos_of[ty]]:
                    ans[qi] = 1

    sys.stdout.write("\n".join("YES" if x else "NO" for x in ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
