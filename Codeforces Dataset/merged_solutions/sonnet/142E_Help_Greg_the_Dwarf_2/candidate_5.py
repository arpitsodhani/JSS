# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
def solve():
    tokens = sys.stdin.buffer.read().split()
    numbers = []
    for token in tokens:
        numbers.append(float(token))

    r = numbers[0]
    h = numbers[1]
    x1 = numbers[2]
    y1 = numbers[3]
    z1 = numbers[4]
    x2 = numbers[5]
    y2 = numbers[6]
    z2 = numbers[7]

    slant = math.hypot(r, h)
    sector_angle = 2.0 * math.pi * r / slant
    angular_factor = sector_angle / (2.0 * math.pi)

    p1 = {
        "x": x1,
        "y": y1,
        "z": z1,
        "rho": math.hypot(x1, y1),
        "theta": math.atan2(y1, x1) * angular_factor,
    }
    p2 = {
        "x": x2,
        "y": y2,
        "z": z2,
        "rho": math.hypot(x2, y2),
        "theta": math.atan2(y2, x2) * angular_factor,
    }

    def radial(point, reflected):
        if reflected:
            return (h + point["z"]) * slant / h
        return (h - point["z"]) * slant / h

    def sector_path(s1, theta1, s2, theta2):
        best = float("inf")
        offsets = range(-10, 11)
        for offset in offsets:
            delta = theta2 - theta1 + offset * sector_angle
            squared = s1 * s1 + s2 * s2 - 2.0 * s1 * s2 * math.cos(delta)
            distance = math.sqrt(max(squared, 0.0))
            best = distance if distance < best else best
        return best

    s1 = radial(p1, False)
    s2 = radial(p2, False)
    answer = sector_path(s1, p1["theta"], s2, p2["theta"])

    alternatives = (
        (s1, p1["theta"], radial(p2, True), p2["theta"]),
        (radial(p1, True), p1["theta"], s2, p2["theta"]),
    )
    for item in alternatives:
        answer = min(answer, sector_path(item[0], item[1], item[2], item[3]))

    eps = 1e-9
    increment = 2.0 * math.pi / 360.0

    if p1["z"] < eps and p1["rho"] < r - eps:
        idx = 0
        while idx < 360:
            phi = -math.pi + increment * idx
            base = math.hypot(p1["x"] - r * math.cos(phi), p1["y"] - r * math.sin(phi))
            theta = phi * angular_factor
            answer = min(answer, base + sector_path(slant, theta, s2, p2["theta"]))
            idx += 1

    if p2["z"] < eps and p2["rho"] < r - eps:
        idx = 0
        while idx < 360:
            phi = -math.pi + increment * idx
            base = math.hypot(p2["x"] - r * math.cos(phi), p2["y"] - r * math.sin(phi))
            theta = phi * angular_factor
            answer = min(answer, sector_path(s1, p1["theta"], slant, theta) + base)
            idx += 1

    if p1["z"] < eps and p2["z"] < eps:
        answer = min(answer, math.hypot(p1["x"] - p2["x"], p1["y"] - p2["y"]))

    print(f"{answer:.9f}")

# CLAUSE: finish_program
solve()
