# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import math

        data = list(map(float, sys.stdin.read().split()))
        xp, yp, vp = data[0], data[1], data[2]
        x, y, v, r = data[3], data[4], data[5], data[6]

        R = math.hypot(xp, yp)
        start_dist = math.hypot(x, y)
        theta0 = math.atan2(yp, xp)
        omega = vp / R

        def angle_diff(a, b):
            d = abs(a - b)
            if d > math.pi:
                d = 2.0 * math.pi - d
            return d

        def shortest_path_to(px, py):
            bdist = R
            phi = angle_diff(math.atan2(y, x), math.atan2(py, px))
            clear_limit = math.acos(r / start_dist) + math.acos(r / bdist)

            if phi <= clear_limit + 1e-15:
                dx = x - px
                dy = y - py
                return math.hypot(dx, dy)

            tangent1 = math.sqrt(start_dist * start_dist - r * r)
            tangent2 = math.sqrt(bdist * bdist - r * r)
            arc = r * (phi - clear_limit)
            return tangent1 + tangent2 + arc

        def can(t):
            ang = theta0 + omega * t
            px = R * math.cos(ang)
            py = R * math.sin(ang)
            return shortest_path_to(px, py) <= v * t

        lo = 0.0
        hi = 1.0
        while not can(hi):
            hi *= 2.0

        for _ in range(100):
            mid = (lo + hi) / 2.0
            if can(mid):
                hi = mid
            else:
                lo = mid

        print("{:.9f}".format(hi))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
