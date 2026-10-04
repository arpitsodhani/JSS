import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[0], tokens[1], tokens[2], tokens[3]


# --- clause: piece_moves :: (r1: int, c1: int, r2: int, c2: int) -> tuple[int, int, int] ---
def piece_moves(r1, c1, r2, c2):
    rook = 1 if (r1 == r2 or c1 == c2) else 2
    if (r1 + c1) % 2 != (r2 + c2) % 2:
        bishop = 0
    elif abs(r1 - r2) == abs(c1 - c2):
        bishop = 1
    else:
        bishop = 2
    king = abs(r1 - r2)
    if abs(c1 - c2) > king:
        king = abs(c1 - c2)
    return rook, bishop, king


# --- clause: main :: () -> None ---
def main():
    r1, c1, r2, c2 = read_input()
    sys.stdout.write("%d %d %d\n" % piece_moves(r1, c1, r2, c2))


if __name__ == "__main__":
    main()
