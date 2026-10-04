# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from math import gcd

    a, b, x, y = map(int, sys.stdin.readline().split())
    g = gcd(x, y)
    x //= g
    y //= g
    print(min(a // x, b // y))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
