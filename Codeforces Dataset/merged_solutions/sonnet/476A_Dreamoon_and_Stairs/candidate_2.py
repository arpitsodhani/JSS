import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[0], tokens[1]


# --- clause: fewest_moves :: (n: int, m: int) -> int ---
def fewest_moves(n, m):
    bottom = (n + 1) // 2
    for moves in range(bottom, n + 1):
        if moves % m == 0:
            return moves
    return -1


# --- clause: main :: () -> None ---
def main():
    n, m = read_input()
    sys.stdout.write("%d\n" % fewest_moves(n, m))


if __name__ == "__main__":
    main()
