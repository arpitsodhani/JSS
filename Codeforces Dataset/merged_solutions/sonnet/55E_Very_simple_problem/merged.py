import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    corners = []
    for i in range(n):
        corners.append((data[1 + 2 * i], data[2 + 2 * i]))
    pos = 1 + 2 * n
    t = data[pos]
    pos += 1
    points = []
    for i in range(t):
        points.append((data[pos + 2 * i], data[pos + 1 + 2 * i]))
    return corners, points

# Clause inside_polygon [Confidence: 1.00]
def inside_polygon(corners, point):
    n = len(corners)
    px = point[0]
    py = point[1]
    for i in range(n):
        ax, ay = corners[i]
        bx, by = corners[(i + 1) % n]
        if (bx - ax) * (py - ay) - (by - ay) * (px - ax) <= 0:
            return False
    return True

# Clause count_triangles [Confidence: 1.00]
def count_triangles(corners, point):
    n = len(corners)
    px = point[0]
    py = point[1]
    amount = n * (n - 1) * (n - 2) // 6
    ahead = 1
    for i in range(n):
        ax = corners[i][0] - px
        ay = corners[i][1] - py
        if ahead < i + 1:
            ahead = i + 1
        while ahead < i + n:
            bx = corners[ahead % n][0] - px
            by = corners[ahead % n][1] - py
            if ax * by - ay * bx <= 0:
                break
            ahead += 1
        span = ahead - i - 1
        amount -= span * (span - 1) // 2
    return amount

# Clause main [Confidence: 1.00]
def main():
    corners, points = read_input()
    corners = corners[::-1]
    out = []
    for point in points:
        if inside_polygon(corners, point):
            out.append(count_triangles(corners, point))
        else:
            out.append(0)
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

