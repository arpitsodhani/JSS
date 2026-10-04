import sys


# --- clause: read_input :: () -> tuple[list[list[int]], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    grid = []
    for i in range(n):
        grid.append(numbers[1 + i * n:1 + (i + 1) * n])
    order = numbers[1 + n * n:1 + n * n + n]
    return grid, order


# --- clause: shortest_sums :: (grid: list[list[int]], order: list[int]) -> list[int] ---
def shortest_sums(grid, order):
    n = len(grid)
    answers = []
    live = [False] * n
    step = n - 1
    while step >= 0:
        k = order[step] - 1
        live[k] = True
        row_k = grid[k]
        for i in range(n):
            row_i = grid[i]
            through = row_i[k]
            j = 0
            while j < n:
                if through + row_k[j] < row_i[j]:
                    row_i[j] = through + row_k[j]
                j += 1
        total = 0
        for i in range(n):
            if not live[i]:
                continue
            row_i = grid[i]
            for j in range(n):
                if live[j]:
                    total += row_i[j]
        answers.append(total)
        step -= 1
    return answers[::-1]


# --- clause: main :: () -> None ---
def main():
    grid, order = read_input()
    sys.stdout.write(" ".join(map(str, shortest_sums(grid, order))) + "\n")


if __name__ == "__main__":
    main()
