import sys


# --- clause: read_input :: () -> tuple[int, int, list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    grid = []
    pos = 2
    for _ in range(n):
        grid.append(data[pos:pos + m])
        pos += m
    return n, m, grid


# --- clause: build_matrix :: (n: int, m: int, grid: list[list[int]]) -> list[list[int]] ---
def build_matrix(n, m, grid):
    base = 720720
    out = [[base] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (i + j) & 1:
                out[i][j] = base + grid[i][j] ** 4
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, grid = read_input()
    result = build_matrix(n, m, grid)
    sys.stdout.write("\n".join(" ".join(map(str, row)) for row in result) + "\n")


if __name__ == "__main__":
    main()
