import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    d = int(data[1])
    xs = list(map(int, data[2:2 + n]))
    return n, d, xs

# Clause count_triples [Confidence: 0.80]
def count_triples(n, d, xs):
    total = 0
    for right in range(n):
        lo = 0
        hi = right
        while lo < hi:
            mid = (lo + hi) // 2
            if xs[right] - xs[mid] > d:
                lo = mid + 1
            else:
                hi = mid
        width = right - lo
        total += width * (width - 1) // 2
    return total

# Clause main [Confidence: 1.00]
def main():
    n, d, xs = read_input()
    sys.stdout.write(str(count_triples(n, d, xs)) + "\n")


if __name__ == "__main__":
    main()

