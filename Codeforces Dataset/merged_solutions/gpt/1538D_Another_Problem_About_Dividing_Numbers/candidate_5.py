import sys
import math

# CLAUSE: factorize_prime_multiplicity
def factorize_prime_multiplicity(n):
    twos = 0
    while not n & 1:
        twos += 1
        n >>= 1
    total = twos
    d = 3
    while d <= n // d:
        while n % d == 0:
            total += 1
            n //= d
        d += 2
    if n > 1:
        total += 1
    return total

# CLAUSE: extract_gcd_core
def extract_gcd_core(a, b):
    return math.gcd(a, b)

# CLAUSE: measure_asymmetric_reduction
def measure_asymmetric_reduction(a, b, g):
    return [a // g, b // g]

# CLAUSE: derive_minimum_turns
def derive_minimum_turns(remainders):
    return len([x for x in remainders if x > 1])

# CLAUSE: derive_maximum_turns
def derive_maximum_turns(a, b):
    first_capacity = factorize_prime_multiplicity(a)
    second_capacity = factorize_prime_multiplicity(b)
    return first_capacity + second_capacity

# CLAUSE: handle_single_turn_case
def handle_single_turn_case(a, b):
    divisible = a % b == 0 or b % a == 0
    return a != b and divisible

# CLAUSE: decide_exact_k_feasibility
def decide_exact_k_feasibility(a, b, k):
    g = extract_gcd_core(a, b)
    remainders = measure_asymmetric_reduction(a, b, g)
    lower_bound = derive_minimum_turns(remainders)
    upper_bound = derive_maximum_turns(a, b)
    if k == 1:
        ok = handle_single_turn_case(a, b)
    else:
        ok = lower_bound <= k <= upper_bound
    return ok

def main():
    values = sys.stdin.buffer.read().split()
    cases = int(values[0])
    lines = []
    p = 1
    for _ in range(cases):
        a, b, k = map(int, values[p:p + 3])
        p += 3
        lines.append("YES" if decide_exact_k_feasibility(a, b, k) else "NO")
    sys.stdout.write("\n".join(lines))

main()
