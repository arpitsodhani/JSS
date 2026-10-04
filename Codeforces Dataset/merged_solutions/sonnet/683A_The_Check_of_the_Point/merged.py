import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]

# Clause classify [Confidence: 0.60]
def classify(a, x, y):
    if x < 0 or y < 0 or x > a or y > a:
        return 2
    if x == 0 or y == 0 or x == a or y == a:
        return 1
    return 0

# Clause main [Confidence: 1.00]
def main():
    a, x, y = read_input()
    sys.stdout.write(str(classify(a, x, y)) + "\n")


if __name__ == "__main__":
    main()

