# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(float, sys.stdin.read().split()))
    l, p, q = data
    print(l * p / (p + q))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
