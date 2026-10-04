# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    if not data:
        sys.exit()

    n = data[0]
    arr = data[1:1 + n]

    print("First" if sum(arr) % 2 else "Second")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
