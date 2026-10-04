import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2], data[3], data[4]

# Clause fastest_time [Confidence: 0.80]
def fastest_time(n, l, v1, v2, k):
    groups = (n + k - 1) // k
    ride = l / (1.0 + 2.0 * v1 * (groups - 1) / (v1 + v2))
    return ride / v2 + (l - ride) / v1

# Clause main [Confidence: 1.00]
def main():
    n, l, v1, v2, k = read_input()
    sys.stdout.write("%.10f\n" % fastest_time(n, l, v1, v2, k))


if __name__ == "__main__":
    main()

