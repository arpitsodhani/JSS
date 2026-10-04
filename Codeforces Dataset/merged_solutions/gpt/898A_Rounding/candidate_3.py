# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    n = int(input().strip())
    r = n % 10

    if r <= 5:
        print(n - r)
    else:
        print(n + (10 - r))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
