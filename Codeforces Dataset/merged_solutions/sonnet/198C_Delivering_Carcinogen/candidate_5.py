import math
import sys


# --- clause: read_input :: () -> tuple[float, float, float, float, float, float, float] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    values = [float(data[i]) for i in range(7)]
    return values[0], values[1], values[2], values[3], values[4], values[5], values[6]


# --- clause: travel_distance :: (ax: float, ay: float, bx: float, by: float, r: float) -> float ---
def travel_distance(ax, ay, bx, by, r):
    da = math.hypot(ax, ay)
    db = math.hypot(bx, by)
    dx = bx - ax
    dy = by - ay
    span = dx * dx + dy * dy
    if span == 0.0:
        near = da
    else:
        t = -(ax * dx + ay * dy) / span
        if t < 0.0:
            t = 0.0
        elif t > 1.0:
            t = 1.0
        near = math.hypot(ax + t * dx, ay + t * dy)
    if near >= r:
        return math.hypot(dx, dy)
    first = math.sqrt(max(da * da - r * r, 0.0))
    second = math.sqrt(max(db * db - r * r, 0.0))
    cosine = (ax * bx + ay * by) / (da * db)
    if cosine > 1.0:
        cosine = 1.0
    elif cosine < -1.0:
        cosine = -1.0
    sweep = math.acos(cosine) - math.acos(min(1.0, r / da)) - math.acos(min(1.0, r / db))
    if sweep < 0.0:
        sweep = 0.0
    return first + second + r * sweep


# --- clause: earliest_time :: (xp: float, yp: float, vp: float, x: float, y: float, v: float, r: float) -> float ---
def earliest_time(xp, yp, vp, x, y, v, r):
    radius = math.hypot(xp, yp)
    start = math.atan2(yp, xp)
    low = 0.0
    high = 1e9
    for _ in range(300):
        mid = (low + high) / 2.0
        angle = start + vp * mid / radius
        tx = radius * math.cos(angle)
        ty = radius * math.sin(angle)
        if v * mid < travel_distance(x, y, tx, ty, r):
            low = mid
        else:
            high = mid
    return high


# --- clause: main :: () -> None ---
def main():
    xp, yp, vp, x, y, v, r = read_input()
    sys.stdout.write("%.9f\n" % earliest_time(xp, yp, vp, x, y, v, r))


if __name__ == "__main__":
    main()
