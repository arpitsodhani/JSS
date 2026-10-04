import sys
from bisect import bisect_right

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k, l = data[0], data[1], data[2]
    a = data[3:]

    # CLAUSE: sort_staves
    a.sort()

    # CLAUSE: determine_valid_minimum_window
    limit = a[0] + l
    valid_count = bisect_right(a, limit)

    # CLAUSE: check_barrel_feasibility
    if valid_count < n:
        print(0)
        return

    # CLAUSE: reserve_filler_capacity
    spare_valid = valid_count - n
    index = 0
    answer = 0

    # CLAUSE: select_greedy_minima
    for _ in range(n):
        chosen = a[index]
        can_skip = min(k - 1, spare_valid)
        index += can_skip + 1
        spare_valid -= can_skip

        # CLAUSE: accumulate_volume_sum
        answer += chosen

    print(answer)

main()
