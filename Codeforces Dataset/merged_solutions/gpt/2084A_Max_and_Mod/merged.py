# Clause detect_parity_feasibility [Confidence: 0.80]
import sys

def detect_parity_feasibility(n):
    return n % 2 == 1


# Clause justify_even_impossibility [Confidence: 0.40]
def justify_even_impossibility(n):
    return n % 2 == 0


# Clause choose_peak_placement [Confidence: 0.40]
def choose_peak_placement(n):
    placement = [None] * n
    placement[0] = n
    return placement


# Clause construct_odd_permutation [Confidence: 0.60]
def construct_odd_permutation(n):
    if n == 1:
        return [1]
    placement = choose_peak_placement(n)
    next_value = 1
    for index in range(1, n):
        placement[index] = next_value
        next_value += 1
    return placement


# Clause verify_adjacent_mod_conditions [Confidence: 0.40]
def verify_adjacent_mod_conditions(p):
    n = len(p)
    return sorted(p) == list(range(1, n + 1)) and all(max(p[i - 2], p[i - 1]) % i == i - 1 for i in range(2, n + 1))


# Clause emit_case_result [Confidence: 0.60]
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


