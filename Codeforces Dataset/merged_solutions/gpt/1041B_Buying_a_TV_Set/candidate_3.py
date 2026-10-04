# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from math import gcd

    a, b, x, y = map(int, sys.stdin.readline().split())
    g = gcd(x, y)
    x //= g
    y //= g
    print(min(a // x, b // y))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
