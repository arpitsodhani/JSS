import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()

# Clause complexity [Confidence: 0.80]
def complexity(bits):
    mod = 1000000007
    element = int(bits, 2) % mod
    return element * pow(2, len(bits) - 1, mod) % mod

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % complexity(read_input()))


if __name__ == "__main__":
    main()

