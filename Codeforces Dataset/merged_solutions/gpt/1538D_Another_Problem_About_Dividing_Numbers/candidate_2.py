import sys
import math

# CLAUSE: factorize_prime_multiplicity
def factorize_prime_multiplicity(value):
    amount = 0
    while value % 2 == 0:
        amount += 1
        value //= 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            value //= divisor
            amount += 1
        else:
            divisor += 2
    return amount + (1 if value > 1 else 0)

# CLAUSE: extract_gcd_core
def extract_gcd_core(first, second):
    return math.gcd(first, second)

# CLAUSE: measure_asymmetric_reduction
def measure_asymmetric_reduction(first, second, core):
    reduced = (first // core, second // core)
    return tuple(part != 1 for part in reduced)

# CLAUSE: derive_minimum_turns
def derive_minimum_turns(asymmetry):
    moves = 0
    for flag in asymmetry:
        if flag:
            moves += 1
    return moves

# CLAUSE: derive_maximum_turns
def derive_maximum_turns(first, second):
    counts = [factorize_prime_multiplicity(first), factorize_prime_multiplicity(second)]
    return sum(counts)

# CLAUSE: handle_single_turn_case
def handle_single_turn_case(first, second):
    if first == second:
        return False
    larger, smaller = (first, second) if first > second else (second, first)
    return larger % smaller == 0

# CLAUSE: decide_exact_k_feasibility
def decide_exact_k_feasibility(first, second, turns):
    core = extract_gcd_core(first, second)
    asymmetry = measure_asymmetric_reduction(first, second, core)
    low = derive_minimum_turns(asymmetry)
    high = derive_maximum_turns(first, second)
    return handle_single_turn_case(first, second) if turns == 1 else low <= turns <= high

def main():
    raw = sys.stdin.buffer.read().split()
    out = []
    for pos in range(1, len(raw), 3):
        a = int(raw[pos])
        b = int(raw[pos + 1])
        k = int(raw[pos + 2])
        out.append("YES" if decide_exact_k_feasibility(a, b, k) else "NO")
    sys.stdout.write("\n".join(out))

main()
