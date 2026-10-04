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
    for skip in range(total):
        low_x = 100
        high_x = -1
        low_y = 100
        high_y = -1
        for index in range(total):
            if index == skip:
                continue
            x, y = points[index]
            if x < low_x:
                low_x = x
            if x > high_x:
                high_x = x
            if y < low_y:
                low_y = y
            if y > high_y:
                high_y = y
        if high_x - low_x != high_y - low_y:
            continue
        outside = 0
        for index in range(total):
            if index == skip:
                continue
            x, y = points[index]
            if x != low_x and x != high_x and y != low_y and y != high_y:
                outside = 1
                break
        if not outside:
            return points[skip]
    return points[0]

# --- clause: main :: () -> None ---
def main():
    n, points = read_input()
    x, y = find_stray(n, points)
    sys.stdout.write("%d %d\n" % (x, y))


if __name__ == "__main__":
    main()
