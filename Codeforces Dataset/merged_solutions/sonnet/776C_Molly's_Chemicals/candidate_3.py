# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_targets(k):
    if k == 1:
        return (1,)
    if k == -1:
        return (1, -1)
    if k == 0:
        return (1, 0)

    result = []
    value = 1
    border = 10 ** 15
    while -border <= value <= border:
        result.append(value)
        value *= k
    return tuple(result)

def main():
    values = [int(x) for x in sys.stdin.buffer.read().split()]
    n = values[0]
    k = values[1]
    targets = build_targets(k)

    prefix_counts = {0: 1}
    prefix_sum = 0
    answer = 0

    for index in range(n):
        prefix_sum += values[index + 2]
        for need in targets:
            answer += prefix_counts.get(prefix_sum - need, 0)
        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
