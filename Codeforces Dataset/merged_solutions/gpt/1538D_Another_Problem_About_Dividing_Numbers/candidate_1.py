import sys
from math import gcd

# CLAUSE: factorize_prime_multiplicity
def factorize_prime_multiplicity(n):
    total = 0
    p = 2
    while p * p <= n:
        while n % p == 0:
            total += 1
            n //= p
        p += 1
    if n > 1:
        total += 1
    return total

# CLAUSE: extract_gcd_core
def extract_gcd_core(a, b):
    return gcd(a, b)

# CLAUSE: measure_asymmetric_reduction
def measure_asymmetric_reduction(a, b, g):
    return a // g > 1, b // g > 1

# CLAUSE: derive_minimum_turns
def derive_minimum_turns(left_needed, right_needed):
    return int(left_needed) + int(right_needed)

# CLAUSE: derive_maximum_turns
def derive_maximum_turns(a, b):
    return factorize_prime_multiplicity(a) + factorize_prime_multiplicity(b)

# CLAUSE: handle_single_turn_case
def handle_single_turn_case(a, b):
    return a != b and (a % b == 0 or b % a == 0)

# CLAUSE: decide_exact_k_feasibility
def decide_exact_k_feasibility(a, b, k):
    g = extract_gcd_core(a, b)
    left_needed, right_needed = measure_asymmetric_reduction(a, b, g)
    minimum = derive_minimum_turns(left_needed, right_needed)
    maximum = derive_maximum_turns(a, b)
    if k == 1:
        return handle_single_turn_case(a, b)
    return minimum <= k <= maximum

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ans = []
    idx = 1
    for _ in range(t):
        a, b, k = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        ans.append("YES" if decide_exact_k_feasibility(a, b, k) else "NO")
    print("\n".join(ans))

if __name__ == "__main__":
    main()
