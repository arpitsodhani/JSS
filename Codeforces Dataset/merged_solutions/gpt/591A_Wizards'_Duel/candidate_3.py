# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(float, sys.stdin.read().split()))
    l, p, q = data
    print(l * p / (p + q))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
