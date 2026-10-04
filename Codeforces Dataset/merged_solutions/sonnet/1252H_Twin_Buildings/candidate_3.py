import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    return [(fields[1 + 2 * i], fields[2 + 2 * i]) for i in range(n)]


# --- clause: best_twice_area :: (lands: list[tuple[int, int]]) -> int ---
def best_twice_area(lands):
    sides = []
    for length, width in lands:
        if length < width:
            length, width = width, length
        sides.append((length, width))
    peak = 0
    for length, width in sides:
        if length * width > peak:
            peak = length * width
    sides.sort(reverse=True)
    widest = 0
    for length, width in sides:
        short = width if width < widest else widest
        if 2 * length * short > peak:
            peak = 2 * length * short
        if width > widest:
            widest = width
    return peak


# --- clause: main :: () -> None ---
def main():
    twice = best_twice_area(read_input())
    sys.stdout.write("%d.%d\n" % (twice // 2, 5 if twice % 2 else 0))


if __name__ == "__main__":
    main()
