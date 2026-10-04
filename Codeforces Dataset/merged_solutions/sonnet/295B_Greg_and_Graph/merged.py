import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    grid = []
    for i in range(n):
        grid.append(data[1 + i * n:1 + (i + 1) * n])
    order = data[1 + n * n:1 + n * n + n]
    return grid, order

# Clause shortest_sums [Confidence: 1.00]
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

# Clause main [Confidence: 1.00]
def main():
    grid, order = read_input()
    sys.stdout.write(" ".join(map(str, shortest_sums(grid, order))) + "\n")


if __name__ == "__main__":
    main()

