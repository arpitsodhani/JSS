import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1]), int(data[2])


# --- clause: snake_cells :: (n: int, m: int) -> list[tuple[int, int]] ---
def snake_cells(n, m):
    cells = []
    for row in range(1, n + 1):
        if row % 2:
            for col in range(1, m + 1):
                cells.append((row, col))
        else:
            for col in range(m, 0, -1):
                cells.append((row, col))
    return cells


# --- clause: split_tubes :: (k: int, cells: list[tuple[int, int]]) -> list[str] ---
def split_tubes(k, cells):
    out = []
    at = 0
    for tube in range(k):
        if tube == k - 1:
            piece = cells[at:]
            at = len(cells)
        else:
            piece = cells[at:at + 2]
            at += 2
        parts = [str(len(piece))]
        for x, y in piece:
            parts.append(str(x))
            parts.append(str(y))
        out.append(" ".join(parts))
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, k = read_input()
    sys.stdout.write("\n".join(split_tubes(k, snake_cells(n, m))) + "\n")


if __name__ == "__main__":
    main()
