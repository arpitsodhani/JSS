import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, x, y, z, p = data[:6]
    candies = []
    for i in range(p):
        candies.append((data[6 + 2 * i], data[7 + 2 * i]))
    return n, m, x % 4, y % 2, z % 4, candies

# Clause move_candy [Confidence: 1.00]
def move_candy(n, m, x, y, z, row, col):
    for _ in range(x):
        row, col, n, m = col, n + 1 - row, m, n
    if y:
        col = m + 1 - col
    for _ in range(z):
        row, col, n, m = m + 1 - col, row, m, n
    return n, m, row, col

# Clause main [Confidence: 1.00]
def main():
    n, m, x, y, z, candies = read_input()
    collected = []
    for row, col in candies:
        _, _, row, col = move_candy(n, m, x, y, z, row, col)
        collected.append("%d %d" % (row, col))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

