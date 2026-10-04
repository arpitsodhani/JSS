# Clause setup_environment [Confidence: 0.60]
import math
import sys


# Clause solve_logic [Confidence: 0.60]
def solve():
    values = list(map(float, sys.stdin.read().split()))
    r, h = values[0], values[1]
    x1, y1, z1 = values[2], values[3], values[4]
    x2, y2, z2 = values[5], values[6], values[7]

    rho1 = math.hypot(x1, y1)
    rho2 = math.hypot(x2, y2)
    phi1 = math.atan2(y1, x1)
    phi2 = math.atan2(y2, x2)

    length = math.hypot(r, h)
    angle = 2.0 * math.pi * r / length

    def cone_distance(s1, t1, s2, t2):
        best = float("inf")
        for k in range(-10, 11):
            delta = t2 - t1 + k * angle
            cand = math.sqrt(max(0.0, s1 * s1 + s2 * s2 - 2.0 * s1 * s2 * math.cos(delta)))
            if cand < best:
                best = cand
        return best

    s1 = (h - z1) * length / h
    s2 = (h - z2) * length / h
    t1 = phi1 * angle / (2.0 * math.pi)
    t2 = phi2 * angle / (2.0 * math.pi)

    answer = cone_distance(s1, t1, s2, t2)
    answer = min(answer, cone_distance(s1, t1, (h + z2) * length / h, t2))
    answer = min(answer, cone_distance((h + z1) * length / h, t1, s2, t2))

    eps = 1e-9
    if z1 < eps and rho1 < r - eps:
        for i in range(360):
            phi = -math.pi + 2.0 * math.pi * i / 360.0
            bx = r * math.cos(phi)
            by = r * math.sin(phi)
            bt = phi * angle / (2.0 * math.pi)
            answer = min(answer, math.hypot(x1 - bx, y1 - by) + cone_distance(length, bt, s2, t2))

    if z2 < eps and rho2 < r - eps:
        for i in range(360):
            phi = -math.pi + 2.0 * math.pi * i / 360.0
            bx = r * math.cos(phi)
            by = r * math.sin(phi)
            bt = phi * angle / (2.0 * math.pi)
            answer = min(answer, math.hypot(x2 - bx, y2 - by) + cone_distance(s1, t1, length, bt))

    if z1 < eps and z2 < eps:
        answer = min(answer, math.hypot(x1 - x2, y1 - y2))

    sys.stdout.write(f"{answer:.9f}")


# Clause finish_program [Confidence: 0.60]
solve()


