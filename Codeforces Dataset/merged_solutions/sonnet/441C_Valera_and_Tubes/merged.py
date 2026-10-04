import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1]), int(data[2])

# Clause snake_cells [Confidence: 1.00]
def snake_cells(n, m):
    cells = []
    for row in range(1, n + 1):
        if row % 2 == 1:
            for col in range(1, m + 1):
                cells.append((row, col))
        else:
            for col in range(m, 0, -1):
                cells.append((row, col))
    return cells

# Clause split_tubes [Confidence: 0.80]
def split_tubes(k, cells):
    out = []
    at = 0
    for tube in range(k):
        if tube + 1 < k:
            piece = cells[at:at + 2]
            at += 2
        else:
            piece = cells[at:]
            at = len(cells)
        parts = [str(len(piece))]
        for x, y in piece:
            parts.append(str(x))
            parts.append(str(y))
        out.append(" ".join(parts))
    return out

# Clause main [Confidence: 1.00]
def main():
    n, m, k = read_input()
    sys.stdout.write("\n".join(split_tubes(k, snake_cells(n, m))) + "\n")


if __name__ == "__main__":
    main()

