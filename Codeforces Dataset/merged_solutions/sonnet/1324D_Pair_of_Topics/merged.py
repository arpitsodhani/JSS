import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return data[1:1 + n], data[1 + n:1 + 2 * n]

# Clause count_good [Confidence: 1.00]
def count_good(a, b):
    gaps = sorted(a[i] - b[i] for i in range(len(a)))
    total = 0
    left = 0
    high = len(gaps) - 1
    while left < high:
        if gaps[left] + gaps[high] > 0:
            total += high - left
            high -= 1
        else:
            left += 1
    return total

# Clause main [Confidence: 1.00]
def main():
    a, b = read_input()
    sys.stdout.write("%d\n" % count_good(a, b))


if __name__ == "__main__":
    main()

