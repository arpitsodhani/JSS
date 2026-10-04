import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1]), int(data[2])


# --- clause: snake_cells :: (n: int, m: int) -> list[tuple[int, int]] ---
def snake_cells(n, m):
    cells = list()
    for row in range(1, n + 1):
        if row % 2 == 1:
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
        if tube + 1 < k:
            piece = cells[at:at + 2]
            at += 2
        else:
            piece = cells[at:]
            at = len(cells)
        flat = [str(len(piece))]
        for cell in piece:
            flat.append(str(cell[0]))
            flat.append(str(cell[1]))
        out.append(" ".join(flat))
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, k = read_input()
    cells = snake_cells(n, m)
    sys.stdout.write("\n".join(split_tubes(k, cells)) + "\n")


if __name__ == "__main__":
    main()
