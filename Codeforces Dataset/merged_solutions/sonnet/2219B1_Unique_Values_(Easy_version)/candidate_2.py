# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def read_cases(values):
    if not values:
        return []
    t = values[0]
    index = 1
    cases = []
    valid = True
    for _ in range(t):
        if index >= len(values):
            valid = False
            break
        n = values[index]
        index += 1
        length = 2 * n + 1
        if index + length > len(values):
            valid = False
            break
        cases.append((n, values[index:index + length]))
        index += length
    if valid and index == len(values):
        return cases
    n = values[0]
    arr = values[1:1 + 2 * n + 1]
    if len(arr) == 2 * n + 1:
        return [(n, arr)]
    return []

def solve(values):
    answers = []
    for n, arr in read_cases(values):
        positions = defaultdict(list)
        for i, value in enumerate(arr, 1):
            positions[value].append(i)
        for group in positions.values():
            if len(group) == 3:
                answers.append("{} {} {}".format(group[0], group[1], group[2]))
                break
    return answers

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    sys.stdout.write("\n".join(solve(data)))

if __name__ == "__main__":
    main()
