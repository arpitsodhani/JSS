# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    n = int(sys.stdin.readline())
    r = n % 5

    if r == 0:
        print(0)
    elif r == 1:
        print(1 if n >= 6 else 2)
    elif r == 2:
        print(2)
    elif r == 3:
        print(1)
    else:
        print(2)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
