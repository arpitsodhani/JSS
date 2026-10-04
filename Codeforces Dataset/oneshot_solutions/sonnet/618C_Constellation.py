import sys

def cross_product(o, a, b):
    """Cross product of vectors OA and OB"""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def is_strictly_outside(p, a, b, c):
    """Returns True if p is strictly outside triangle abc"""
    d1 = cross_product(a, b, p)
    d2 = cross_product(b, c, p)
    d3 = cross_product(c, a, p)
    
    # Point is inside or on boundary if all cross products are >= 0 or all <= 0
    all_non_negative = (d1 >= 0 and d2 >= 0 and d3 >= 0)
    all_non_positive = (d1 <= 0 and d2 <= 0 and d3 <= 0)
    
    return not (all_non_negative or all_non_positive)

def solve():
    data = sys.stdin.buffer.read().decode('ascii').strip().split()
    n = int(data[0])
    points = []
    for i in range(n):
        x = int(data[1 + 2*i])
        y = int(data[1 + 2*i + 1])
        points.append((x, y, i + 1))
    
    # Sort points lexicographically
    points.sort()
    
    # Try combinations from the first several points
    limit = min(20, n)
    for i in range(limit):
        for j in range(i + 1, limit):
            for k in range(j + 1, limit):
                a, b, c = points[i], points[j], points[k]
                
                # Check if triangle has positive area (non-collinear)
                if cross_product(a, b, c) == 0:
                    continue
                
                # Check if all other points are strictly outside
                valid = True
                for m in range(n):
                    if m == i or m == j or m == k:
                        continue
                    if not is_strictly_outside(points[m], a, b, c):
                        valid = False
                        break
                
                if valid:
                    print(a[2], b[2], c[2])
                    return

solve()
