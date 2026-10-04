import sys

# Clause read_input [Confidence: 0.80]
def read_input():
    data = sys.stdin.buffer.read().split()
    return [row.decode() for row in data[:4]]

# Clause has_square [Confidence: 0.80]
def has_square(grid):
    for r in range(3):
        for c in range(3):
            dark = 0
            for dr in range(2):
                for dc in range(2):
                    if grid[r + dr][c + dc] == "#":
                        dark += 1
            if dark != 2:
                return "YES"
    return "NO"

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(has_square(read_input()) + "\n")


if __name__ == "__main__":
    main()

