import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause fewest_bacteria [Confidence: 0.80]
def fewest_bacteria(x):
    amount = 0
    while x:
        amount += x % 2
        x //= 2
    return amount

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % fewest_bacteria(read_input()))


if __name__ == "__main__":
    main()

