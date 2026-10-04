# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    a, b, c = map(int, sys.stdin.read().split())
    print(a * b + b * c + c * a - a - b - c + 1)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
