# Clause collect_mismatch_positions [Confidence: 0.40]
import sys

def solve_case(n, x, y, a, b):

    diff = []
    for i in range(n):
        if a[i] != b[i]:
            diff.append(i)


# Clause validate_parity_feasibility [Confidence: 0.40]
    m = len(diff)
    if m % 2 == 1:
        return -1


# Clause handle_zero_distance_case [Confidence: 0.80]
    if m == 0:
        return 0


# Clause classify_two_mismatch_case [Confidence: 0.40]
    exactly_two = count == 2
    adjacent = exactly_two and mismatches[0] + 1 == mismatches[1]


# Clause price_adjacent_pair_exception [Confidence: 0.40]
    if adjacent_two:
        if n == 2:
            return x
        alternative = 2 * y
        return min(x, alternative)


# Clause compute_bulk_pairing_cost [Confidence: 0.60]
    bulk_cost = (m // 2) * y


# Clause select_minimum_total_cost [Confidence: 0.60]
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


