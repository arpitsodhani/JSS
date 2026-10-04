# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def convex_hull(points):
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

def area2(a, b, c):
    return abs(cross(a, b, c))

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    
    points = []
    idx = 1
    for _ in range(n):
        points.append((data[idx], data[idx + 1]))
        idx += 2
    
    hull = convex_hull(points)
    m = len(hull)
    
    if m == 1:
        p = hull[0]
        print(p[0], p[1])
        print(p[0], p[1])
        print(p[0], p[1])
        return
    
    if m == 2:
        a, b = hull
        print(a[0], a[1])
        print(b[0], b[1])
        print(a[0], a[1])
        return
    
    best = (hull[0], hull[1], hull[2])
    best_area = 0
    
    for i in range(m):
        k = (i + 2) % m
        for j in range(i + 1, m):
            if k == j:
                k = (k + 1) % m
            
            while True:
                nk = (k + 1) % m
                if nk == i:
                    break
                if area2(hull[i], hull[j], hull[nk]) > area2(hull[i], hull[j], hull[k]):
                    k = nk
                else:
                    break
            
            cur = area2(hull[i], hull[j], hull[k])
            if cur > best_area:
                best_area = cur
                best = (hull[i], hull[j], hull[k])
    
    a, b, c = best
    
    result = [
        (a[0] + b[0] - c[0], a[1] + b[1] - c[1]),
        (a[0] + c[0] - b[0], a[1] + c[1] - b[1]),
        (b[0] + c[0] - a[0], b[1] + c[1] - a[1]),
    ]
    
    for x, y in result:
        print(x, y)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
