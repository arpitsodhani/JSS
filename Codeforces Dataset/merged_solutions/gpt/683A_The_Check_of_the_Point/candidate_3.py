# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    a, x, y = map(int, input().split())

    if 0 < x < a and 0 < y < a:
        print(0)
    elif 0 <= x <= a and 0 <= y <= a:
        print(1)
    else:
        print(2)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
