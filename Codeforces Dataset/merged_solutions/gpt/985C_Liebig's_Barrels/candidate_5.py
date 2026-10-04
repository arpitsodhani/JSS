import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    l = data[2]
    wood = data[3:]

    # CLAUSE: sort_staves
    wood.sort()

    # CLAUSE: determine_valid_minimum_window
    allowed = wood[0] + l
    lo, hi = 0, len(wood)
    while lo < hi:
        mid = (lo + hi) // 2
        if wood[mid] <= allowed:
            lo = mid + 1
        else:
            hi = mid
    prefix_len = lo

    # CLAUSE: check_barrel_feasibility
    if prefix_len < n:
        print(0)
        return

    # CLAUSE: reserve_filler_capacity
    skip_budget = prefix_len - n
    answer = 0
    pointer = 0

    # CLAUSE: select_greedy_minima
    for barrel in range(n):
        answer += wood[pointer]
        step = 1 + min(skip_budget, k - 1)
        skip_budget -= step - 1
        pointer += step

    # CLAUSE: accumulate_volume_sum
    print(answer)

main()
