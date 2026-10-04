import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = list(map(int, data[1:n + 1]))
    return n, values

# Clause winner [Confidence: 1.00]
def winner(n, values):
    for value in values:
        if value % 2 == 1:
            return "First"
    return "Second"

# Clause main [Confidence: 1.00]
def main():
    n, values = read_input()
    sys.stdout.write(winner(n, values) + "\n")


if __name__ == "__main__":
    main()

