# CLAUSE: setup_environment
import sys
from array import array

def ceil_div(a, b):
    return -((-a) // b)

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pts = []
    at = 1
    for _ in range(n):
        pts.append((data[at], data[at + 1]))
        at += 2

    mn = min(x for x, y in pts)
    mx = max(x for x, y in pts)
    off = -mn
    w = mx - mn + 1
    inf = 10 ** 18
    low = array("q", [inf]) * w
    high = array("q", [-inf]) * w

    for i, (x1, y1) in enumerate(pts):
        x2, y2 = pts[(i + 1) % n]
        if x1 == x2:
            p = x1 + off
            if y1 > y2:
                y1, y2 = y2, y1
            if y1 < low[p]:
                low[p] = y1
            if y2 > high[p]:
                high[p] = y2
        else:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            dx = x2 - x1
            dy = y2 - y1
            for x in range(x1, x2 + 1):
                num = y1 * dx + dy * (x - x1)
                p = x + off
                a = ceil_div(num, dx)
                b = num // dx
                if a < low[p]:
                    low[p] = a
                if b > high[p]:
                    high[p] = b

    cnt = sx = sy = ss = 0
    for p in range(w):
        lo = low[p]
        hi = high[p]
        if lo <= hi:
            x = p - off
            c = hi - lo + 1
            k = c - 1
            col_sum = (lo + hi) * c // 2
            col_sq = c * lo * lo + lo * c * k + k * c * (2 * k + 1) // 6
            cnt += c
            sx += x * c
            sy += col_sum
            ss += x * x * c + col_sq

    ans = (cnt * ss - sx * sx - sy * sy) / (cnt * (cnt - 1))
    sys.stdout.write("{:.10f}\n".format(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
