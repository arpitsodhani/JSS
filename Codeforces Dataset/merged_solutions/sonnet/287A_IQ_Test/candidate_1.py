import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return [row.decode() for row in data[:4]]


# --- clause: has_square :: (grid: list[str]) -> str ---
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


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(has_square(read_input()) + "\n")


if __name__ == "__main__":
    main()
