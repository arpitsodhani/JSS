import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return n, [data[1 + i].decode() for i in range(n)]

# Clause count_crosses [Confidence: 1.00]
def count_crosses(n, grid):
    total = 0
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if grid[i][j] != "X":
                continue
            corners = (grid[i - 1][j - 1], grid[i - 1][j + 1],
                       grid[i + 1][j - 1], grid[i + 1][j + 1])
            if all(ch == "X" for ch in corners):
                total += 1
    return total

# Clause main [Confidence: 1.00]
def main():
    n, grid = read_input()
    sys.stdout.write(str(count_crosses(n, grid)) + "\n")


if __name__ == "__main__":
    main()

