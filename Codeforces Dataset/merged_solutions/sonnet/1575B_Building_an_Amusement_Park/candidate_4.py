# CLAUSE: setup_environment
import sys
import math

raw = sys.stdin.buffer.read().split()
n = int(raw[0])
k = int(raw[1])
items = []
base = 0
for pos in range(n):
    x = int(raw[2 + pos * 2])
    y = int(raw[3 + pos * 2])
    squared = x * x + y * y
    if squared == 0:
        base += 1
    else:
        items.append((math.sqrt(squared), math.atan2(y, x)))

circle = math.tau

# CLAUSE: solve_logic
def build_segments(rad):
    result = []
    max_dist = 2.0 * rad + 1e-9
    for distance, theta in items:
        if distance > max_dist:
            continue
        shift = math.acos(min(1.0, distance / (2.0 * rad)))
        a = (theta - shift) % circle
        b = (theta + shift) % circle
        if a <= b:
            result.append((a, b))
        else:
            result.append((a, circle))
            result.append((0.0, b))
    return result

def valid(rad):
    if base >= k:
        return True
    if rad < 1e-13:
        return False
    required = k - base
    segments = build_segments(rad)
    if len(segments) < required:
        return False
    changes = []
    for a, b in segments:
        changes.append((a, 1))
        changes.append((b, -1))
    changes.sort(key=lambda pair: (pair[0], -pair[1]))
    now = 0
    for point, value in changes:
        now += value
        if now >= required:
            return True
    return False

left = 0.0
right = 200000.0
for step in range(80):
    center = left + (right - left) / 2.0
    if valid(center):
        right = center
    else:
        left = center

# CLAUSE: finish_program
print("%.10f" % right)
