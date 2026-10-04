# CLAUSE: setup_environment
import sys
import math

data = sys.stdin.buffer.read().split()
n = int(data[0])
k = int(data[1])
points = []
zero_count = 0
for i in range(n):
    x = int(data[2 + 2 * i])
    y = int(data[3 + 2 * i])
    if x == 0 and y == 0:
        zero_count += 1
    else:
        points.append((x, y, math.hypot(x, y), math.atan2(y, x)))

tau = 2.0 * math.pi
eps = 1e-12

# CLAUSE: solve_logic
def possible(radius):
    if zero_count >= k:
        return True
    if radius <= 0.0:
        return False
    events = []
    limit = 2.0 * radius + 1e-10
    for x, y, dist, angle in points:
        if dist > limit:
            continue
        half = math.acos(min(1.0, dist / (2.0 * radius)))
        left = angle - half
        right = angle + half
        while left < 0.0:
            left += tau
            right += tau
        while left >= tau:
            left -= tau
            right -= tau
        if right >= tau:
            events.append((left, 1))
            events.append((tau, -1))
            events.append((0.0, 1))
            events.append((right - tau, -1))
        else:
            events.append((left, 1))
            events.append((right, -1))
    events.sort(key=lambda item: (item[0], -item[1]))
    covered = zero_count
    for _, delta in events:
        covered += delta
        if covered >= k:
            return True
    return False

lo = 0.0
hi = 200000.0
for _ in range(90):
    mid = (lo + hi) * 0.5
    if possible(mid):
        hi = mid
    else:
        lo = mid

# CLAUSE: finish_program
print(f"{hi:.10f}")
