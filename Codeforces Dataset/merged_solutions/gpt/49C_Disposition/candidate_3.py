# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    n = int(sys.stdin.readline())
    ans = list(range(2, n + 1)) + [1]
    print(*ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
