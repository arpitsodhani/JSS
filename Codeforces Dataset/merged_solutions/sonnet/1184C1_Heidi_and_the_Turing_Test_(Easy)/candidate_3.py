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
    for skip, stray in enumerate(points):
        rest = [p for i, p in enumerate(points) if i != skip]
        low_x = min(p[0] for p in rest)
        high_x = max(p[0] for p in rest)
        low_y = min(p[1] for p in rest)
        high_y = max(p[1] for p in rest)
        if high_x - low_x != high_y - low_y:
            continue
        if all(x in (low_x, high_x) or y in (low_y, high_y) for x, y in rest):
            return stray
    return points[0]

# --- clause: main :: () -> None ---
def main():
    n, points = read_input()
    x, y = find_stray(n, points)
    sys.stdout.write("%d %d\n" % (x, y))


if __name__ == "__main__":
    main()
