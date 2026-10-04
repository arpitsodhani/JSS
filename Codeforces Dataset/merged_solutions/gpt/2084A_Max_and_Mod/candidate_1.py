import sys

# CLAUSE: detect_parity_feasibility
def detect_parity_feasibility(n):
    return n % 2 == 1

# CLAUSE: justify_even_impossibility
def justify_even_impossibility(n):
    return not detect_parity_feasibility(n)

# CLAUSE: choose_peak_placement
def choose_peak_placement(n):
    if n == 1:
        return [1]
    return [n]

# CLAUSE: construct_odd_permutation
def construct_odd_permutation(n):
    if n == 1:
        return [1]
    return choose_peak_placement(n) + list(range(1, n))

# CLAUSE: verify_adjacent_mod_conditions
def verify_adjacent_mod_conditions(p):
    n = len(p)
    return sorted(p) == list(range(1, n + 1)) and all(max(p[i - 2], p[i - 1]) % i == i - 1 for i in range(2, n + 1))

# CLAUSE: emit_case_result
def emit_case_result(n):
    if justify_even_impossibility(n):
        return "-1"
    p = construct_odd_permutation(n)
    return " ".join(map(str, p))

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    cases = data[1:] if len(data) > 1 and data[0] == len(data) - 1 else data
    sys.stdout.write("\n".join(emit_case_result(n) for n in cases))

if __name__ == "__main__":
    main()
