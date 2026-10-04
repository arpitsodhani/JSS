import sys

def mismatch_positions(a, b):
    res = []
    for idx, pair in enumerate(zip(a, b)):
        if pair[0] != pair[1]:
            res.append(idx)
    return res

def answer(n, x, y, a, b):
    # CLAUSE: collect_mismatch_positions
    mismatches = mismatch_positions(a, b)
    count = len(mismatches)

    # CLAUSE: validate_parity_feasibility
    possible = (count & 1) == 0
    if not possible:
        return -1

    # CLAUSE: handle_zero_distance_case
    if count < 1:
        return 0

    # CLAUSE: classify_two_mismatch_case
    exactly_two = count == 2
    adjacent = exactly_two and mismatches[0] + 1 == mismatches[1]

    # CLAUSE: price_adjacent_pair_exception
    if adjacent:
        direct = x
        indirect = 2 * y
        return direct if n == 2 else min(direct, indirect)

    # CLAUSE: compute_bulk_pairing_cost
    pairs = count // 2
    total = pairs * y

    # CLAUSE: select_minimum_total_cost
    return total

tokens = sys.stdin.buffer.read().split()
tests = int(tokens[0])
at = 1
answers = []
for _ in range(tests):
    n = int(tokens[at])
    x = int(tokens[at + 1])
    y = int(tokens[at + 2])
    a = tokens[at + 3].decode()
    b = tokens[at + 4].decode()
    at += 5
    answers.append(str(answer(n, x, y, a, b)))
sys.stdout.write("\n".join(answers))
