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
    base_x, base_y, first = order[0]
    next_x, next_y, second = order[1]
    vx = next_x - base_x
    vy = next_y - base_y
    best = -1
    third = -1
    for x, y, index in order[2:]:
        spread = abs(vx * (y - base_y) - vy * (x - base_x))
        if spread == 0:
            continue
        if best < 0 or spread < best:
            best = spread
            third = index
    return first, second, third

# --- clause: main :: () -> None ---
def main():
    stars = read_input()
    a, b, c = pick_triangle(stars)
    sys.stdout.write("%d %d %d\n" % (a, b, c))


if __name__ == "__main__":
    main()
