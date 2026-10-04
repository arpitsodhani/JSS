import sys

def solve_case(n, x, y, a, b):
    # CLAUSE: collect_mismatch_positions
    diff = []
    for i in range(n):
        if a[i] != b[i]:
            diff.append(i)

    # CLAUSE: validate_parity_feasibility
    m = len(diff)
    if m % 2 == 1:
        return -1

    # CLAUSE: handle_zero_distance_case
    if m == 0:
        return 0

    # CLAUSE: classify_two_mismatch_case
    two_mismatches = m == 2

    # CLAUSE: price_adjacent_pair_exception
    if two_mismatches and diff[1] == diff[0] + 1:
        if n == 2:
            return x
        return min(x, 2 * y)

    # CLAUSE: compute_bulk_pairing_cost
    bulk_cost = (m // 2) * y

    # CLAUSE: select_minimum_total_cost
    return bulk_cost

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        x = int(data[pos + 1])
        y = int(data[pos + 2])
        a = data[pos + 3]
        b = data[pos + 4]
        pos += 5
        out.append(str(solve_case(n, x, y, a, b)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
