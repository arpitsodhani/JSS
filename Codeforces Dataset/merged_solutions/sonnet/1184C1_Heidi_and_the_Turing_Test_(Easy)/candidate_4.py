import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    points = []
    for i in range(4 * n + 1):
        points.append((data[1 + 2 * i], data[2 + 2 * i]))
    return n, points

# --- clause: find_stray :: (n: int, points: list[tuple[int, int]]) -> tuple[int, int] ---
def find_stray(n, points):
    total = len(points)
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    for skip in range(total):
        rest_x = xs[:skip] + xs[skip + 1:]
        rest_y = ys[:skip] + ys[skip + 1:]
        low_x = min(rest_x)
        high_x = max(rest_x)
        low_y = min(rest_y)
        high_y = max(rest_y)
        if high_x - low_x != high_y - low_y:
            continue
        good = True
        for x, y in zip(rest_x, rest_y):
            if low_x < x < high_x and low_y < y < high_y:
                good = False
                break
        if good:
            return points[skip]
    return points[0]

# --- clause: main :: () -> None ---
def main():
    n, points = read_input()
    x, y = find_stray(n, points)
    sys.stdout.write("%d %d\n" % (x, y))


if __name__ == "__main__":
    main()
