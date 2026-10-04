# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    n = int(sys.stdin.readline())
    ans = sum(1.0 / i for i in range(1, n + 1))
    print(f"{ans:.12f}")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
