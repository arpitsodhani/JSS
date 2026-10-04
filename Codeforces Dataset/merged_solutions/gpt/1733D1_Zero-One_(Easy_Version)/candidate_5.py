import sys

def case_cost(n, x, y, a, b):
    # CLAUSE: collect_mismatch_positions
    mismatch_count = 0
    first = -1
    second = -1
    for idx in range(n):
        if a[idx] != b[idx]:
            mismatch_count += 1
            if first == -1:
                first = idx
            elif second == -1:
                second = idx

    # CLAUSE: validate_parity_feasibility
    if mismatch_count % 2 != 0:
        return -1

    # CLAUSE: handle_zero_distance_case
    if mismatch_count == 0:
        return 0

    # CLAUSE: classify_two_mismatch_case
    has_two = mismatch_count == 2
    adjacent_two = has_two and second == first + 1

    # CLAUSE: price_adjacent_pair_exception
    if adjacent_two:
        if n == 2:
            return x
        alternative = 2 * y
        return min(x, alternative)

    # CLAUSE: compute_bulk_pairing_cost
    pair_count = mismatch_count // 2
    cost = pair_count * y

    # CLAUSE: select_minimum_total_cost
    return cost

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    p = 1
    lines = []
    for _ in range(t):
        n = int(data[p])
        x = int(data[p + 1])
        y = int(data[p + 2])
        a = data[p + 3]
        b = data[p + 4]
        p += 5
        lines.append(str(case_cost(n, x, y, a, b)))
    sys.stdout.write("\n".join(lines))

main()
