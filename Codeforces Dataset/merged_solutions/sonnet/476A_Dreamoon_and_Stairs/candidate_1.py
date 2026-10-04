import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: fewest_moves :: (n: int, m: int) -> int ---
def fewest_moves(n, m):
    low = (n + 1) // 2
    for moves in range(low, n + 1):
        if moves % m == 0:
            return moves
    return -1


# --- clause: main :: () -> None ---
def main():
    n, m = read_input()
    sys.stdout.write("%d\n" % fewest_moves(n, m))


if __name__ == "__main__":
    main()
