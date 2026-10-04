import sys

def is_square_boundary(points):
    if not points:
        return False
    
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    
    # Must be a square
    if x_max - x_min != y_max - y_min:
        return False
    
    # All points must be on boundary
    for x, y in points:
        if not (((x == x_min or x == x_max) and y_min <= y <= y_max) or
                ((y == y_min or y == y_max) and x_min <= x <= x_max)):
            return False
    
    return True

def main():
    input_data = sys.stdin.read().strip().split('\n')
    n = int(input_data[0])
    
    points = []
    for line in input_data[1:]:
        x, y = map(int, line.split())
        points.append((x, y))
    
    for i in range(len(points)):
        remaining = points[:i] + points[i+1:]
        if is_square_boundary(remaining):
            print(points[i][0], points[i][1])
            return

main()
