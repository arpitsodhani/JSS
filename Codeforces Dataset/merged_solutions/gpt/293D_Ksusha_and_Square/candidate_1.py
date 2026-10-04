import sys

# CLAUSE: derive_pair_moment_formula
def pref(n):
    return n * (n - 1) // 2, n * (n - 1) * (2 * n - 1) // 6, (n * (n - 1) // 2) ** 2

def floor_stats(n, mod, aa, bb):
    if n <= 0:
        return (0, 0, 0, 0, 0, 0)
    qa, a = divmod(aa, mod)
    qb, b = divmod(bb, mod)
    h0, h2, hx, h3, hx2, hxh2 = floor_core(n, mod, a, b)
    s1, s2, s3 = pref(n)
    r0 = qa * s1 + qb * n + h0
    r2 = qa * qa * s2 + qb * qb * n + h2 + 2 * qa * qb * s1 + 2 * qa * hx + 2 * qb * h0
    rx = qa * s2 + qb * s1 + hx
    r3 = qa ** 3 * s3 + qb ** 3 * n + h3 + 3 * qa * qa * qb * s2 + 3 * qa * qa * hx2 + 3 * qb * qb * qa * s1 + 3 * qb * qb * h0 + 6 * qa * qb * hx + 3 * qa * hxh2 + 3 * qb * h2
    rx2 = qa * s3 + qb * s2 + hx2
    rxf2 = qa * qa * s3 + qb * qb * s1 + hxh2 + 2 * qa * qb * s2 + 2 * qa * hx2 + 2 * qb * hx
    return r0, r2, rx, r3, rx2, rxf2

def floor_core(n, mod, a, b):
    if n <= 0 or a == 0:
        return (0, 0, 0, 0, 0, 0)
    y = (a * n + b) // mod
    if y == 0:
        return (0, 0, 0, 0, 0, 0)
    c0, c2, jc, c3, j2c, jc2 = floor_stats(y, a, mod, mod - b + a - 1)
    si, si2, _ = pref(n)
    s0 = n * y - c0
    sx = y * si - (c2 - c0) // 2
    yc = jc + c0
    y2c = j2c + 2 * jc + c0
    s2 = n * y * y - (2 * yc - c0)
    s3 = n * y ** 3 - (3 * y2c - 3 * yc + c0)
    sx2 = y * si2 - (2 * c3 - 3 * c2 + c0) // 6
    sxf2 = y * y * si - (2 * jc2 + c2 - 2 * jc - c0) // 2
    return s0, s2, sx, s3, sx2, sxf2

# CLAUSE: normalize_convex_polygon
def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])

def normalize(poly):
    q = []
    for p in poly:
        if not q or q[-1] != p:
            q.append(p)
    if len(q) > 1 and q[0] == q[-1]:
        q.pop()
    changed = True
    while changed and len(q) > 2:
        changed = False
        r = []
        m = len(q)
        for i in range(m):
            if cross(q[i - 1], q[i], q[(i + 1) % m]) != 0:
                r.append(q[i])
            else:
                changed = True
        q = r
    area = 0
    for i in range(len(q)):
        x1, y1 = q[i]
        x2, y2 = q[(i + 1) % len(q)]
        area += x1 * y2 - x2 * y1
    if area < 0:
        q.reverse()
    return q

# CLAUSE: split_monotone_chains
def chains(poly):
    low, high = [], []
    m = len(poly)
    for i in range(m):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % m]
        if x1 == x2:
            continue
        if x1 < x2:
            low.append((x1, x2, y1, y2, x2 - x1, y2 - y1))
        else:
            high.append((x2, x1, y2, y1, x1 - x2, y1 - y2))
    low.sort()
    high.sort()
    return low, high

# CLAUSE: advance_edge_windows
def line_moments(a, b, d, l, r):
    n = r - l + 1
    s0, s2, sk, s3, sk2, _ = floor_stats(n, d, a, a * l + b)
    sx = l * s0 + sk
    sx2 = l * l * s0 + 2 * l * sk + sk2
    return n, s0, s2, sx, s3, sx2

def below_moments(a, b, d, l, r):
    n, g0, g2, xg, g3, x2g = line_moments(-a, -b, d, l, r)
    sx = (l + r) * n // 2
    sx2 = r * (r + 1) * (2 * r + 1) // 6 - (l - 1) * l * (2 * l - 1) // 6
    return n, -g0 - n, g2 + 2 * g0 + n, -xg - sx, -g3 - 3 * g2 - 3 * g0 - n, -x2g - sx2

# CLAUSE: evaluate_floor_sum_blocks
def segment_parts(seg):
    xl, xr, yl, yr, dx, dy = seg
    return dy, yl * dx - dy * xl, dx

# CLAUSE: accumulate_lattice_moments
def accumulate(poly):
    lower, upper = chains(poly)
    minx = min(x for x, _ in poly)
    maxx = max(x for x, _ in poly)
    i = j = 0
    x = minx
    cnt = sx = sy = sx2 = sy2 = 0
    while x <= maxx:
        while i + 1 < len(lower) and lower[i][1] < x:
            i += 1
        while j + 1 < len(upper) and upper[j][1] < x:
            j += 1
        r = min(lower[i][1], upper[j][1], maxx)
        la, lb, ld = segment_parts(lower[i])
        ua, ub, ud = segment_parts(upper[j])
        n, u0, u2, xu, u3, x2u = line_moments(ua, ub, ud, x, r)
        _, m0, m2, xm, m3, x2m = below_moments(la, lb, ld, x, r)
        add = u0 - m0
        cnt += add
        sx += xu - xm
        sx2 += x2u - x2m
        sy += ((u2 + u0) - (m2 + m0)) // 2
        sy2 += ((2 * u3 + 3 * u2 + u0) - (2 * m3 + 3 * m2 + m0)) // 6
        x = r + 1
    return cnt, sx, sy, sx2, sy2

# CLAUSE: finalize_expected_area
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    pts = [(data[i], data[i + 1]) for i in range(1, 2 * n + 1, 2)]
    poly = normalize(pts)
    total, sumx, sumy, sumx2, sumy2 = accumulate(poly)
    if total < 2:
        print("0.0000000000")
        return
    dist = total * (sumx2 + sumy2) - sumx * sumx - sumy * sumy
    print("{:.10f}".format(dist / (total * (total - 1))))

if __name__ == "__main__":
    main()
