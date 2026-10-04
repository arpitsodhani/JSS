# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    n = int(sys.stdin.readline())
    if n % 2:
        print("a" * (n // 2) + "b" + "a" * (n // 2))
    else:
        print("a" * (n // 2 - 1) + "b" + "a" * (n // 2) + "c")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
