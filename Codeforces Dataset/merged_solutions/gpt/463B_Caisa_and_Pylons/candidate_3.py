# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    h = data[1:1 + n]
    print(max(h))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
