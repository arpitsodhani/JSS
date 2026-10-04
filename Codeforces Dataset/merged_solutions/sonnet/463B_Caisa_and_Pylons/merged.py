import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause least_paid [Confidence: 0.80]
def least_paid(heights):
    best = 0
    for item in heights:
        if item > best:
            best = item
    return best

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % least_paid(read_input()))


if __name__ == "__main__":
    main()

