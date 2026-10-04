import sys


# --- clause: read_input :: () -> tuple[list[list[int]], list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    grid = []
    for i in range(n):
        grid.append(fields[1 + i * n:1 + (i + 1) * n])
    order = fields[1 + n * n:1 + n * n + n]
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
                element = through + row_k[j]
                if element < row_i[j]:
                    row_i[j] = element
        summed = 0
        for i in live:
            row_i = grid[i]
            for j in live:
                summed += row_i[j]
        answers.append(summed)
    answers.reverse()
    return answers


# --- clause: main :: () -> None ---
def main():
    grid, order = read_input()
    sys.stdout.write(" ".join(map(str, shortest_sums(grid, order))) + "\n")


if __name__ == "__main__":
    main()
