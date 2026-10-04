import sys

def prefixes(commands):
    values = []
    total = 0
    for command in commands:
        total += 1 if command == "R" else -1
        values.append(total)
    return values

def first_index(values, target):
    for pos, value in enumerate(values, 1):
        if value == target:
            return pos
    return 0

def solve_one(n, x, k, s):
    # CLAUSE: compute_prefix_displacements
    movement = prefixes(s)

    # CLAUSE: locate_initial_zero_hit
    first_touch = first_index(movement, -x)

    # CLAUSE: derive_cycle_zero_hit
    zero_period = first_index(movement, 0)

    # CLAUSE: account_first_execution
    total = 0
    left = k
    if first_touch and first_touch <= left:
        total += 1
        left -= first_touch
    else:
        left = -1

    # CLAUSE: count_reset_cycles
    if left >= 0 and zero_period:
        total += left // zero_period

    # CLAUSE: handle_stop_condition
    return total

def main():
    tokens = sys.stdin.buffer.read().split()
    cases = int(tokens[0])
    answer = []
    at = 1
    for _ in range(cases):
        n = int(tokens[at])
        x = int(tokens[at + 1])
        k = int(tokens[at + 2])
        s = tokens[at + 3].decode()
        at += 4
        answer.append(str(solve_one(n, x, k, s)))
    sys.stdout.write("\n".join(answer))

main()
