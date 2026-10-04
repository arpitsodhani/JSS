import sys


# --- clause: read_input :: () -> tuple[int, list[list[str]]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    pieces = []
    at = 1
    for _ in range(4):
        pieces.append([tokens[at + i].decode() for i in range(n)])
        at += n
    return n, pieces


# --- clause: piece_costs :: (n: int, pieces: list[list[str]]) -> list[tuple[int, int]] ---
def piece_costs(n, pieces):
    rows = []
    for grid in pieces:
        wrong = 0
        for i in range(n):
            for j in range(n):
                want = "0" if (i + j) % 2 == 0 else "1"
                if grid[i][j] != want:
                    wrong += 1
        rows.append((wrong, n * n - wrong))
    return rows


# --- clause: cheapest_board :: (rows: list[tuple[int, int]]) -> int ---
def cheapest_board(rows):
    best = 1 << 62
    for mask in range(16):
        if bin(mask).count("1") != 2:
            continue
        here = 0
        for i in range(4):
            here += rows[i][0] if (mask >> i) & 1 else rows[i][1]
        if here < best:
            best = here
    return best


# --- clause: main :: () -> None ---
def main():
    n, pieces = read_input()
    sys.stdout.write("%d\n" % cheapest_board(piece_costs(n, pieces)))


if __name__ == "__main__":
    main()
