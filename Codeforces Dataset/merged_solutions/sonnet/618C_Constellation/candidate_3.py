import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    stars = []
    for i in range(n):
        stars.append((data[1 + 2 * i], data[2 + 2 * i], i + 1))
    return stars

# --- clause: pick_triangle :: (stars: list[tuple[int, int, int]]) -> tuple[int, int, int] ---
def pick_triangle(stars):
    order = sorted(stars)
    ax, ay, ai = order[0]
    bx, by, bi = order[1]
    best = 0
    ci = 0
    for point in order[2:]:
        cx, cy, index = point
        area = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
        if area < 0:
            area = -area
        if area > 0 and (ci == 0 or area < best):
            best = area
            ci = index
    return ai, bi, ci

# --- clause: main :: () -> None ---
def main():
    stars = read_input()
    a, b, c = pick_triangle(stars)
    sys.stdout.write("%d %d %d\n" % (a, b, c))


if __name__ == "__main__":
    main()
