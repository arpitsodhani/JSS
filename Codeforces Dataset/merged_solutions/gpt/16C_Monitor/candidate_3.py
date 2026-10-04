# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from math import gcd

    a, b, x, y = map(int, sys.stdin.read().split())

    g = gcd(x, y)
    x //= g
    y //= g

    k = min(a // x, b // y)

    print(x * k, y * k)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
