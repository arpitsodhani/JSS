import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause gcd_of [Confidence: 1.00]
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a

# Clause least_sum [Confidence: 0.80]
def least_sum(x):
    base = x[0]
    for element in x:
        base = gcd_of(base, element)
    return base * len(x)

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % least_sum(read_input()))


if __name__ == "__main__":
    main()

