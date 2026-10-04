import sys

# CLAUSE: detect_parity_feasibility
def detect_parity_feasibility(n):
    return n == 1 or n % 2 == 1

# CLAUSE: justify_even_impossibility
def justify_even_impossibility(n):
    return n % 2 == 0

# CLAUSE: choose_peak_placement
def choose_peak_placement(n):
    front = [n]
    suffix_start = 1
    return front, suffix_start

# CLAUSE: construct_odd_permutation
def construct_odd_permutation(n):
    if n == 1:
        return [1]
    front, suffix_start = choose_peak_placement(n)
    suffix = [x for x in range(suffix_start, n)]
    return front + suffix

# CLAUSE: verify_adjacent_mod_conditions
def verify_adjacent_mod_conditions(p):
    n = len(p)
    if len(p) != len(set(p)):
        return False
    for i, pair in enumerate(zip(p, p[1:]), start=2):
        if max(pair) % i != i - 1:
            return False
    return n == 0 or min(p) == 1 and max(p) == n

# CLAUSE: emit_case_result
def emit_case_result(n):
    possible = detect_parity_feasibility(n)
    if not possible:
        return "-1"
    p = construct_odd_permutation(n)
    return " ".join(str(x) for x in p)

def main():
    numbers = list(map(int, sys.stdin.read().split()))
    if not numbers:
        return
    if numbers[0] == len(numbers) - 1:
        numbers = numbers[1:]
    lines = []
    for n in numbers:
        lines.append(emit_case_result(n))
    sys.stdout.write("\n".join(lines))

main()
