# CLAUSE: setup_environment
import math
import sys

# CLAUSE: solve_logic
def solve():
    data = tuple(float(x) for x in sys.stdin.read().split())
    radius, height = data[0], data[1]
    first = data[2], data[3], data[4]
    second = data[5], data[6], data[7]

    slant = math.sqrt(radius * radius + height * height)
    full = 2.0 * math.pi
    sector = full * radius / slant
    turn = sector / full

    def surface(point, reflected=False):
        x, y, z = point
        if reflected:
            z = -z
        return ((height - z) * slant / height, math.atan2(y, x) * turn)

    def spread(u, v):
        su, au = u
        sv, av = v
        return min(
            math.sqrt(max(0.0, su * su + sv * sv - 2.0 * su * sv * math.cos(av - au + sector * k)))
            for k in range(-10, 11)
        )

    a = surface(first)
    b = surface(second)
    answer = min(spread(a, b), spread(a, surface(second, True)), spread(surface(first, True), b))

    step = full / 360.0
    eps = 1e-9

    def boundary_options(inner, outer, reverse):
        x, y, z = inner
        best = float("inf")
        for i in range(360):
            phi = -math.pi + step * i
            rim_point = (slant, phi * turn)
            base_part = math.hypot(x - radius * math.cos(phi), y - radius * math.sin(phi))
            if reverse:
                value = spread(outer, rim_point) + base_part
            else:
                value = base_part + spread(rim_point, outer)
            if value < best:
                best = value
        return best

    x1, y1, z1 = first
    x2, y2, z2 = second

    if z1 < eps and math.hypot(x1, y1) < radius - eps:
        answer = min(answer, boundary_options(first, b, False))

    if z2 < eps and math.hypot(x2, y2) < radius - eps:
        answer = min(answer, boundary_options(second, a, True))

    if z1 < eps and z2 < eps:
        answer = min(answer, math.hypot(x1 - x2, y1 - y2))

    sys.stdout.write("{:.9f}\n".format(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
