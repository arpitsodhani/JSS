# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    import math

    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])

    points = []
    zero = 0
    idx = 2
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        d = math.hypot(x, y)
        if d == 0:
            zero += 1
        else:
            points.append((d, math.atan2(y, x) % (2.0 * math.pi)))

    if zero >= k:
        print("0.0000000000")
        sys.exit()

    need = k - zero
    twopi = 2.0 * math.pi

    def ok(r):
        events = []
        limit = 2.0 * r
        for d, ang in points:
            if d > limit + 1e-12:
                continue
            v = d / limit
            if v > 1.0:
                v = 1.0
            a = math.acos(v)
            l = ang - a
            rr = ang + a
            if l < 0.0:
                events.append((l + twopi, 1))
                events.append((twopi, -1))
                events.append((0.0, 1))
                events.append((rr, -1))
            elif rr >= twopi:
                events.append((l, 1))
                events.append((twopi, -1))
                events.append((0.0, 1))
                events.append((rr - twopi, -1))
            else:
                events.append((l, 1))
                events.append((rr, -1))

        if not events:
            return False

        events.sort(key=lambda e: (e[0], -e[1]))
        cur = 0
        best = 0
        for _, t in events:
            cur += t
            if cur > best:
                best = cur
                if best >= need:
                    return True
        return False

    lo = 0.0
    hi = 200000.0

    for _ in range(70):
        mid = (lo + hi) / 2.0
        if ok(mid):
            hi = mid
        else:
            lo = mid

    print(f"{hi:.10f}")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
