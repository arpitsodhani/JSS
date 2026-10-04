import sys
from math import gcd

# CLAUSE: factorize_prime_multiplicity
def factorize_prime_multiplicity(n):
    count = 0
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor = 3 if factor == 2 else factor + 2
            continue
        power = 0
        while n % factor == 0:
            n //= factor
            power += 1
        count += power
    if n != 1:
        count += 1
    return count

# CLAUSE: extract_gcd_core
def extract_gcd_core(a, b):
    while b:
        a, b = b, a % b
    return a

# CLAUSE: measure_asymmetric_reduction
def measure_asymmetric_reduction(a, b, g):
    need_a = a != g
    need_b = b != g
    return need_a, need_b

# CLAUSE: derive_minimum_turns
def derive_minimum_turns(need_a, need_b):
    return (need_a + need_b)

# CLAUSE: derive_maximum_turns
def derive_maximum_turns(a, b):
    return factorize_prime_multiplicity(a) + factorize_prime_multiplicity(b)

# CLAUSE: handle_single_turn_case
def handle_single_turn_case(a, b):
    if a == b:
        return False
    return max(a, b) % min(a, b) == 0

# CLAUSE: decide_exact_k_feasibility
def decide_exact_k_feasibility(a, b, k):
    g = extract_gcd_core(a, b)
    need_a, need_b = measure_asymmetric_reduction(a, b, g)
    least = derive_minimum_turns(need_a, need_b)
    most = derive_maximum_turns(a, b)
    if k == 1:
        return handle_single_turn_case(a, b)
    if k < least:
        return False
    if k > most:
        return False
    return True

def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(it)
    output = []
    for _ in range(t):
        a = next(it)
        b = next(it)
        k = next(it)
        output.append("YES" if decide_exact_k_feasibility(a, b, k) else "NO")
    print(*output, sep="\n")

if __name__ == "__main__":
    main()
