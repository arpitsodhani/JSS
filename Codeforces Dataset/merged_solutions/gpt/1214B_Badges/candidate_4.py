# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    b = int(input())
    g = int(input())
    n = int(input())

    lo = max(0, n - g)
    hi = min(b, n)

    print(max(0, hi - lo + 1))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
