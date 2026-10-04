import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])

# Clause trailing_zeros [Confidence: 0.60]
def trailing_zeros(n):
    power = 5
    total = 0
    while power <= n:
        total += n // power
        power *= 5
    return total

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(str(trailing_zeros(read_input())) + "\n")


if __name__ == "__main__":
    main()

