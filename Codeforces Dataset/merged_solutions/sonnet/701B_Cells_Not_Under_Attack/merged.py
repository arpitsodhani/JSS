import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    spots = [int(token) for token in data[2:2 + 2 * m]]
    return n, m, spots

# Clause free_cells [Confidence: 0.60]
def free_cells(n, m, spots):
    rows = [False] * (n + 1)
    cols = [False] * (n + 1)
    used_rows = 0
    used_cols = 0
    out = []
    for i in range(m):
        r = spots[2 * i]
        c = spots[2 * i + 1]
        if not rows[r]:
            rows[r] = True
            used_rows += 1
        if not cols[c]:
            cols[c] = True
            used_cols += 1
        out.append(str((n - used_rows) * (n - used_cols)))
    return out

# Clause main [Confidence: 1.00]
def main():
    n, m, spots = read_input()
    sys.stdout.write(" ".join(free_cells(n, m, spots)) + "\n")


if __name__ == "__main__":
    main()

