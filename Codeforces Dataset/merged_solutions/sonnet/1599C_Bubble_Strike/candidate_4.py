# CLAUSE: setup_environment
import sys
from math import comb

# CLAUSE: solve_logic
def contribution(n, k):
    total = comb(n, 3)
    studied = k
    unstudied = n - k
    parts = [
        (studied >= 1 and unstudied >= 2, comb(studied, 1) * comb(unstudied, 2), 0.5),
        (studied >= 2 and unstudied >= 1, comb(studied, 2) * comb(unstudied, 1), 1.0),
        (studied >= 3, comb(studied, 3), 1.0),
    ]
    result = 0.0
    for active, ways, weight in parts:
        if active:
            result += ways * weight / total
    return result

def solve(n, p):
    candidates = range(n + 1)
    for k in candidates:
        if contribution(n, k) + 1e-9 >= p:
            return k
    return n

# CLAUSE: finish_program
n_text, p_text = sys.stdin.read().strip().split()
print(solve(int(n_text), float(p_text)))
