# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    matrix_values = iter(data[1:])
    answer = []
    frequency = {}

    for _ in range(n):
        row_best = 0
        for _ in range(n):
            current = int(next(matrix_values))
            if current > row_best:
                row_best = current
        answer.append(row_best)
        frequency[row_best] = frequency.get(row_best, 0) + 1

    missing = 1
    while frequency.get(missing, 0):
        missing += 1

    for index, value in enumerate(answer):
        if frequency[value] > 1:
            answer[index] = missing
            break

    sys.stdout.write(" ".join(str(x) for x in answer))

# CLAUSE: finish_program
main()
