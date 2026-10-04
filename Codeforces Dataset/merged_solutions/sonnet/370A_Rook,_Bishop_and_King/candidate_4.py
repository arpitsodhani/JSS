import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2], numbers[3]


# --- clause: piece_moves :: (r1: int, c1: int, r2: int, c2: int) -> tuple[int, int, int] ---
def piece_moves(r1, c1, r2, c2):
    down = r2 - r1
    across = c2 - c1
    if down < 0:
        down = -down
    if across < 0:
        across = -across
    rook = 2
    if down == 0 or across == 0:
        rook = 1
    if (down + across) % 2:
        bishop = 0
    elif down == across:
        bishop = 1
    else:
        bishop = 2
    king = down + across - (down if down < across else across)
    return rook, bishop, king


# --- clause: main :: () -> None ---
def main():
    r1, c1, r2, c2 = read_input()
    sys.stdout.write("%d %d %d\n" % piece_moves(r1, c1, r2, c2))


if __name__ == "__main__":
    main()
