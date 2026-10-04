import sys


# --- clause: read_input :: () -> tuple[int, list[str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return n, [data[1 + i].decode() for i in range(n)]


# --- clause: count_crosses :: (n: int, grid: list[str]) -> int ---
def count_crosses(n, grid):
    marks = [[ch == "X" for ch in row] for row in grid]
    found = 0
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if (marks[i][j] and marks[i - 1][j - 1] and marks[i - 1][j + 1]
                    and marks[i + 1][j - 1] and marks[i + 1][j + 1]):
                found += 1
    return found

# --- clause: main :: () -> None ---
def main():
    n, grid = read_input()
    sys.stdout.write(str(count_crosses(n, grid)) + "\n")


if __name__ == "__main__":
    main()
