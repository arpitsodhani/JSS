import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])

# Clause decide [Confidence: 0.60]
def decide(n):
    if not n % 2:
        return "white\n1 2"
    return "black"

# Clause main [Confidence: 1.00]
def main():
    n = read_input()
    sys.stdout.write(decide(n) + "\n")


if __name__ == "__main__":
    main()

