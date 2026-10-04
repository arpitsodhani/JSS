# CLAUSE: setup_environment
import sys

def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def build_hull(points):
    pts = sorted(set(points))
    if len(pts) < 2:
        return pts
    low = []
    for p in pts:
        while len(low) > 1 and cross(low[-2], low[-1], p) <= 0:
            low.pop()
        low.append(p)
    high = []
    for p in pts[::-1]:
        while len(high) > 1 and cross(high[-2], high[-1], p) <= 0:
            high.pop()
        high.append(p)
    return low[:-1] + high[:-1]

def doubled_area(a, b, c):
    v = cross(a, b, c)
    return v if v >= 0 else -v

# CLAUSE: solve_logic
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    pts = [(raw[i], raw[i + 1]) for i in range(1, 2 * n, 2)]
    hull = build_hull(pts)
    m = len(hull)

    if m == 1:
        ans = [hull[0], hull[0], hull[0]]
    elif m == 2:
        ans = [hull[0], hull[1], hull[0]]
    else:
        best = (hull[0], hull[1], hull[2])
        best_value = -1
        for i in range(m):
            k = (i + 2) % m
            for j in range(i + 1, m):
                if k == j:
                    k = (k + 1) % m
                while True:
                    nxt = (k + 1) % m
                    if nxt == i:
                        break
                    if doubled_area(hull[i], hull[j], hull[nxt]) > doubled_area(hull[i], hull[j], hull[k]):
                        k = nxt
                    else:
                        break
                now = doubled_area(hull[i], hull[j], hull[k])
                if now > best_value:
                    best_value = now
                    best = (hull[i], hull[j], hull[k])
        a, b, c = best
        ans = [
            (a[0] + b[0] - c[0], a[1] + b[1] - c[1]),
            (a[0] + c[0] - b[0], a[1] + c[1] - b[1]),
            (b[0] + c[0] - a[0], b[1] + c[1] - a[1]),
        ]

# CLAUSE: finish_program
    sys.stdout.write("\n".join(f"{x} {y}" for x, y in ans))

if __name__ == "__main__":
    main()
