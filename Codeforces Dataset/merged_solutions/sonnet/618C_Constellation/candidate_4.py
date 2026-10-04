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
    first = order[0]
    second = order[1]
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    best_area = None
    best_index = 0
    position = 2
    while position < len(order):
        x, y, index = order[position]
        area = abs(dx * (y - first[1]) - dy * (x - first[0]))
        if area and (best_area is None or area < best_area):
            best_area = area
            best_index = index
        position += 1
    return first[2], second[2], best_index

# --- clause: main :: () -> None ---
def main():
    stars = read_input()
    a, b, c = pick_triangle(stars)
    sys.stdout.write("%d %d %d\n" % (a, b, c))


if __name__ == "__main__":
    main()
