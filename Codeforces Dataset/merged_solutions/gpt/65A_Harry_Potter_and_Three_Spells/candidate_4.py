# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    a, b, c, d, e, f = map(int, sys.stdin.read().split())

    if b * d * f > a * c * e:
        print("Ron")
    else:
        print("Hermione")

# CLAUSE: finish_program
def main():
    _inner_main()

main()
