import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]

# Clause count_decks [Confidence: 0.60]
def count_decks(b, g, n):
    high = n if n < b else b
    low = n - g
    if low < 0:
        low = 0
    return high - low + 1

# Clause main [Confidence: 1.00]
def main():
    b, g, n = read_input()
    sys.stdout.write(str(count_decks(b, g, n)) + "\n")


if __name__ == "__main__":
    main()

