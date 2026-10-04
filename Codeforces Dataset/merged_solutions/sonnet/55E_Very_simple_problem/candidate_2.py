import sys


# --- clause: read_input :: () -> tuple[list[tuple[int, int]], list[tuple[int, int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    corners = []
    for i in range(n):
        corners.append((tokens[1 + 2 * i], tokens[2 + 2 * i]))
    at = 1 + 2 * n
    t = tokens[at]
    at += 1
    points = []
    for i in range(t):
        points.append((tokens[at + 2 * i], tokens[at + 1 + 2 * i]))
    return corners, points


# --- clause: inside_polygon :: (corners: list[tuple[int, int]], point: tuple[int, int]) -> bool ---
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


# --- clause: count_triangles :: (corners: list[tuple[int, int]], point: tuple[int, int]) -> int ---
def count_triangles(corners, point):
    n = len(corners)
    px = point[0]
    py = point[1]
    total = n * (n - 1) * (n - 2) // 6
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
        total -= span * (span - 1) // 2
    return total


# --- clause: main :: () -> None ---
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
