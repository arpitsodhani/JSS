import sys

# CLAUSE: detect_parity_feasibility
def detect_parity_feasibility(n):
    feasible = n % 2 != 0
    return feasible

# CLAUSE: justify_even_impossibility
def justify_even_impossibility(n):
    last_requirement_blocks_even_peak = n % 2 == 0
    return last_requirement_blocks_even_peak

# CLAUSE: choose_peak_placement
def choose_peak_placement(n):
    peak_index = 0 if n > 1 else None
    return peak_index

# CLAUSE: construct_odd_permutation
def construct_odd_permutation(n):
    permutation = list(range(1, n + 1))
    peak_index = choose_peak_placement(n)
    if peak_index is not None:
        permutation[0], permutation[-1] = permutation[-1], permutation[0]
        tail = permutation[1:]
        tail.sort()
        permutation[1:] = tail
    return permutation

# CLAUSE: verify_adjacent_mod_conditions
def verify_adjacent_mod_conditions(permutation):
    expected = set(range(1, len(permutation) + 1))
    if set(permutation) != expected:
        return False
    checks = (
        max(permutation[i - 2], permutation[i - 1]) % i == i - 1
        for i in range(2, len(permutation) + 1)
    )
    return all(checks)

# CLAUSE: emit_case_result
def emit_case_result(n):
    if justify_even_impossibility(n):
        return "-1"
    permutation = construct_odd_permutation(n)
    return " ".join(map(str, permutation))

def read_cases():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if len(values) >= 2 and values[0] + 1 == len(values):
        return values[1:]
    return values

sys.stdout.write("\n".join(emit_case_result(n) for n in read_cases()))
