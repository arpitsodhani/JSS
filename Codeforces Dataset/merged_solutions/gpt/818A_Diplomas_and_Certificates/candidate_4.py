# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    n, k = map(int, sys.stdin.read().split())

    d = (n // 2) // (k + 1)
    c = d * k
    r = n - d - c

    print(d, c, r)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
