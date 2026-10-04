import sys


# --- clause: read_input :: () -> tuple[list[list[int]], list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    grid = []
    for i in range(n):
        grid.append(tokens[1 + i * n:1 + (i + 1) * n])
    order = tokens[1 + n * n:1 + n * n + n]
    return grid, order


# --- clause: shortest_sums :: (grid: list[list[int]], order: list[int]) -> list[int] ---
def shortest_sums(grid, order):
    n = len(grid)
    answers = []
    live = []
    for step in range(n - 1, -1, -1):
        k = order[step] - 1
        live.append(k)
        row_k = grid[k]
        for i in range(n):
            row_i = grid[i]
            through = row_i[k]
            for j in range(n):
                item = through + row_k[j]
                if item < row_i[j]:
                    row_i[j] = item
        total = 0
        for i in live:
            row_i = grid[i]
            for j in live:
                total += row_i[j]
        answers.append(total)
    answers.reverse()
    return answers


# --- clause: main :: () -> None ---
def main():
    grid, order = read_input()
    sys.stdout.write(" ".join(map(str, shortest_sums(grid, order))) + "\n")


if __name__ == "__main__":
    main()
