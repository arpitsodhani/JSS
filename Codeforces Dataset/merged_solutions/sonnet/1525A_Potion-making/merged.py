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

# Clause fewest_steps [Confidence: 0.80]
def fewest_steps(k):
    return 100 // gcd_of(k, 100)

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for k in read_input():
        collected.append(fewest_steps(k))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()

