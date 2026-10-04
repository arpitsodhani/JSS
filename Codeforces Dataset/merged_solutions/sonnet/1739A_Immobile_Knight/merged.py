import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    return [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(t)]

# Clause find_cell [Confidence: 0.80]
def find_cell(n, m):
    steps = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    for band in range(1, n + 1):
        for column in range(1, m + 1):
            stuck = True
            for dr, dc in steps:
                r = band + dr
                c = column + dc
                if 1 <= r <= n and 1 <= c <= m:
                    stuck = False
                    break
            if stuck:
                return band, column
    return 1, 1

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for n, m in read_input():
        band, column = find_cell(n, m)
        lines.append("%d %d" % (band, column))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

