# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    pts = []
    for s in data[1:1 + n]:
        b = s.count('B')
        nn = len(s) - b
        pts.append((b, nn, b - nn))

    def get_point(r):
        xl, xr = 0, 10**18
        yl, yr = 0, 10**18
        dl, dr = -10**18, 10**18

        for b, nn, diff in pts:
            xl = max(xl, b - r)
            xr = min(xr, b + r)
            yl = max(yl, nn - r)
            yr = min(yr, nn + r)
            dl = max(dl, diff - r)
            dr = min(dr, diff + r)

        if xl > xr or yl > yr or dl > dr:
            return None

        dl = max(dl, xl - yr)
        dr = min(dr, xr - yl)
        if dl > dr:
            return None

        candidates = [dl, dr]
        if dl <= 0 <= dr:
            candidates.append(0)

        for d in candidates:
            lx = max(xl, yl + d)
            rx = min(xr, yr + d)
            if lx <= rx:
                x = lx
                if d == 0 and x == 0 and rx >= 1:
                    x = 1
                y = x - d
                if x >= 0 and y >= 0 and x + y > 0:
                    return x, y

        return None

    lo, hi = 0, 1
    while get_point(hi) is None:
        hi *= 2

    while lo < hi:
        mid = (lo + hi) // 2
        if get_point(mid) is not None:
            hi = mid
        else:
            lo = mid + 1

    x, y = get_point(lo)
    print(lo)
    print('B' * x + 'N' * y)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
