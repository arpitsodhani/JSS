import sys

def solve_one(n, x, y, a, b):
    # CLAUSE: collect_mismatch_positions
    bad = [i for i in range(n) if a[i] != b[i]]

    # CLAUSE: validate_parity_feasibility
    if len(bad) % 2:
        return -1

    # CLAUSE: handle_zero_distance_case
    if not bad:
        return 0

    # CLAUSE: classify_two_mismatch_case
    only_pair = len(bad) == 2
    touches = only_pair and abs(bad[0] - bad[1]) == 1

    # CLAUSE: price_adjacent_pair_exception
    if touches:
        if n == 2:
            best_for_pair = x
        else:
            best_for_pair = x if x < 2 * y else 2 * y
        return best_for_pair

    # CLAUSE: compute_bulk_pairing_cost
    best_bulk = y * (len(bad) // 2)

    # CLAUSE: select_minimum_total_cost
    return best_bulk

def main():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    res = []
    for _ in range(t):
        n = int(next(it))
        x = int(next(it))
        y = int(next(it))
        a = next(it)
        b = next(it)
        res.append(str(solve_one(n, x, y, a, b)))
    sys.stdout.write("\n".join(res))

main()
