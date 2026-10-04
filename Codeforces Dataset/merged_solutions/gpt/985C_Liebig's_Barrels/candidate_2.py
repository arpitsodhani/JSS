import sys

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    k = values[1]
    l = values[2]
    staves = values[3:]

    # CLAUSE: sort_staves
    staves = sorted(staves)

    # CLAUSE: determine_valid_minimum_window
    threshold = staves[0] + l
    right = 0
    total = n * k
    while right < total and staves[right] <= threshold:
        right += 1

    # CLAUSE: check_barrel_feasibility
    if right < n:
        sys.stdout.write("0\n")
        return

    # CLAUSE: reserve_filler_capacity
    optional_inside_prefix = right - n
    pos = 0
    result = 0
    barrels_left = n

    # CLAUSE: select_greedy_minima
    while barrels_left:
        result += staves[pos]
        skipped = k - 1
        if skipped > optional_inside_prefix:
            skipped = optional_inside_prefix
        optional_inside_prefix -= skipped
        pos += skipped + 1
        barrels_left -= 1

    # CLAUSE: accumulate_volume_sum
    sys.stdout.write(str(result) + "\n")

main()
