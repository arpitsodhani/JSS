import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases

# Clause paint_board [Confidence: 1.00]
def paint_board(n, m):
    rows = ["W" + "B" * (m - 1)]
    for _ in range(n - 1):
        rows.append("B" * m)
    return rows

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n, m in read_input():
        collected.extend(paint_board(n, m))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

