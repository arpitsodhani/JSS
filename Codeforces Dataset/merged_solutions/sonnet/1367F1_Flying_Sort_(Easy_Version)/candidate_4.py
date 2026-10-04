# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def minimum_moves(n, arr):
    sorted_values = sorted(arr)
    where = {value: index for index, value in enumerate(arr)}
    best = 1
    start = 0
    while start < n:
        end = start + 1
        while end < n and where[sorted_values[end - 1]] < where[sorted_values[end]]:
            end += 1
        size = end - start
        if size > best:
            best = size
        start = end
    return n - best

def main():
    values = sys.stdin.buffer.read().split()
    it = iter(values)
    t = int(next(it))
    answers = []
    for _ in range(t):
        n = int(next(it))
        arr = []
        for _ in range(n):
            arr.append(int(next(it)))
        answers.append(str(minimum_moves(n, arr)))
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
