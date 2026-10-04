import sys
from bisect import bisect_right

def read_case():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[0], raw[1], raw[2], raw[3:]

def main():
    n, k, l, lengths = read_case()

    # CLAUSE: sort_staves
    lengths.sort()

    # CLAUSE: determine_valid_minimum_window
    bound = lengths[0] + l
    usable_end = bisect_right(lengths, bound, 0, len(lengths))

    # CLAUSE: check_barrel_feasibility
    if usable_end < n:
        print(0)
        return

    # CLAUSE: reserve_filler_capacity
    fillers_available = usable_end - n
    take_positions = []

    # CLAUSE: select_greedy_minima
    cursor = 0
    for barrel_index in range(n):
        take_positions.append(cursor)
        room = min(k - 1, fillers_available)
        fillers_available -= room
        cursor += room + 1

    # CLAUSE: accumulate_volume_sum
    total_volume = sum(lengths[p] for p in take_positions)
    print(total_volume)

main()
