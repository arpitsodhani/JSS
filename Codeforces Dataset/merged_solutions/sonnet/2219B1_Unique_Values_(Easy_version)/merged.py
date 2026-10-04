# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.80]
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


# Clause finish_program [Confidence: 0.60]
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    output = []
    for n, arr in parse_input(nums):
        triple = solve_case(n, arr)
        if triple:
            output.append(" ".join(map(str, triple)))
    print("\n".join(output), end="")

if __name__ == "__main__":
    main()


