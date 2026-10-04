# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    a, b = map(int, input().split())

    while a and b:
        if a >= 2 * b:
            a %= 2 * b
        elif b >= 2 * a:
            b %= 2 * a
        else:
            break

    print(a, b)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
