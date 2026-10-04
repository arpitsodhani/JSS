import sys

def evaluate(n, x, y, a, b):
    # CLAUSE: collect_mismatch_positions
    positions = []
    i = 0
    while i < n:
        if a[i] != b[i]:
            positions += [i]
        i += 1

    # CLAUSE: validate_parity_feasibility
    total_bad = len(positions)
    if total_bad & 1:
        return -1

    # CLAUSE: handle_zero_distance_case
    if total_bad == 0:
        return 0

    # CLAUSE: classify_two_mismatch_case
    is_double = total_bad == 2
    gap = positions[1] - positions[0] if is_double else None

    # CLAUSE: price_adjacent_pair_exception
    if is_double and gap == 1:
        if n == 2:
            return x
        via_neighbors = x
        via_other_pairings = y + y
        return min(via_neighbors, via_other_pairings)

    # CLAUSE: compute_bulk_pairing_cost
    ordinary_answer = (total_bad // 2) * y

    # CLAUSE: select_minimum_total_cost
    return ordinary_answer

def main():
    raw = sys.stdin.readline
    t = int(raw())
    output = []
    for _ in range(t):
        n, x, y = map(int, raw().split())
        a = raw().strip()
        b = raw().strip()
        output.append(str(evaluate(n, x, y, a, b)))
    print("\n".join(output))

if __name__ == "__main__":
    main()
