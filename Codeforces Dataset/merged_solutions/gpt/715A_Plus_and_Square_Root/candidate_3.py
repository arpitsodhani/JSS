# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    n = int(input())
    for i in range(1, n + 1):
        if i == 1:
            print(2)
        else:
            print(i * (i + 1) * (i + 1) - i + 1)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
