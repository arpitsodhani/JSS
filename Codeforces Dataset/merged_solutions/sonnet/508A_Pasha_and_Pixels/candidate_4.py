import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    k = numbers[2]
    moves = []
    for i in range(k):
        moves.append((numbers[3 + 2 * i], numbers[4 + 2 * i]))
    return n, m, moves


# --- clause: losing_move :: (n: int, m: int, moves: list[tuple[int, int]]) -> int ---
def losing_move(n, m, moves):
    black = set()
    for step in range(len(moves)):
        i, j = moves[step]
        black.add((i, j))
        for corner in ((i, j), (i - 1, j), (i, j - 1), (i - 1, j - 1)):
            y, x = corner
            if (y, x) in black and (y + 1, x) in black and (y, x + 1) in black and (y + 1, x + 1) in black:
                return step + 1
    return 0


# --- clause: main :: () -> None ---
def main():
    n, m, moves = read_input()
    sys.stdout.write("%d\n" % losing_move(n, m, moves))


if __name__ == "__main__":
    main()
