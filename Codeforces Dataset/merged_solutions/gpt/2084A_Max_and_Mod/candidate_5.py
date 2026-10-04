import sys

# CLAUSE: detect_parity_feasibility
def detect_parity_feasibility(n):
    return (n & 1) == 1

# CLAUSE: justify_even_impossibility
def justify_even_impossibility(n):
    blocked_by_parity = (n & 1) == 0
    return blocked_by_parity

# CLAUSE: choose_peak_placement
def choose_peak_placement(n):
    placement = [None] * n
    placement[0] = n
    return placement

# CLAUSE: construct_odd_permutation
def construct_odd_permutation(n):
    if n == 1:
        return [1]
    placement = choose_peak_placement(n)
    next_value = 1
    for index in range(1, n):
        placement[index] = next_value
        next_value += 1
    return placement

# CLAUSE: verify_adjacent_mod_conditions
def verify_adjacent_mod_conditions(p):
    n = len(p)
    if sorted(p) != list(range(1, n + 1)):
        return False
    index = 2
    while index <= n:
        if max(p[index - 2], p[index - 1]) % index != index - 1:
            return False
        index += 1
    return True

# CLAUSE: emit_case_result
def emit_case_result(n):
    if justify_even_impossibility(n):
        return "-1"
    p = construct_odd_permutation(n)
    return " ".join(map(str, p))

data = sys.stdin.buffer.read().split()
values = [int(item) for item in data]
if values:
    case_values = values[1:] if len(values) - 1 == values[0] else values
    output = [emit_case_result(n) for n in case_values]
    sys.stdout.write("\n".join(output))
