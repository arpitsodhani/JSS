import sys

# CLAUSE: derive_pair_moment_formula
def base(n):
    s = n * (n - 1) // 2
    return s, n * (n - 1) * (2 * n - 1) // 6, s * s

def stat_floor(n, m, a, b):
    if n <= 0:
        return [0, 0, 0, 0, 0, 0]
    qa, ra = divmod(a, m)
    qb, rb = divmod(b, m)
    h = pure_floor(n, m, ra, rb)
    si, sii, siii = base(n)
    ans = [0] * 6
    ans[0] = qa * si + qb * n + h[0]
    ans[1] = qa * qa * sii + qb * qb * n + h[1] + 2 * qa * qb * si + 2 * qa * h[2] + 2 * qb * h[0]
    ans[2] = qa * sii + qb * si + h[2]
    ans[3] = qa ** 3 * siii + qb ** 3 * n + h[3] + 3 * qa * qa * qb * sii + 3 * qa * qa * h[4] + 3 * qb * qb * qa * si + 3 * qb * qb * h[0] + 6 * qa * qb * h[2] + 3 * qa * h[5] + 3 * qb * h[1]
    ans[4] = qa * siii + qb * sii + h[4]
    ans[5] = qa * qa * siii + qb * qb * si + h[5] + 2 * qa * qb * sii + 2 * qa * h[4] + 2 * qb * h[2]
    return ans

def pure_floor(n, m, a, b):
    if n == 0 or a == 0:
        return [0, 0, 0, 0, 0, 0]
    y = (a * n + b) // m
    if y == 0:
        return [0, 0, 0, 0, 0, 0]
    c0, c2, jc, c3, j2c, jc2 = stat_floor(y, a, m, m - b + a - 1)
    si, sii, _ = base(n)
    r0 = n * y - c0
    rx = y * si - (c2 - c0) // 2
    r2 = n * y * y - (2 * (jc + c0) - c0)
    r3 = n * y ** 3 - (3 * (j2c + 2 * jc + c0) - 3 * (jc + c0) + c0)
    rx2 = y * sii - (2 * c3 - 3 * c2 + c0) // 6
    rxq = y * y * si - (2 * jc2 + c2 - 2 * jc - c0) // 2
    return [r0, r2, rx, r3, rx2, rxq]

# CLAUSE: normalize_convex_polygon
def orient(poly):
    z = 0
    m = len(poly)
    for i in range(m):
        z += poly[i][0] * poly[(i + 1) % m][1] - poly[(i + 1) % m][0] * poly[i][1]
    return z

def clean_polygon(poly):
    a = []
    for x in poly:
        if not a or a[-1] != x:
            a.append(x)
    if a and a[0] == a[-1]:
        a.pop()
    while True:
        b = []
        cut = 0
        m = len(a)
        for i in range(m):
            p, q, r = a[i - 1], a[i], a[(i + 1) % m]
            if (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0]) == 0:
                cut += 1
            else:
                b.append(q)
        a = b
        if cut == 0:
            break
    if orient(a) < 0:
        a.reverse()
    return a

# CLAUSE: split_monotone_chains
def split(poly):
    bottom = []
    top = []
    m = len(poly)
    for i in range(m):
        x0, y0 = poly[i]
        x1, y1 = poly[(i + 1) % m]
        if x0 < x1:
            bottom.append((x0, x1, y0, y1, x1 - x0, y1 - y0))
        elif x0 > x1:
            top.append((x1, x0, y1, y0, x0 - x1, y0 - y1))
    return sorted(bottom), sorted(top)

# CLAUSE: advance_edge_windows
def current_ranges(poly):
    bottom, top = split(poly)
    lx = min(x for x, y in poly)
    rx = max(x for x, y in poly)
    i = j = 0
    x = lx
    while x <= rx:
        while bottom[i][1] < x:
            i += 1
        while top[j][1] < x:
            j += 1
        y = min(bottom[i][1], top[j][1], rx)
        yield x, y, bottom[i], top[j]
        x = y + 1

# CLAUSE: evaluate_floor_sum_blocks
def coeff(e):
    x0, x1, y0, y1, d, a = e
    return a, y0 * d - a * x0, d

def moments_floor(a, b, d, l, r):
    n = r - l + 1
    f0, f2, kf, f3, k2f, kf2 = stat_floor(n, d, a, a * l + b)
    return f0, f2, l * f0 + kf, f3, l * l * f0 + 2 * l * kf + k2f

def moments_low_minus(a, b, d, l, r):
    n = r - l + 1
    f0, f2, xf, f3, x2f = moments_floor(-a, -b, d, l, r)
    sx = (l + r) * n // 2
    sx2 = r * (r + 1) * (2 * r + 1) // 6 - (l - 1) * l * (2 * l - 1) // 6
    return -f0 - n, f2 + 2 * f0 + n, -xf - sx, -f3 - 3 * f2 - 3 * f0 - n, -x2f - sx2

# CLAUSE: accumulate_lattice_moments
def lattice_moments(poly):
    n = sx = sy = sx2 = sy2 = 0
    for l, r, lo, up in current_ranges(poly):
        la, lb, ld = coeff(lo)
        ua, ub, ud = coeff(up)
        a0, a2, ax, a3, ax2 = moments_floor(ua, ub, ud, l, r)
        b0, b2, bx, b3, bx2 = moments_low_minus(la, lb, ld, l, r)
        n += a0 - b0
        sx += ax - bx
        sx2 += ax2 - bx2
        sy += (a2 + a0 - b2 - b0) // 2
        sy2 += (2 * a3 + 3 * a2 + a0 - 2 * b3 - 3 * b2 - b0) // 6
    return n, sx, sy, sx2, sy2

# CLAUSE: finalize_expected_area
def main():
    arr = list(map(int, sys.stdin.buffer.read().split()))
    n = arr[0]
    p = clean_polygon([(arr[2 * i + 1], arr[2 * i + 2]) for i in range(n)])
    c, x, y, xx, yy = lattice_moments(p)
    if c < 2:
        ans = 0.0
    else:
        ans = (c * (xx + yy) - x * x - y * y) / (c * (c - 1))
    print("{:.10f}".format(ans))

main()
