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
    for skip in range(len(points)):
        rest = points[:skip] + points[skip + 1:]
        xs = [p[0] for p in rest]
        ys = [p[1] for p in rest]
        low_x = min(xs)
        high_x = max(xs)
        low_y = min(ys)
        high_y = max(ys)
        if high_x - low_x != high_y - low_y:
            continue
        good = True
        for x, y in rest:
            if x != low_x and x != high_x and y != low_y and y != high_y:
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
