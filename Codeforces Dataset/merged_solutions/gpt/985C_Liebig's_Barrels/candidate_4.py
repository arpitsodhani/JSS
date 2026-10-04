import sys

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    n, k, l = nums[:3]
    arr = nums[3:]

    # CLAUSE: sort_staves
    arr.sort()

    # CLAUSE: determine_valid_minimum_window
    max_minimum = arr[0] + l
    valid = []
    for x in arr:
        if x > max_minimum:
            break
        valid.append(x)

    # CLAUSE: check_barrel_feasibility
    if len(valid) < n:
        print(0)
        return

    # CLAUSE: reserve_filler_capacity
    surplus = len(valid) - n
    chosen_sum = 0
    i = 0

    # CLAUSE: select_greedy_minima
    for remaining in range(n, 0, -1):
        chosen_sum += valid[i]
        jump = k - 1
        if surplus < jump:
            jump = surplus
        surplus -= jump
        i += jump + 1

    # CLAUSE: accumulate_volume_sum
    print(chosen_sum)

main()
