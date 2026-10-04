# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def read_cases():
    nums = tuple(map(int, sys.stdin.buffer.read().split()))
    total = nums[0]
    items = []
    maximum = 1
    index = 1
    for _ in range(total):
        case = nums[index:index + 3]
        index += 3
        items.append(case)
        maximum = max(maximum, case[0] + case[1])
    return items, maximum

def add_axis(answer, fixed_side, changing_side, threshold, inverse):
    first = threshold // fixed_side + 1
    if first <= 0:
        first = 1
    for side in range(first, changing_side):
        answer += inverse[side + threshold // side]
        if answer >= MOD:
            answer -= MOD
    return answer

def main():
    cases, maximum = read_cases()

    inverse = [0] * (maximum + 1)
    inverse[1] = 1
    for i in range(2, maximum + 1):
        inverse[i] = ((MOD - MOD // i) * inverse[MOD % i]) % MOD

    answers = []
    append = answers.append

    for n, m, k in cases:
        threshold = k - 1
        if n * m <= threshold:
            append("0")
            continue

        answer = add_axis(1, n, m, threshold, inverse)
        answer = add_axis(answer, m, n, threshold, inverse)
        append(str(answer % MOD))

    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
