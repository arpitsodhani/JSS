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
    x0, y0, i0 = order[0]
    x1, y1, i1 = order[1]
    dx = x1 - x0
    dy = y1 - y0
    best = 0
    chosen = -1
    for x, y, index in order[2:]:
        area = dx * (y - y0) - dy * (x - x0)
        if area < 0:
            area = -area
        if area and (chosen < 0 or area < best):
            best = area
            chosen = index
    return i0, i1, chosen


# --- clause: main :: () -> None ---
def main():
    stars = read_input()
    a, b, c = pick_triangle(stars)
    sys.stdout.write("%d %d %d\n" % (a, b, c))


if __name__ == "__main__":
    main()
