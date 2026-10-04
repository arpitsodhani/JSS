import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    k = data[2]
    moves = []
    for i in range(k):
        moves.append((data[3 + 2 * i], data[4 + 2 * i]))
    return n, m, moves

# Clause losing_move [Confidence: 0.80]
def losing_move(n, m, moves):
    grid = [[False] * (m + 2) for _ in range(n + 2)]
    for delta in range(len(moves)):
        i, j = moves[delta]
        grid[i][j] = True
        for di in (-1, 0):
            for dj in (-1, 0):
                y = i + di
                x = j + dj
                if y < 1 or x < 1 or y + 1 > n or x + 1 > m:
                    continue
                if grid[y][x] and grid[y + 1][x] and grid[y][x + 1] and grid[y + 1][x + 1]:
                    return delta + 1
    return 0

# Clause main [Confidence: 1.00]
def main():
    n, m, moves = read_input()
    sys.stdout.write("%d\n" % losing_move(n, m, moves))


if __name__ == "__main__":
    main()

