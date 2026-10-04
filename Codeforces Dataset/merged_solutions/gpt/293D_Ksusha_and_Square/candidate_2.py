import sys

# CLAUSE: derive_pair_moment_formula
def sums_i(n):
    a = n * (n - 1) // 2
    return a, n * (n - 1) * (2 * n - 1) // 6, a * a

def fl(n, m, a, b):
    if n <= 0:
        return 0, 0, 0, 0, 0, 0
    da, a = divmod(a, m)
    db, b = divmod(b, m)
    z0, z2, zx, z3, zx2, zxq = fl_inner(n, m, a, b)
    s1, s2, s3 = sums_i(n)
    p0 = da * s1 + db * n + z0
    px = da * s2 + db * s1 + zx
    p2 = da * da * s2 + db * db * n + z2 + 2 * da * db * s1 + 2 * da * zx + 2 * db * z0
    px2 = da * s3 + db * s2 + zx2
    p3 = da ** 3 * s3 + db ** 3 * n + z3 + 3 * da * da * db * s2 + 3 * da * da * zx2 + 3 * db * db * da * s1 + 3 * db * db * z0 + 6 * da * db * zx + 3 * da * zxq + 3 * db * z2
    pxq = da * da * s3 + db * db * s1 + zxq + 2 * da * db * s2 + 2 * da * zx2 + 2 * db * zx
    return p0, p2, px, p3, px2, pxq

def fl_inner(n, m, a, b):
    if a == 0 or n <= 0:
        return 0, 0, 0, 0, 0, 0
    top = (a * n + b) // m
    if top == 0:
        return 0, 0, 0, 0, 0, 0
    c, c2, tc, c3, t2c, tc2 = fl(top, a, m, m - b + a - 1)
    s1, s2, _ = sums_i(n)
    v0 = n * top - c
    vx = top * s1 - (c2 - c) // 2
    yc = tc + c
    yyc = t2c + 2 * tc + c
    v2 = n * top * top - 2 * yc + c
    v3 = n * top ** 3 - 3 * yyc + 3 * yc - c
    vx2 = top * s2 - (2 * c3 - 3 * c2 + c) // 6
    vxq = top * top * s1 - (2 * tc2 + c2 - 2 * tc - c) // 2
    return v0, v2, vx, v3, vx2, vxq

# CLAUSE: normalize_convex_polygon
def signed_area(p):
    s = 0
    for a, b in zip(p, p[1:] + p[:1]):
        s += a[0] * b[1] - a[1] * b[0]
    return s

def bad(a, b, c):
    return (b[0] - a[0]) * (c[1] - b[1]) == (b[1] - a[1]) * (c[0] - b[0])

def canonical(points):
    v = []
    for p in points:
        if len(v) == 0 or v[-1] != p:
            v.append(p)
    if len(v) > 1 and v[0] == v[-1]:
        v.pop()
    again = True
    while again:
        again = False
        w = []
        for k in range(len(v)):
            if len(v) > 2 and bad(v[k - 1], v[k], v[(k + 1) % len(v)]):
                again = True
            else:
                w.append(v[k])
        v = w
    if signed_area(v) < 0:
        v = v[::-1]
    return v

# CLAUSE: split_monotone_chains
def make_boundaries(v):
    down, up = [], []
    for k in range(len(v)):
        x, y = v[k]
        X, Y = v[(k + 1) % len(v)]
        if x == X:
            continue
        if x < X:
            down.append((x, X, y, Y))
        else:
            up.append((X, x, Y, y))
    down.sort(key=lambda e: (e[0], e[1]))
    up.sort(key=lambda e: (e[0], e[1]))
    return down, up

# CLAUSE: advance_edge_windows
def edge_expr(e):
    l, r, y0, y1 = e
    dx = r - l
    dy = y1 - y0
    return dy, y0 * dx - dy * l, dx

def floor_line(a, b, d, l, r):
    n = r - l + 1
    f0, f2, kf, f3, k2f, _ = fl(n, d, a, a * l + b)
    return f0, f2, l * f0 + kf, f3, l * l * f0 + 2 * l * kf + k2f

# CLAUSE: evaluate_floor_sum_blocks
def lower_prefix(a, b, d, l, r):
    n = r - l + 1
    g0, g2, xg, g3, x2g = floor_line(-a, -b, d, l, r)
    xs = (l + r) * n // 2
    xs2 = r * (r + 1) * (2 * r + 1) // 6 - (l - 1) * l * (2 * l - 1) // 6
    return -g0 - n, g2 + 2 * g0 + n, -xg - xs, -g3 - 3 * g2 - 3 * g0 - n, -x2g - xs2

# CLAUSE: accumulate_lattice_moments
def collect(v):
    lo, hi = make_boundaries(v)
    left = min(x for x, _ in v)
    right = max(x for x, _ in v)
    p = q = 0
    x = left
    npt = ax = ay = ax2 = ay2 = 0
    while x <= right:
        while lo[p][1] < x:
            p += 1
        while hi[q][1] < x:
            q += 1
        end = min(lo[p][1], hi[q][1], right)
        la, lb, ld = edge_expr(lo[p])
        ua, ub, ud = edge_expr(hi[q])
        u0, u2, ux, u3, ux2 = floor_line(ua, ub, ud, x, end)
        l0, l2, lx, l3, lx2 = lower_prefix(la, lb, ld, x, end)
        npt += u0 - l0
        ax += ux - lx
        ax2 += ux2 - lx2
        ay += (u2 + u0 - l2 - l0) // 2
        ay2 += (2 * u3 + 3 * u2 + u0 - 2 * l3 - 3 * l2 - l0) // 6
        x = end + 1
    return npt, ax, ay, ax2, ay2

# CLAUSE: finalize_expected_area
def solve():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    polygon = canonical([(raw[i], raw[i + 1]) for i in range(1, 2 * n + 1, 2)])
    cnt, sx, sy, sx2, sy2 = collect(polygon)
    if cnt <= 1:
        print("0.0000000000")
    else:
        num = cnt * (sx2 + sy2) - sx * sx - sy * sy
        print("%.10f" % (num / (cnt * (cnt - 1))))

solve()
