# CLAUSE: setup_environment
import sys
from math import gcd
from heapq import heappush, heappop

EPS = 1e-10

# CLAUSE: solve_logic
def canonical(x, y):
    g = gcd(abs(x), abs(y))
    return x // g, y // g

def lower_bound(a, x):
    left = 0
    right = len(a)
    while left < right:
        mid = (left + right) >> 1
        if a[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(a, x):
    left = 0
    right = len(a)
    while left < right:
        mid = (left + right) >> 1
        if a[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

def transformed_segment(u, v, seg):
    ax, ay, bx, by = seg
    x1 = u * ax + v * ay
    y1 = u * ay - v * ax
    x2 = u * bx + v * by
    y2 = u * by - v * bx
    if x2 < x1:
        return x2, y2, x1, y1
    return x1, y1, x2, y2

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    n = data[at]
    at += 1

    segments = []
    directions = set()
    for _ in range(n):
        seg = (data[at], data[at + 1], data[at + 2], data[at + 3])
        at += 4
        segments.append(seg)
        directions.add(canonical(seg[0], seg[1]))
        directions.add(canonical(seg[2], seg[3]))

    q = data[at]
    at += 1
    queries = []
    for _ in range(q):
        x, y = data[at], data[at + 1]
        at += 2
        queries.append((x, y))
        directions.add(canonical(x, y))

    ok = [False] * q

    for u, v in directions:
        starts = []
        queries_here = []
        all_y = {0}

        for seg in segments:
            item = transformed_segment(u, v, seg)
            starts.append(item)
            all_y.add(item[1])
            all_y.add(item[3])

        for qi, point in enumerate(queries):
            x, y = point
            tx = u * x + v * y
            ty = u * y - v * x
            all_y.add(ty)
            if tx >= 0:
                queries_here.append((tx, ty, qi))

        starts.sort(key=lambda z: z[0])
        queries_here.sort(key=lambda z: z[0])
        y_axis = sorted(all_y)
        y_index = {y: i for i, y in enumerate(y_axis)}
        reachable = [False for _ in y_axis]
        reachable[y_index[0]] = True

        xs = []
        last = None
        for x1, _, _, _ in starts:
            if last != x1:
                xs.append(x1)
                last = x1
        for tx, _, _ in queries_here:
            if tx not in y_index:
                pass
        scan_x = sorted(set(xs + [tx for tx, _, _ in queries_here]))

        heap = []
        si = 0
        qi = 0
        ns = len(starts)
        nq = len(queries_here)

        for current in scan_x:
            while heap and heap[0][0] <= current + EPS:
                _, yi, val = heappop(heap)
                reachable[yi] = val

            while si < ns and starts[si][0] == current:
                x1, y1, x2, y2 = starts[si]
                si += 1
                active = reachable[y_index[y1]] and x2 - x1 > abs(y2 - y1)

                if y1 < y2:
                    low, high = y1, y2
                else:
                    low, high = y2, y1

                left = lower_bound(y_axis, low)
                right = upper_bound(y_axis, high)

                if y1 == y2:
                    exit_x = float(x1)
                    for yi in range(left, right):
                        heappush(heap, (exit_x, yi, active))
                else:
                    dx = x2 - x1
                    dy = y2 - y1
                    for yi in range(left, right):
                        yv = y_axis[yi]
                        exit_x = x1 + dx * (yv - y1) / dy
                        if exit_x >= current - EPS:
                            heappush(heap, (exit_x, yi, active))

            while heap and heap[0][0] <= current + EPS:
                _, yi, val = heappop(heap)
                reachable[yi] = val

            while qi < nq and queries_here[qi][0] == current:
                _, ty, original = queries_here[qi]
                qi += 1
                if reachable[y_index[ty]]:
                    ok[original] = True

    out = ["NO"] * q
    for i, value in enumerate(ok):
        if value:
            out[i] = "YES"
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
