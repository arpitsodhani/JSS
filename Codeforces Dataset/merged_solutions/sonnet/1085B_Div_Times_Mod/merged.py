import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1])

# Clause smallest_x [Confidence: 0.80]
def smallest_x(n, k):
    best = None
    for r in range(1, k):
        if n % r:
            continue
        item = (n // r) * k + r
        if best is None or item < best:
            best = item
    return best

# Clause main [Confidence: 1.00]
def main():
    n, k = read_input()
    sys.stdout.write("%d\n" % smallest_x(n, k))


if __name__ == "__main__":
    main()

