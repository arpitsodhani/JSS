# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    x = int(input())
    print(x.bit_count())

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
