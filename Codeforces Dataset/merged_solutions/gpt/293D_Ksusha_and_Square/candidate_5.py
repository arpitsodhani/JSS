import sys

# CLAUSE: derive_pair_moment_formula
def sigma(n):
    s1 = n * (n - 1) // 2
    return s1, n * (n - 1) * (2 * n - 1) // 6, s1 * s1

def floor_pack(n, m, a, b):
    if n <= 0:
        return (0, 0, 0, 0, 0, 0)
    aq, ar = divmod(a, m)
    bq, br = divmod(b, m)
    w0, w2, wx, w3, wx2, wx22 = reduced_pack(n, m, ar, br)
    s1, s2, s3 = sigma(n)
    return (
        aq * s1 + bq * n + w0,
        aq * aq * s2 + bq * bq * n + w2 + 2 * aq * bq * s1 + 2 * aq * wx + 2 * bq * w0,
        aq * s2 + bq * s1 + wx,
        aq ** 3 * s3 + bq ** 3 * n + w3 + 3 * aq * aq * bq * s2 + 3 * aq * aq * wx2 + 3 * bq * bq * aq * s1 + 3 * bq * bq * w0 + 6 * aq * bq * wx + 3 * aq * wx22 + 3 * bq * w2,
        aq * s3 + bq * s2 + wx2,
        aq * aq * s3 + bq * bq * s1 + wx22 + 2 * aq * bq * s2 + 2 * aq * wx2 + 2 * bq * wx,
    )

def reduced_pack(n, m, a, b):
    if a == 0:
        return (0, 0, 0, 0, 0, 0)
    ymax = (a * n + b) // m
    if ymax == 0:
        return (0, 0, 0, 0, 0, 0)
    c = floor_pack(ymax, a, m, m - b + a - 1)
    s1, s2, _ = sigma(n)
    c0, c2, jc, c3, j2c, jc2 = c
    yc = jc + c0
    y2c = j2c + 2 * jc + c0
    return (
        n * ymax - c0,
        n * ymax * ymax - (2 * yc - c0),
        ymax * s1 - (c2 - c0) // 2,
        n * ymax ** 3 - (3 * y2c - 3 * yc + c0),
        ymax * s2 - (2 * c3 - 3 * c2 + c0) // 6,
        ymax * ymax * s1 - (2 * jc2 + c2 - 2 * jc - c0) // 2,
    )

# CLAUSE: normalize_convex_polygon
def twice_area(p):
    ans = 0
    for i in range(len(p)):
        ans += p[i][0] * p[(i + 1) % len(p)][1] - p[(i + 1) % len(p)][0] * p[i][1]
    return ans

def normalize_vertices(p):
    v = []
    for item in p:
        if not v or item != v[-1]:
            v.append(item)
    if v[0] == v[-1]:
        v.pop()
    while True:
        nxt = []
        dropped = False
        for i in range(len(v)):
            a, b, c = v[i - 1], v[i], v[(i + 1) % len(v)]
            z = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
            if z == 0:
                dropped = True
            else:
                nxt.append(b)
        v = nxt
        if not dropped:
            break
    if twice_area(v) < 0:
        v.reverse()
    return v

# CLAUSE: split_monotone_chains
def boundary_lists(p):
    lo = []
    hi = []
    for i in range(len(p)):
        x0, y0 = p[i]
        x1, y1 = p[(i + 1) % len(p)]
        if x0 < x1:
            lo.append((x0, x1, y0, y1, x1 - x0, y1 - y0))
        elif x0 > x1:
            hi.append((x1, x0, y1, y0, x0 - x1, y0 - y1))
    lo.sort()
    hi.sort()
    return lo, hi

# CLAUSE: advance_edge_windows
def next_windows(p):
    lo, hi = boundary_lists(p)
    start = min(x for x, y in p)
    finish = max(x for x, y in p)
    li = ui = 0
    pos = start
    while pos <= finish:
        while lo[li][1] < pos:
            li += 1
        while hi[ui][1] < pos:
            ui += 1
        last = min(finish, lo[li][1], hi[ui][1])
        yield pos, last, lo[li], hi[ui]
        pos = last + 1

# CLAUSE: evaluate_floor_sum_blocks
def unpack_edge(e):
    x0, x1, y0, y1, dx, dy = e
    return dy, y0 * dx - dy * x0, dx

def floor_interval(a, b, d, l, r):
    n = r - l + 1
    z0, z2, zk, z3, zk2, zkq = floor_pack(n, d, a, a * l + b)
    return z0, z2, l * z0 + zk, z3, l * l * z0 + 2 * l * zk + zk2

def ceil_minus_interval(a, b, d, l, r):
    n = r - l + 1
    q0, q2, qx, q3, qx2 = floor_interval(-a, -b, d, l, r)
    sx = n * (l + r) // 2
    sx2 = r * (r + 1) * (2 * r + 1) // 6 - (l - 1) * l * (2 * l - 1) // 6
    return -q0 - n, q2 + 2 * q0 + n, -qx - sx, -q3 - 3 * q2 - 3 * q0 - n, -qx2 - sx2

# CLAUSE: accumulate_lattice_moments
def scan_moments(p):
    count = sumx = sumy = sumx2 = sumy2 = 0
    for l, r, low, up in next_windows(p):
        la, lb, ld = unpack_edge(low)
        ua, ub, ud = unpack_edge(up)
        hi0, hi2, hix, hi3, hix2 = floor_interval(ua, ub, ud, l, r)
        lo0, lo2, lox, lo3, lox2 = ceil_minus_interval(la, lb, ld, l, r)
        count += hi0 - lo0
        sumx += hix - lox
        sumy += (hi2 + hi0 - lo2 - lo0) // 2
        sumx2 += hix2 - lox2
        sumy2 += (2 * hi3 + 3 * hi2 + hi0 - 2 * lo3 - 3 * lo2 - lo0) // 6
    return count, sumx, sumy, sumx2, sumy2

# CLAUSE: finalize_expected_area
def run():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    p = [(data[2 * i + 1], data[2 * i + 2]) for i in range(n)]
    p = normalize_vertices(p)
    cnt, sx, sy, sx2, sy2 = scan_moments(p)
    if cnt < 2:
        print("0.0000000000")
        return
    numerator = cnt * (sx2 + sy2) - sx * sx - sy * sy
    denominator = cnt * (cnt - 1)
    print("{:.10f}".format(numerator / denominator))

run()
