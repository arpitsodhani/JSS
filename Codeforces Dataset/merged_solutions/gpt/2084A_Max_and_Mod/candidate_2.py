import sys

# CLAUSE: detect_parity_feasibility
def detect_parity_feasibility(size):
    return bool(size & 1)

# CLAUSE: justify_even_impossibility
def justify_even_impossibility(size):
    if size & 1:
        return False
    return True

# CLAUSE: choose_peak_placement
def choose_peak_placement(size):
    answer = []
    if size > 1:
        answer.append(size)
    return answer

# CLAUSE: construct_odd_permutation
def construct_odd_permutation(size):
    if size == 1:
        return [1]
    answer = choose_peak_placement(size)
    for value in range(1, size):
        answer.append(value)
    return answer

# CLAUSE: verify_adjacent_mod_conditions
def verify_adjacent_mod_conditions(answer):
    for index in range(2, len(answer) + 1):
        if max(answer[index - 2], answer[index - 1]) % index != index - 1:
            return False
    return len(set(answer)) == len(answer)

# CLAUSE: emit_case_result
def emit_case_result(size):
    if not detect_parity_feasibility(size):
        justify_even_impossibility(size)
        return "-1"
    answer = construct_odd_permutation(size)
    return " ".join(str(value) for value in answer)

tokens = [int(x) for x in sys.stdin.buffer.read().split()]
if tokens:
    tests = tokens[1:] if len(tokens) == tokens[0] + 1 else tokens
    print("\n".join(emit_case_result(size) for size in tests))
