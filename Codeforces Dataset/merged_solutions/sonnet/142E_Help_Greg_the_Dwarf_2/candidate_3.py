# CLAUSE: setup_environment
from math import atan2, cos, hypot, pi, sqrt
import sys

# CLAUSE: solve_logic
def wrapped_distance(a, b, sector):
    s1, t1 = a
    s2, t2 = b
    best = 1e100
    k = -10
    while k <= 10:
        dtheta = t2 - t1 + sector * k
        value = s1 * s1 + s2 * s2 - 2.0 * s1 * s2 * cos(dtheta)
        if value < 0.0 and value > -1e-8:
            value = 0.0
        d = sqrt(value)
        if d < best:
            best = d
        k += 1
    return best

def solve():
    raw = sys.stdin.buffer.read().split()
    nums = [float(item) for item in raw]
    r, h = nums[:2]
    p = nums[2:5]
    q = nums[5:8]

    slant = hypot(r, h)
    sector = 2.0 * pi * r / slant
    scale = sector / (2.0 * pi)

    def projected(point, sign):
        x, y, z = point
        return ((h - sign * z) * slant / h, atan2(y, x) * scale)

    p_on = projected(p, 1.0)
    q_on = projected(q, 1.0)
    p_ref = projected(p, -1.0)
    q_ref = projected(q, -1.0)

    answer = min(
        wrapped_distance(p_on, q_on, sector),
        wrapped_distance(p_on, q_ref, sector),
        wrapped_distance(p_ref, q_on, sector),
    )

    eps = 1e-9
    px, py, pz = p
    qx, qy, qz = q
    pr = hypot(px, py)
    qr = hypot(qx, qy)

    def try_base_from(point, other):
        x, y, z = point
        best = 1e100
        for i in range(360):
            phi = -pi + i * (2.0 * pi / 360.0)
            rim = (slant, phi * scale)
            flat = hypot(x - r * cos(phi), y - r * __import__("math").sin(phi))
            total = flat + wrapped_distance(rim, other, sector)
            if total < best:
                best = total
        return best

    if pz < eps and pr < r - eps:
        answer = min(answer, try_base_from(p, q_on))

    if qz < eps and qr < r - eps:
        x, y, z = q
        best = 1e100
        for i in range(360):
            phi = -pi + i * (2.0 * pi / 360.0)
            rim = (slant, phi * scale)
            flat = hypot(x - r * cos(phi), y - r * __import__("math").sin(phi))
            total = wrapped_distance(p_on, rim, sector) + flat
            if total < best:
                best = total
        answer = min(answer, best)

    if pz < eps and qz < eps:
        answer = min(answer, hypot(px - qx, py - qy))

    print(f"{answer:.9f}")

# CLAUSE: finish_program
solve()
