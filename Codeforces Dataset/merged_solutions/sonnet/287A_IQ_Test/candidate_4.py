import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return [bytes(row).decode() for row in data[0:4]]


# --- clause: has_square :: (grid: list[str]) -> str ---
def has_square(grid):
    for r in range(3):
        for c in range(3):
            dark = 0
            for dr in range(2):
                for dc in range(2):
                    if grid[r + dr][c + dc] == "#":
                        dark += 1
            if dark == 2:
                continue
            return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    grid = read_input()
    sys.stdout.write(has_square(grid) + "\n")


if __name__ == "__main__":
    main()
