# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from math import gcd

    n, k = map(int, sys.stdin.readline().split())
    a, b = map(int, sys.stdin.readline().split())

    total = n * k
    mn = 10**30
    mx = 0

    for d in (a + b, abs(a - b)):
        for r in (d, k - d):
            if r == 0:
                g = k
            else:
                g = gcd(total, r)
            stops = total // g
            mn = min(mn, stops)
            mx = max(mx, stops)

    print(mn, mx)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
