# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:]

    p1 = a.index(1) + 1
    pn = a.index(n) + 1

    print(max(p1 - 1, n - p1, pn - 1, n - pn))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
