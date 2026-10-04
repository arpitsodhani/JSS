import sys

def cross(a, b, c=None):
    if c is None:
        return a[0] * b[1] - a[1] * b[0]
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def inside_convex(poly, p):
    n = len(poly)
    for i in range(n):
        if cross(poly[i], poly[(i + 1) % n], p) <= 0:
            return False
    return True

def count_triangles(poly, p):
    n = len(poly)
    
    if not inside_convex(poly, p):
        return 0
    
    vectors = [(x - p[0], y - p[1]) for x, y in poly]
    bad = 0
    right = 0
    
    for left in range(n):
        if right < left:
            right = left
        
        while right + 1 < left + n:
            a = vectors[left]
            b = vectors[(right + 1) % n]
            if cross(a, b) <= 0:
                break
            right += 1
        
        cnt = right - left
        bad += cnt * (cnt - 1) // 2
    
    total = n * (n - 1) * (n - 2) // 6
    return total - bad

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    idx = 0
    n = data[idx]
    idx += 1
    
    poly = []
    for _ in range(n):
        poly.append((data[idx], data[idx + 1]))
        idx += 2
    
    area2 = 0
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        area2 += x1 * y2 - y1 * x2
    
    if area2 < 0:
        poly.reverse()
    
    if idx + 2 == len(data):
        queries = [(data[idx], data[idx + 1])]
    else:
        m = data[idx]
        idx += 1
        queries = []
        for _ in range(m):
            queries.append((data[idx], data[idx + 1]))
            idx += 2
    
    ans = [str(count_triangles(poly, p)) for p in queries]
    print('\n'.join(ans))

if __name__ == "__main__":
    main()
