# Clause setup_environment [Confidence: 0.80]
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


# Clause solve_logic [Confidence: 0.80]
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


# Clause finish_program [Confidence: 0.20]
sys.stdout.write(f"{hi:.10f}\n")


