import sys


# --- clause: read_input :: () -> tuple[int, list[str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return n, [data[1 + i].decode() for i in range(n)]


# --- clause: count_crosses :: (n: int, grid: list[str]) -> int ---
def count_crosses(n, grid):
    total = 0
    for i in range(1, n - 1):
        row = grid[i]
        above = grid[i - 1]
        below = grid[i + 1]
        for j in range(1, n - 1):
            if row[j] != "X":
                continue
            if above[j - 1] == "X" and above[j + 1] == "X" and below[j - 1] == "X" and below[j + 1] == "X":
                total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    n, grid = read_input()
    sys.stdout.write(str(count_crosses(n, grid)) + "\n")


if __name__ == "__main__":
    main()
