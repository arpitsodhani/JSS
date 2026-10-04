import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]

# Clause count_tiles [Confidence: 0.80]
def count_tiles(a, b, c):
    return a * b + b * c + c * a - a - b - c + 1

# Clause main [Confidence: 1.00]
def main():
    a, b, c = read_input()
    sys.stdout.write("%d\n" % count_tiles(a, b, c))


if __name__ == "__main__":
    main()

