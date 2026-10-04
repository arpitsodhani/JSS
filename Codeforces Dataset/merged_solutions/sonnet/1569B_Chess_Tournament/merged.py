import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        cases.append(data[2 + 2 * i].decode())
    return cases

# Clause build_matrix [Confidence: 1.00]
def build_matrix(s):
    n = len(s)
    winners = [i for i in range(n) if s[i] == "2"]
    if 0 < len(winners) < 3:
        return None
    grid = [["="] * n for _ in range(n)]
    for i in range(n):
        grid[i][i] = "X"
    for i in range(len(winners)):
        me = winners[i]
        prey = winners[(i + 1) % len(winners)]
        grid[me][prey] = "+"
        grid[prey][me] = "-"
    return ["".join(band) for band in grid]

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for s in read_input():
        grid = build_matrix(s)
        if grid is None:
            lines.append("NO")
        else:
            lines.append("YES")
            lines.extend(grid)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

