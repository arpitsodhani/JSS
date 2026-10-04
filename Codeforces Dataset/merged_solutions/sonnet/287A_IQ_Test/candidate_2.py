import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return [str(row, "ascii") for row in data[:4]]


# --- clause: has_square :: (grid: list[str]) -> str ---
def has_square(grid):
    for r in range(3):
        for c in range(3):
            block = grid[r][c] + grid[r][c + 1] + grid[r + 1][c] + grid[r + 1][c + 1]
            if block.count("#") != 2:
                return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%s\n" % has_square(read_input()))


if __name__ == "__main__":
    main()
