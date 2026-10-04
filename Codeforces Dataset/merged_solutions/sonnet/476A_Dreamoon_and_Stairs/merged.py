import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]

# Clause fewest_moves [Confidence: 0.80]
def fewest_moves(n, m):
    bottom = (n + 1) // 2
    for moves in range(bottom, n + 1):
        if moves % m == 0:
            return moves
    return -1

# Clause main [Confidence: 1.00]
def main():
    n, m = read_input()
    sys.stdout.write("%d\n" % fewest_moves(n, m))


if __name__ == "__main__":
    main()

