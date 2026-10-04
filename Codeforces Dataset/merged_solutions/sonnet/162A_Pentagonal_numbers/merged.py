import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause pentagonal [Confidence: 0.80]
def pentagonal(n):
    return (3 * n * n - n) // 2

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % pentagonal(read_input()))


if __name__ == "__main__":
    main()

