import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, m, k = int(data[0]), int(data[1]), int(data[2])
    return n, m, k


# --- clause: snake_cells :: (n: int, m: int) -> list[tuple[int, int]] ---
def snake_cells(n, m):
    cells = []
    for row in range(1, n + 1):
        columns = range(1, m + 1) if row & 1 else range(m, 0, -1)
        for col in columns:
            cells.append((row, col))
    return cells


# --- clause: split_tubes :: (k: int, cells: list[tuple[int, int]]) -> list[str] ---
def split_tubes(k, cells):
    out = []
    at = 0
    for tube in range(k):
        if tube + 1 < k:
            piece = cells[at:at + 2]
            at += 2
        else:
            piece = cells[at:]
            at = len(cells)
        parts = [str(len(piece))]
        for x, y in piece:
            parts.append(str(x))
            parts.append(str(y))
        out.append(" ".join(parts))
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, k = read_input()
    sys.stdout.write("%s\n" % "\n".join(split_tubes(k, snake_cells(n, m))))


if __name__ == "__main__":
    main()
