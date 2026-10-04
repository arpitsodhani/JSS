# Clause sort_staves [Confidence: 0.80]
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    l = data[2]
    wood = data[3:]

    wood.sort()


# Clause determine_valid_minimum_window [Confidence: 0.40]
    bound = lengths[0] + l
    usable_end = bisect_right(lengths, bound, 0, len(lengths))


# Clause check_barrel_feasibility [Confidence: 0.80]
    if prefix_len < n:
        print(0)
        return


# Clause reserve_filler_capacity [Confidence: 0.80]
    skip_budget = prefix_len - n
    answer = 0
    pointer = 0


# Clause select_greedy_minima [Confidence: 0.60]
    for barrel in range(n):
        answer += wood[pointer]
        step = 1 + min(skip_budget, k - 1)
        skip_budget -= step - 1
        pointer += step


# Clause accumulate_volume_sum [Confidence: 0.60]
    print(answer)

main()


