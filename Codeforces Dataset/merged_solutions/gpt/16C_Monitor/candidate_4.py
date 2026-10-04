# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from math import gcd

    a, b, x, y = map(int, sys.stdin.read().split())

    g = gcd(x, y)
    x //= g
    y //= g

    k = min(a // x, b // y)

    print(x * k, y * k)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
