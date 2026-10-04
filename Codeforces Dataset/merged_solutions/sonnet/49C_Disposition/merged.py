import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause shifted_order [Confidence: 1.00]
def shifted_order(n):
    arranged = []
    for j in range(1, n + 1):
        arranged.append(j % n + 1)
    return arranged

# Clause main [Confidence: 1.00]
def main():
    n = read_input()
    sys.stdout.write(" ".join(map(str, shifted_order(n))) + "\n")


if __name__ == "__main__":
    main()

