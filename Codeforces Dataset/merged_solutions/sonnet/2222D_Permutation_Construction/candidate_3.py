# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_permutation(values):
    running = 0
    pairs = []
    for index, number in enumerate(values):
        pairs.append((running, index))
        running += number
    pairs.sort(key=lambda item: item[0])
    result = [0] * len(values)
    for rank, item in enumerate(pairs):
        result[item[1]] = len(values) - rank
    return result

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    where = 1
    output = []
    for _ in range(tokens[0]):
        n = tokens[where]
        where += 1
        arr = tokens[where:where + n]
        where += n
        output.append(" ".join(str(x) for x in build_permutation(arr)))
    print("\n".join(output))

# CLAUSE: finish_program
main()
