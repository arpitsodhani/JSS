import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    b = int(data[0])
    k = int(data[1])
    digits = [int(token) for token in data[2:k + 2]]
    return b, k, digits

# Clause parity [Confidence: 0.80]
def parity(b, k, digits):
    if b % 2 == 0:
        rest = digits[k - 1] % 2
    else:
        rest = 0
        for value in digits:
            rest ^= value % 2
    if rest:
        return "odd"
    return "even"

# Clause main [Confidence: 1.00]
def main():
    b, k, digits = read_input()
    sys.stdout.write(parity(b, k, digits) + "\n")


if __name__ == "__main__":
    main()

