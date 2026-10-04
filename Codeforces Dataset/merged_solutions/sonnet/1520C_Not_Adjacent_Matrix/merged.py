import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause build_matrix [Confidence: 0.40]
def build_matrix(n):
    if n == 2:
        return None
    values = list(range(1, n * n + 1, 2)) + list(range(2, n * n + 1, 2))
    rows = []
    for i in range(n):
        rows.append(values[i * n:(i + 1) * n])
    return rows

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n in read_input():
        rows = build_matrix(n)
        if rows is None:
            out.append("-1")
        else:
            for row in rows:
                out.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

