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

def build_signature(poly):
    n = len(poly)
    if n <= 1:
        return []
    
    if n == 2:
        dx = poly[1][0] - poly[0][0]
        dy = poly[1][1] - poly[0][1]
        return [(dx * dx + dy * dy,)]
    
    result = []
    edges = []
    for i in range(n):
        j = (i + 1) % n
        edges.append((poly[j][0] - poly[i][0], poly[j][1] - poly[i][1]))
    
    for i in range(n):
        x1, y1 = edges[i]
        x2, y2 = edges[(i + 1) % n]
        length = x1 * x1 + y1 * y1
        turn = x1 * y2 - y1 * x2
        dot = x1 * x2 + y1 * y2
        result.append((length, turn, dot))
    
    return result

def contains_rotation(a, b):
    if len(a) != len(b):
        return False
    if not a:
        return True
    
    pattern = b
    text = a + a[:-1]
    
    prefix = [0] * len(pattern)
    for i in range(1, len(pattern)):
        j = prefix[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j
    
    j = 0
    for item in text:
        while j > 0 and item != pattern[j]:
            j = prefix[j - 1]
        if item == pattern[j]:
            j += 1
        if j == len(pattern):
            return True
    
    return False

def parse_input(data):
    if len(data) >= 2:
        n, m = data[0], data[1]
        if len(data) == 2 + 2 * (n + m):
            idx = 2
            first = [(data[idx + 2 * i], data[idx + 2 * i + 1]) for i in range(n)]
            idx += 2 * n
            second = [(data[idx + 2 * i], data[idx + 2 * i + 1]) for i in range(m)]
            return first, second
    
    n = data[0]
    idx = 1
    first = [(data[idx + 2 * i], data[idx + 2 * i + 1]) for i in range(n)]
    idx += 2 * n
    m = data[idx]
    idx += 1
    second = [(data[idx + 2 * i], data[idx + 2 * i + 1]) for i in range(m)]
    return first, second

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    first, second = parse_input(data)
    
    hull_first = convex_hull(first)
    hull_second = convex_hull(second)
    
    sig_first = build_signature(hull_first)
    sig_second = build_signature(hull_second)
    
    print("YES" if contains_rotation(sig_first, sig_second) else "NO")

if __name__ == "__main__":
    main()
