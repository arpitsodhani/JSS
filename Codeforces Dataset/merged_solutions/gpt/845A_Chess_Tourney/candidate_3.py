# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    ratings = sorted(data[1:])

    print("YES" if ratings[n] > ratings[n - 1] else "NO")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
