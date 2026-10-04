import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    rows = []
    for row in data[:4]:
        rows.append(row.decode())
    return rows


# --- clause: has_square :: (grid: list[str]) -> str ---
def has_square(grid):
    for r in range(3):
        for c in range(3):
            cells = [grid[r][c], grid[r][c + 1], grid[r + 1][c], grid[r + 1][c + 1]]
            if len(set(cells)) == 1 or cells.count(cells[0]) == 3 or cells.count(cells[0]) == 1:
                return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    print(has_square(read_input()))


if __name__ == "__main__":
    main()
