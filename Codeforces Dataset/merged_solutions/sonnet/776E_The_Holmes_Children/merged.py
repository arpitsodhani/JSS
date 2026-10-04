import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]

# Clause totient [Confidence: 1.00]
def totient(value):
    result = value
    factor = 2
    while factor * factor <= value:
        if value % factor == 0:
            while value % factor == 0:
                value //= factor
            result -= result // factor
        factor += 1
    if value > 1:
        result -= result // value
    return result

# Clause iterate_totient [Confidence: 0.60]
def iterate_totient(n, k):
    steps = (k + 1) // 2
    value = n
    while steps and value > 1:
        value = totient(value)
        steps -= 1
    return value % 1000000007

# Clause main [Confidence: 1.00]
def main():
    n, k = read_input()
    sys.stdout.write(str(iterate_totient(n, k)) + "\n")


if __name__ == "__main__":
    main()

