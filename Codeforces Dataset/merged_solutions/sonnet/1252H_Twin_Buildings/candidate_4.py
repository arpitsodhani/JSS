import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    return [(numbers[1 + 2 * i], numbers[2 + 2 * i]) for i in range(n)]


# --- clause: best_twice_area :: (lands: list[tuple[int, int]]) -> int ---
def best_twice_area(lands):
    sides = []
    for length, width in lands:
        sides.append((max(length, width), min(length, width)))
    sides.sort()
    best = 0
    widest = 0
    i = len(sides) - 1
    while i >= 0:
        length, width = sides[i]
        if length * width > best:
            best = length * width
        short = min(width, widest)
        if 2 * length * short > best:
            best = 2 * length * short
        widest = max(widest, width)
        i -= 1
    return best


# --- clause: main :: () -> None ---
def main():
    twice = best_twice_area(read_input())
    sys.stdout.write("%d.%d\n" % (twice // 2, 5 if twice % 2 else 0))


if __name__ == "__main__":
    main()
