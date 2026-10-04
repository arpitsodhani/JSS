import sys
from math import sqrt

def main():
    data = list(map(float, sys.stdin.read().split()))
    idx = 0
    
    n = int(data[idx])
    idx += 1
    
    p = data[idx]
    q = data[idx + 1]
    m = int(data[idx + 2])
    idx += 3
    
    lines = []
    for _ in range(n):
        a = data[idx]
        b = data[idx + 1]
        c = -(a * a + b * b)
        lines.append((a, b, c))
        idx += 2
    
    # Find all intersection points
    points = []
    for i in range(n):
        for j in range(i + 1, n):
            a1, b1, c1 = lines[i]
            a2, b2, c2 = lines[j]
            
            # Solve system: a1*x + b1*y + c1 = 0, a2*x + b2*y + c2 = 0
            det = a1 * b2 - a2 * b1
            if abs(det) > 1e-12:  # Lines not parallel
                x = (b1 * c2 - b2 * c1) / det
                y = (a2 * c1 - a1 * c2) / det
                points.append((x, y))
    
    # Calculate distances from query point
    distances = []
    for x, y in points:
        dist = sqrt((x - p) ** 2 + (y - q) ** 2)
        distances.append(dist)
    
    # Sort and sum m smallest
    distances.sort()
    result = sum(distances[:m])
    
    print(f"{result:.9f}")

if __name__ == "__main__":
    main()
