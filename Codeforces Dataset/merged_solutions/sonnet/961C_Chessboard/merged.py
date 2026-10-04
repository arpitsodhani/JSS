import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    pieces = []
    pos = 1
    for _ in range(4):
        pieces.append([data[pos + i].decode() for i in range(n)])
        pos += n
    return n, pieces

# Clause piece_costs [Confidence: 1.00]
def piece_costs(n, pieces):
    rows = []
    for grid in pieces:
        wrong = 0
        for i in range(n):
            for j in range(n):
                want = "0" if (i + j) % 2 == 0 else "1"
                if grid[i][j] != want:
                    wrong += 1
        rows.append((wrong, n * n - wrong))
    return rows

# Clause cheapest_board [Confidence: 1.00]
def cheapest_board(rows):
    best = 1 << 62
    for bits in range(16):
        if bin(bits).count("1") != 2:
            continue
        here = 0
        for i in range(4):
            here += rows[i][0] if (bits >> i) & 1 else rows[i][1]
        if here < best:
            best = here
    return best

# Clause main [Confidence: 1.00]
def main():
    n, pieces = read_input()
    sys.stdout.write("%d\n" % cheapest_board(piece_costs(n, pieces)))


if __name__ == "__main__":
    main()

