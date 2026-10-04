# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(values, limit):
    taken = [True] * len(values)
    kept = len(values)
    for i, current in enumerate(values):
        if i > 0 and taken[i - 1] and current + values[i - 1] < limit * 2:
            taken[i] = False
            kept -= 1
        elif i > 1 and taken[i - 1] and taken[i - 2] and current + values[i - 1] + values[i - 2] < limit * 3:
            taken[i] = False
            kept -= 1
    return kept

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    tests = int(next(it))
    out = []
    for _ in range(tests):
        n = int(next(it))
        arr = [int(next(it)) for _ in range(n)]
        x = int(next(it))
        out.append(str(solve_case(arr, x)))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
main()
