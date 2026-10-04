import sys
from math import ceil, floor
from array import array

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pts = [(data[i], data[i + 1]) for i in range(1, 2 * n + 1, 2)]

    minx = min(x for x, _ in pts)
    maxx = max(x for x, _ in pts)
    w = maxx - minx + 1

    inf = 1e100
    low = array('d', [inf]) * w
    high = array('d', [-inf]) * w

    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]

        if x1 == x2:
            idx = x1 - minx
            a = y1 if y1 < y2 else y2
            b = y2 if y1 < y2 else y1
            if a < low[idx]:
                low[idx] = a
            if b > high[idx]:
                high[idx] = b
        else:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            dx = x2 - x1
            dy = y2 - y1
            for x in range(x1, x2 + 1):
                idx = x - minx
                y = y1 + dy * (x - x1) / dx
                if y < low[idx]:
                    low[idx] = y
                if y > high[idx]:
                    high[idx] = y

    def pref_sq(t):
        return t * (t + 1) * (2 * t + 1) // 6

    cnt = 0
    sx = 0
    sy = 0
    s2 = 0
    eps = 1e-9

    for idx in range(w):
        if low[idx] == inf:
            continue

        a = ceil(low[idx] - eps)
        b = floor(high[idx] + eps)
        if a > b:
            continue

        c = b - a + 1
        x = idx + minx
        sum_y = (a + b) * c // 2
        sum_y2 = pref_sq(b) - pref_sq(a - 1)

        cnt += c
        sx += x * c
        sy += sum_y
        s2 += x * x * c + sum_y2

    ans = (cnt * s2 - sx * sx - sy * sy) / (cnt * (cnt - 1))
    print("{:.10f}".format(ans))

if __name__ == "__main__":
    main()
