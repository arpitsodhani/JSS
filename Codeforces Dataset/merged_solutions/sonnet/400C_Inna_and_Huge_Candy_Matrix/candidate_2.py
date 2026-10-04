import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, int, list[tuple[int, int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n, m, x, y, z, p = tokens[:6]
    candies = []
    for i in range(p):
        candies.append((tokens[6 + 2 * i], tokens[7 + 2 * i]))
    return n, m, x % 4, y % 2, z % 4, candies


# --- clause: move_candy :: (n: int, m: int, x: int, y: int, z: int, row: int, col: int) -> tuple[int, int, int, int] ---
def move_candy(n, m, x, y, z, row, col):
    for _ in range(x):
        row, col, n, m = col, n + 1 - row, m, n
    if y:
        col = m + 1 - col
    for _ in range(z):
        row, col, n, m = m + 1 - col, row, m, n
    return n, m, row, col


# --- clause: main :: () -> None ---
def main():
    n, m, x, y, z, candies = read_input()
    lines = []
    for row, col in candies:
        _, _, row, col = move_candy(n, m, x, y, z, row, col)
        lines.append("%d %d" % (row, col))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
