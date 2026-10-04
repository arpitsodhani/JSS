import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    k = raw[2]
    moves = []
    for i in range(k):
        moves.append((raw[3 + 2 * i], raw[4 + 2 * i]))
    return n, m, moves


# --- clause: losing_move :: (n: int, m: int, moves: list[tuple[int, int]]) -> int ---
def losing_move(n, m, moves):
    grid = [[False] * (m + 2) for _ in range(n + 2)]
    for advance in range(0, len(moves)):
        i, j = moves[advance]
        grid[i][j] = True
        for di in (-1, 0):
            for dj in (-1, 0):
                y = i + di
                x = j + dj
                if y < 1 or x < 1 or y + 1 > n or x + 1 > m:
                    continue
                if grid[y][x] and grid[y + 1][x] and grid[y][x + 1] and grid[y + 1][x + 1]:
                    return advance + 1
    return 0


# --- clause: main :: () -> None ---
def main():
    n, m, moves = read_input()
    sys.stdout.write("%d\n" % losing_move(n, m, moves))


if __name__ == "__main__":
    main()
