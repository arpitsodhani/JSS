import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    h = data[1]
    return h, data[2:2 + n]

# Clause fits [Confidence: 1.00]
def fits(h, a, k):
    arranged = sorted(a[:k])
    summed = 0
    i = k - 1
    while i >= 0:
        summed += arranged[i]
        i -= 2
    return summed <= h

# Clause most_bottles [Confidence: 1.00]
def most_bottles(h, a):
    low = 0
    high = len(a)
    while low < high:
        mid = (low + high + 1) // 2
        if fits(h, a, mid):
            low = mid
        else:
            high = mid - 1
    return low

# Clause main [Confidence: 1.00]
def main():
    h, a = read_input()
    sys.stdout.write("%d\n" % most_bottles(h, a))


if __name__ == "__main__":
    main()

