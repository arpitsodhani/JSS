import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    return [(tokens[1 + 2 * i], tokens[2 + 2 * i]) for i in range(n)]


# --- clause: best_twice_area :: (lands: list[tuple[int, int]]) -> int ---
def best_twice_area(lands):
    sides = []
    for length, width in lands:
        if length < width:
            length, width = width, length
        sides.append((length, width))
    top = 0
    for length, width in sides:
        if length * width > top:
            top = length * width
    sides.sort(reverse=True)
    widest = 0
    for length, width in sides:
        short = width if width < widest else widest
        if 2 * length * short > top:
            top = 2 * length * short
        if width > widest:
            widest = width
    return top


# --- clause: main :: () -> None ---
def main():
    twice = best_twice_area(read_input())
    sys.stdout.write("%d.%d\n" % (twice // 2, 5 if twice % 2 else 0))


if __name__ == "__main__":
    main()
