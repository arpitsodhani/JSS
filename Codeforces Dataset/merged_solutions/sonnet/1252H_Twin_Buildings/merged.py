import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]

# Clause best_twice_area [Confidence: 1.00]
def best_twice_area(lands):
    sides = []
    for length, width in lands:
        if length < width:
            length, width = width, length
        sides.append((length, width))
    best = 0
    for length, width in sides:
        if length * width > best:
            best = length * width
    sides.sort(reverse=True)
    widest = 0
    for length, width in sides:
        short = width if width < widest else widest
        if 2 * length * short > best:
            best = 2 * length * short
        if width > widest:
            widest = width
    return best

# Clause main [Confidence: 1.00]
def main():
    twice = best_twice_area(read_input())
    sys.stdout.write("%d.%d\n" % (twice // 2, 5 if twice % 2 else 0))


if __name__ == "__main__":
    main()

