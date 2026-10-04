# CLAUSE: setup_environment
import sys
import math
from bisect import bisect_left

values = sys.stdin.buffer.read().split()
n = int(values[0])
k = int(values[1])
vectors = []
at_origin = 0
for i in range(n):
    px = int(values[2 * i + 2])
    py = int(values[2 * i + 3])
    if px == 0 and py == 0:
        at_origin += 1
    else:
        vectors.append((math.atan2(py, px), math.hypot(px, py)))

two_pi = 2.0 * math.pi

# CLAUSE: solve_logic
def can(radius):
    target = k - at_origin
    if target <= 0:
        return True
    if radius <= 0.0:
        return False
    arcs = []
    bound = radius * 2.0 + 1e-10
    for angle, distance in vectors:
        if distance <= bound:
            spread = math.acos(min(1.0, distance / (radius * 2.0)))
            start = (angle - spread) % two_pi
            finish = (angle + spread) % two_pi
            if start <= finish:
                arcs.append((start, finish))
            else:
                arcs.append((start, finish + two_pi))
                arcs.append((start - two_pi, finish))
    if len(arcs) < target:
        return False
    lefts = sorted(a for a, b in arcs)
    rights = sorted(b for a, b in arcs)
    checks = lefts
    for angle in checks:
        active = bisect_left(lefts, angle + 1e-15) - bisect_left(rights, angle - 1e-15)
        if active >= target:
            return True
    return False

lo = 0.0
hi = 200000.0
for _ in range(90):
    mid = (lo + hi) / 2.0
    if can(mid):
        hi = mid
    else:
        lo = mid

# CLAUSE: finish_program
sys.stdout.write(f"{hi:.10f}\n")
