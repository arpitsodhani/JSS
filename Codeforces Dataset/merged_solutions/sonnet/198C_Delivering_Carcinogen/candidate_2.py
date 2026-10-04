import math
import sys


# --- clause: read_input :: () -> tuple[float, float, float, float, float, float, float] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    xp, yp, vp = float(data[0]), float(data[1]), float(data[2])
    x, y, v, r = float(data[3]), float(data[4]), float(data[5]), float(data[6])
    return xp, yp, vp, x, y, v, r


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
    between = abs(math.atan2(ay, ax) - math.atan2(by, bx))
    if between > math.pi:
        between = 2.0 * math.pi - between
    sweep = between - math.asin(min(1.0, first / da)) - math.asin(min(1.0, second / db))
    if sweep < 0.0:
        sweep = 0.0
    return first + second + r * sweep


# --- clause: earliest_time :: (xp: float, yp: float, vp: float, x: float, y: float, v: float, r: float) -> float ---
def earliest_time(xp, yp, vp, x, y, v, r):
    radius = math.hypot(xp, yp)
    start = math.atan2(yp, xp)
    low = 0.0
    high = 1e9
    for _ in range(200):
        mid = (low + high) / 2.0
        angle = start + vp * mid / radius
        tx = radius * math.cos(angle)
        ty = radius * math.sin(angle)
        if travel_distance(x, y, tx, ty, r) <= v * mid:
            high = mid
        else:
            low = mid
    return high


# --- clause: main :: () -> None ---
def main():
    xp, yp, vp, x, y, v, r = read_input()
    sys.stdout.write("%.9lf\n" % earliest_time(xp, yp, vp, x, y, v, r))


if __name__ == "__main__":
    main()
