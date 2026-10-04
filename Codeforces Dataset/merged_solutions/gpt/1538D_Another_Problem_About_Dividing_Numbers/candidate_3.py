import sys
from math import gcd

# CLAUSE: factorize_prime_multiplicity
def factorize_prime_multiplicity(n):
    result = 0
    candidate = 2
    while n > 1 and candidate * candidate <= n:
        quotient, remainder = divmod(n, candidate)
        if remainder == 0:
            result += 1
            n = quotient
        else:
            candidate += 1 if candidate == 2 else 2
    if n > 1:
        result += 1
    return result

# CLAUSE: extract_gcd_core
def extract_gcd_core(a, b):
    core = gcd(a, b)
    return core

# CLAUSE: measure_asymmetric_reduction
def measure_asymmetric_reduction(a, b, g):
    left = a // g
    right = b // g
    return {"left": left > 1, "right": right > 1}

# CLAUSE: derive_minimum_turns
def derive_minimum_turns(parts):
    return (1 if parts["left"] else 0) + (1 if parts["right"] else 0)

# CLAUSE: derive_maximum_turns
def derive_maximum_turns(a, b):
    total = 0
    for number in (a, b):
        total += factorize_prime_multiplicity(number)
    return total

# CLAUSE: handle_single_turn_case
def handle_single_turn_case(a, b):
    return (a > b and a % b == 0) or (b > a and b % a == 0)

# CLAUSE: decide_exact_k_feasibility
def decide_exact_k_feasibility(a, b, k):
    if k == 1:
        return handle_single_turn_case(a, b)
    g = extract_gcd_core(a, b)
    required = derive_minimum_turns(measure_asymmetric_reduction(a, b, g))
    available = derive_maximum_turns(a, b)
    return required <= k and k <= available

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    answers = []
    n = tokens[0]
    cursor = 1
    for _ in range(n):
        a = tokens[cursor]
        b = tokens[cursor + 1]
        k = tokens[cursor + 2]
        cursor += 3
        answers.append("YES" if decide_exact_k_feasibility(a, b, k) else "NO")
    sys.stdout.write("\n".join(answers))

main()
