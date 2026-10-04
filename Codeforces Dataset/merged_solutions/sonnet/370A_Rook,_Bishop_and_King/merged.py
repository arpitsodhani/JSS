import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2], data[3]

# Clause piece_moves [Confidence: 1.00]
def piece_moves(r1, c1, r2, c2):
    rook = 1 if (r1 == r2 or c1 == c2) else 2
    if (r1 + c1) % 2 != (r2 + c2) % 2:
        bishop = 0
    elif abs(r1 - r2) == abs(c1 - c2):
        bishop = 1
    else:
        bishop = 2
    king = abs(r1 - r2)
    if abs(c1 - c2) > king:
        king = abs(c1 - c2)
    return rook, bishop, king

# Clause main [Confidence: 1.00]
def main():
    r1, c1, r2, c2 = read_input()
    sys.stdout.write("%d %d %d\n" % piece_moves(r1, c1, r2, c2))


if __name__ == "__main__":
    main()

