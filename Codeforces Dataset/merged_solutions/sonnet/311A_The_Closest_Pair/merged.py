import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]

# Clause build_data [Confidence: 0.60]
def build_data(n, k):
    if n * (n - 1) // 2 <= k:
        return None
    return [(0, y) for y in range(n)]

# Clause main [Confidence: 1.00]
def main():
    n, k = read_input()
    points = build_data(n, k)
    if points is None:
        sys.stdout.write("no solution\n")
    else:
        sys.stdout.write("\n".join("%d %d" % p for p in points) + "\n")


if __name__ == "__main__":
    main()

