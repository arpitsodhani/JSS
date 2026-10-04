# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:1 + n]

    ans = 1
    for i, x in enumerate(a, 1):
        if x > 0:
            ans = max(ans, (x - 1) * n + i)

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
