import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1]


# --- clause: fewest_moves :: (n: int, m: int) -> int ---
def fewest_moves(n, m):
    low = (n + 1) // 2
    moves = (low + m - 1) // m * m
    return moves if moves <= n else -1


# --- clause: main :: () -> None ---
def main():
    n, m = read_input()
    sys.stdout.write("%d\n" % fewest_moves(n, m))


if __name__ == "__main__":
    main()
