import sys

def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
pts = [(data[i], data[i + 1]) for i in range(2, 2 * n + 2, 2)]

p = hull(pts)
m = len(p)

if m == 1:
    x, y = p[0]
    print(x, y)
    print(x + 1, y)
    print(x, y + 1)
elif m == 2:
    a, b = p
    print(a[0], a[1])
    print(b[0], b[1])
    print(a[0] + b[1] - a[1], a[1] + a[0] - b[0])
else:
    best = (0, 1, 2)
    best_area = abs(cross(p[0], p[1], p[2]))
    for i in range(m):
        k = (i + 2) % m
        for j in range(i + 1, m):
            if k == j:
                k = (k + 1) % m
            while True:
                nk = (k + 1) % m
                if nk == i:
                    break
                if abs(cross(p[i], p[j], p[nk])) > abs(cross(p[i], p[j], p[k])):
                    k = nk
                else:
                    break
            area = abs(cross(p[i], p[j], p[k]))
            if area > best_area:
                best_area = area
                best = (i, j, k)

    a, b, c = p[best[0]], p[best[1]], p[best[2]]
    print(b[0] + c[0] - a[0], b[1] + c[1] - a[1])
    print(a[0] + c[0] - b[0], a[1] + c[1] - b[1])
    print(a[0] + b[0] - c[0], a[1] + b[1] - c[1])
