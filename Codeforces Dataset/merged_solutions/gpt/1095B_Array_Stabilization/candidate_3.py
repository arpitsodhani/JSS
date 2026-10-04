# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = sorted(data[1:])

    if n == 2:
        print(0)
    else:
        print(min(a[-2] - a[0], a[-1] - a[1]))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
