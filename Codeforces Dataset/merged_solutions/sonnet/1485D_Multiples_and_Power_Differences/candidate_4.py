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
    out = []
    for i, row in enumerate(grid):
        line = []
        for j, value in enumerate(row):
            if (i + j) % 2:
                line.append(base + value ** 4)
            else:
                line.append(base)
        out.append(line)
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, grid = read_input()
    result = build_matrix(n, m, grid)
    sys.stdout.write("\n".join(" ".join(map(str, row)) for row in result) + "\n")


if __name__ == "__main__":
    main()
