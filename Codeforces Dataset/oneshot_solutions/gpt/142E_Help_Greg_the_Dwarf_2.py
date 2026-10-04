import sys
import math

data = list(map(float, sys.stdin.read().split()))
r, h = data[0], data[1]
pts = [data[2:5], data[5:8]]

pi = math.pi
twopi = 2.0 * pi
L = math.hypot(r, h)
alpha = r / L
eps = 1e-8


def norm_angle(x):
    x = (x + pi) % twopi - pi
    return x


def make_point(p):
    x, y, z = p
    rho = math.hypot(x, y)
    phi = math.atan2(y, x)
    if phi < 0:
        phi += twopi
    s = L * (h - z) / h
    if s < 0 and s > -1e-7:
        s = 0.0
    if s > L and s < L + 1e-7:
        s = L
    on_base = abs(z) <= eps
    on_side = abs(rho - r * (h - z) / h) <= 1e-7
    return {
        "x": x,
        "y": y,
        "z": z,
        "rho": rho,
        "phi": phi,
        "s": s,
        "base": on_base,
        "side": on_side,
    }


A = make_point(pts[0])
B = make_point(pts[1])
ans = float("inf")


def base_dist_to_rim(P, q):
    return math.sqrt(max(0.0, P["rho"] * P["rho"] + r * r - 2.0 * P["rho"] * r * math.cos(norm_angle(q - P["phi"]))))


def rim_chord(a, b):
    return 2.0 * r * abs(math.sin(norm_angle(a - b) * 0.5))


def side_to_rim(P, q):
    ang = alpha * norm_angle(q - P["phi"])
    return math.sqrt(max(0.0, P["s"] * P["s"] + L * L - 2.0 * P["s"] * L * math.cos(ang)))


def side_between(P, Q):
    ang = alpha * norm_angle(Q["phi"] - P["phi"])
    return math.sqrt(max(0.0, P["s"] * P["s"] + Q["s"] * Q["s"] - 2.0 * P["s"] * Q["s"] * math.cos(ang)))


def minimize_1d(f):
    n = 720
    step = twopi / n
    vals = [f(i * step) for i in range(n)]
    best = min(vals)
    for i in range(n):
        if vals[i] <= vals[(i - 1) % n] and vals[i] <= vals[(i + 1) % n]:
            lo = i * step - step
            hi = i * step + step
            for _ in range(90):
                m1 = lo + (hi - lo) / 3.0
                m2 = hi - (hi - lo) / 3.0
                if f(m1 % twopi) < f(m2 % twopi):
                    hi = m2
                else:
                    lo = m1
            best = min(best, f(((lo + hi) * 0.5) % twopi))
    return best


def side_base(Pbase, Qside):
    return minimize_1d(lambda q: base_dist_to_rim(Pbase, q) + side_to_rim(Qside, q))


def side_side_via_base(P, Q):
    def f(a, b):
        return side_to_rim(P, a) + rim_chord(a, b) + side_to_rim(Q, b)

    best = float("inf")
    starts = []
    m = 18
    for i in range(m):
        for j in range(m):
            a = twopi * i / m
            b = twopi * j / m
            starts.append((f(a, b), a, b))
    for a in (P["phi"], Q["phi"], (P["phi"] + Q["phi"]) * 0.5):
        for b in (P["phi"], Q["phi"], (P["phi"] + Q["phi"]) * 0.5):
            starts.append((f(a % twopi, b % twopi), a % twopi, b % twopi))

    starts.sort(key=lambda x: x[0])
    for _, a, b in starts[:80]:
        cur = f(a, b)
        step = twopi / 8.0
        while step > 1e-10:
            improved = False
            best_a, best_b, best_v = a, b, cur
            for da in (-step, 0.0, step):
                for db in (-step, 0.0, step):
                    if da == 0.0 and db == 0.0:
                        continue
                    na = (a + da) % twopi
                    nb = (b + db) % twopi
                    v = f(na, nb)
                    if v < best_v:
                        best_a, best_b, best_v = na, nb, v
            if best_v < cur:
                a, b, cur = best_a, best_b, best_v
                improved = True
            if not improved:
                step *= 0.5
        best = min(best, cur)
    return best


if A["base"] and B["base"]:
    ans = min(ans, math.hypot(A["x"] - B["x"], A["y"] - B["y"]))

if A["side"] and B["side"]:
    ans = min(ans, side_between(A, B))
    ans = min(ans, side_side_via_base(A, B))

if A["base"] and B["side"]:
    ans = min(ans, side_base(A, B))

if B["base"] and A["side"]:
    ans = min(ans, side_base(B, A))

print("{:.9f}".format(ans))
