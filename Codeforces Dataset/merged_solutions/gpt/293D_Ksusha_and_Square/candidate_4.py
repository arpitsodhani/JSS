import sys

# CLAUSE: derive_pair_moment_formula
def pow_sums(n):
    one = n * (n - 1) // 2
    two = n * (n - 1) * (2 * n - 1) // 6
    return one, two, one * one

def fs_all(n, m, a, b):
    if n <= 0:
        return (0, 0, 0, 0, 0, 0)
    q, a = divmod(a, m)
    r, b = divmod(b, m)
    g0, g2, gx, g3, gx2, gxq = fs_small(n, m, a, b)
    s1, s2, s3 = pow_sums(n)
    v0 = q * s1 + r * n + g0
    v2 = q * q * s2 + r * r * n + g2 + 2 * q * r * s1 + 2 * q * gx + 2 * r * g0
    vx = q * s2 + r * s1 + gx
    v3 = q ** 3 * s3 + r ** 3 * n + g3 + 3 * q * q * r * s2 + 3 * q * q * gx2 + 3 * r * r * q * s1 + 3 * r * r * g0 + 6 * q * r * gx + 3 * q * gxq + 3 * r * g2
    vx2 = q * s3 + r * s2 + gx2
    vxq = q * q * s3 + r * r * s1 + gxq + 2 * q * r * s2 + 2 * q * gx2 + 2 * r * gx
    return v0, v2, vx, v3, vx2, vxq

def fs_small(n, m, a, b):
    if a == 0:
        return (0, 0, 0, 0, 0, 0)
    y = (a * n + b) // m
    if y == 0:
        return (0, 0, 0, 0, 0, 0)
    t0, t2, kt, t3, k2t, kt2 = fs_all(y, a, m, m - b + a - 1)
    s1, s2, _ = pow_sums(n)
    yct = kt + t0
    yyct = k2t + 2 * kt + t0
    return (
        n * y - t0,
        n * y * y - 2 * yct + t0,
        y * s1 - (t2 - t0) // 2,
        n * y ** 3 - 3 * yyct + 3 * yct - t0,
        y * s2 - (2 * t3 - 3 * t2 + t0) // 6,
        y * y * s1 - (2 * kt2 + t2 - 2 * kt - t0) // 2,
    )

# CLAUSE: normalize_convex_polygon
def area2(v):
    return sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))

def normalize_convex_polygon(v):
    u = []
    for p in v:
        if not u or p != u[-1]:
            u.append(p)
    if len(u) > 1 and u[0] == u[-1]:
        u.pop()
    while len(u) > 2:
        keep = []
        removed = False
        for i in range(len(u)):
            a, b, c = u[i - 1], u[i], u[(i + 1) % len(u)]
            if (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]):
                keep.append(b)
            else:
                removed = True
        u = keep
        if not removed:
            break
    if area2(u) < 0:
        u.reverse()
    return u

# CLAUSE: split_monotone_chains
def split_monotone_chains(v):
    a = []
    b = []
    for p, q in zip(v, v[1:] + v[:1]):
        if p[0] == q[0]:
            continue
        if p[0] < q[0]:
            a.append((p[0], q[0], p[1], q[1]))
        else:
            b.append((q[0], p[0], q[1], p[1]))
    return sorted(a), sorted(b)

# CLAUSE: advance_edge_windows
def windows(v):
    a, b = split_monotone_chains(v)
    x = min(p[0] for p in v)
    stop = max(p[0] for p in v)
    i = j = 0
    while x <= stop:
        if a[i][1] < x:
            i += 1
            continue
        if b[j][1] < x:
            j += 1
            continue
        y = min(a[i][1], b[j][1], stop)
        yield x, y, a[i], b[j]
        x = y + 1

# CLAUSE: evaluate_floor_sum_blocks
def line_data(e):
    x0, x1, y0, y1 = e
    d = x1 - x0
    a = y1 - y0
    return a, y0 * d - a * x0, d

def eval_floor(a, b, d, l, r):
    n = r - l + 1
    z = fs_all(n, d, a, a * l + b)
    return z[0], z[1], l * z[0] + z[2], z[3], l * l * z[0] + 2 * l * z[2] + z[4]

def eval_ceil_minus_one(a, b, d, l, r):
    n = r - l + 1
    q0, q2, qx, q3, qx2 = eval_floor(-a, -b, d, l, r)
    xs = n * (l + r) // 2
    xs2 = r * (r + 1) * (2 * r + 1) // 6 - (l - 1) * l * (2 * l - 1) // 6
    return -q0 - n, q2 + 2 * q0 + n, -qx - xs, -q3 - 3 * q2 - 3 * q0 - n, -qx2 - xs2

# CLAUSE: accumulate_lattice_moments
def accumulate_lattice_moments(v):
    total = [0, 0, 0, 0, 0]
    for l, r, lo, hi in windows(v):
        la, lb, ld = line_data(lo)
        ha, hb, hd = line_data(hi)
        u0, u2, ux, u3, ux2 = eval_floor(ha, hb, hd, l, r)
        d0, d2, dx, d3, dx2 = eval_ceil_minus_one(la, lb, ld, l, r)
        total[0] += u0 - d0
        total[1] += ux - dx
        total[2] += (u2 + u0 - d2 - d0) // 2
        total[3] += ux2 - dx2
        total[4] += (2 * u3 + 3 * u2 + u0 - 2 * d3 - 3 * d2 - d0) // 6
    return total

# CLAUSE: finalize_expected_area
def main():
    z = list(map(int, sys.stdin.buffer.read().split()))
    n = z[0]
    v = normalize_convex_polygon([(z[i], z[i + 1]) for i in range(1, 2 * n + 1, 2)])
    c, sx, sy, sx2, sy2 = accumulate_lattice_moments(v)
    ans = 0.0 if c < 2 else (c * (sx2 + sy2) - sx * sx - sy * sy) / (c * (c - 1))
    sys.stdout.write("{:.10f}\n".format(ans))

main()
