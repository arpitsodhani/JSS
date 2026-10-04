import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1])

# Clause settle [Confidence: 1.00]
def settle(a, b):
    while a and b:
        if a >= 2 * b:
            a %= 2 * b
        elif b >= 2 * a:
            b %= 2 * a
        else:
            break
    return a, b

# Clause main [Confidence: 1.00]
def main():
    a, b = read_input()
    sys.stdout.write("%d %d\n" % settle(a, b))


if __name__ == "__main__":
    main()

