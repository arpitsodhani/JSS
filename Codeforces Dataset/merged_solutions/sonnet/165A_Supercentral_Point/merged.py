import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]

# Clause count_supercentral [Confidence: 0.80]
def count_supercentral(points):
    amount = 0
    for x, y in points:
        left = right = below = above = False
        for a, b in points:
            if b == y and a < x:
                left = True
            if b == y and a > x:
                right = True
            if a == x and b < y:
                below = True
            if a == x and b > y:
                above = True
        if left and right and below and above:
            amount += 1
    return amount

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % count_supercentral(read_input()))


if __name__ == "__main__":
    main()

