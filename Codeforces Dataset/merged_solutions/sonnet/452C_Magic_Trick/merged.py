import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]

# Clause trick_chance [Confidence: 1.00]
def trick_chance(n, m):
    if n == 1 or m == 1:
        return 1.0
    extra = (n - 1) * (m - 1) / float(n * m - 1)
    return (1.0 + extra) / n

# Clause main [Confidence: 1.00]
def main():
    n, m = read_input()
    sys.stdout.write("%.12f\n" % trick_chance(n, m))


if __name__ == "__main__":
    main()

