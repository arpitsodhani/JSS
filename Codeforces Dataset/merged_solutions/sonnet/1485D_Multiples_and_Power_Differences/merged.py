import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    grid = []
    pos = 2
    for _ in range(n):
        grid.append(data[pos:pos + m])
        pos += m
    return n, m, grid

# Clause build_matrix [Confidence: 0.80]
def build_matrix(n, m, grid):
    base = 720720
    out = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row.append(base)
            else:
                value = grid[i][j]
                row.append(base + value * value * value * value)
        out.append(row)
    return out

# Clause main [Confidence: 1.00]
def main():
    n, m, grid = read_input()
    result = build_matrix(n, m, grid)
    sys.stdout.write("\n".join(" ".join(map(str, row)) for row in result) + "\n")


if __name__ == "__main__":
    main()

