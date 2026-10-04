# CLAUSE: setup_environment
import sys

def orientation(p, q, r):
    x1 = q[0] - p[0]
    y1 = q[1] - p[1]
    x2 = r[0] - p[0]
    y2 = r[1] - p[1]
    return x1 * y2 - y1 * x2

def convex_polygon(seq):
    seq = sorted(set(seq))
    if len(seq) <= 1:
        return seq
    first = []
    second = []
    for point in seq:
        while len(first) >= 2 and orientation(first[-2], first[-1], point) <= 0:
            first.pop()
        first.append(point)
    for point in reversed(seq):
        while len(second) >= 2 and orientation(second[-2], second[-1], point) <= 0:
            second.pop()
        second.append(point)
    first.pop()
    second.pop()
    first.extend(second)
    return first

def area_value(p, q, r):
    return abs(orientation(p, q, r))

def enclosing_triangle(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    return (
        (ax + bx - cx, ay + by - cy),
        (ax + cx - bx, ay + cy - by),
        (bx + cx - ax, by + cy - ay),
    )

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    count = values[0]
    points = []
    pos = 1
    while len(points) < count:
        points.append((values[pos], values[pos + 1]))
        pos += 2

    poly = convex_polygon(points)
    size = len(poly)

    if size < 3:
        if size == 1:
            out = (poly[0], poly[0], poly[0])
        else:
            out = (poly[0], poly[1], poly[0])
    else:
        chosen = (0, 1, 2)
        largest = 0
        for left in range(size):
            top = (left + 2) % size
            middle = left + 1
            while middle < size:
                if top == middle:
                    top = (top + 1) % size
                while (top + 1) % size != left:
                    after = (top + 1) % size
                    if area_value(poly[left], poly[middle], poly[after]) <= area_value(poly[left], poly[middle], poly[top]):
                        break
                    top = after
                candidate = area_value(poly[left], poly[middle], poly[top])
                if candidate > largest:
                    largest = candidate
                    chosen = (left, middle, top)
                middle += 1
        out = enclosing_triangle(poly[chosen[0]], poly[chosen[1]], poly[chosen[2]])

# CLAUSE: finish_program
    print("\n".join("{} {}".format(x, y) for x, y in out))

if __name__ == "__main__":
    main()
