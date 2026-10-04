import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    z = data[1]
    return z, sorted(data[2:2 + n])

# Clause fits [Confidence: 1.00]
def fits(k, z, spots):
    n = len(spots)
    for i in range(k):
        if spots[n - k + i] - spots[i] < z:
            return False
    return True

# Clause most_pairs [Confidence: 1.00]
def most_pairs(z, spots):
    bottom = 0
    high = len(spots) // 2
    while bottom < high:
        mid = (bottom + high + 1) // 2
        if fits(mid, z, spots):
            bottom = mid
        else:
            high = mid - 1
    return bottom

# Clause main [Confidence: 1.00]
def main():
    z, spots = read_input()
    sys.stdout.write("%d\n" % most_pairs(z, spots))


if __name__ == "__main__":
    main()

