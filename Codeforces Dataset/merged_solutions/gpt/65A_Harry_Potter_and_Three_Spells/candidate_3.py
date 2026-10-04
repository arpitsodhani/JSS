# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    a, b, c, d, e, f = map(int, sys.stdin.read().split())

    if b * d * f > a * c * e:
        print("Ron")
    else:
        print("Hermione")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
