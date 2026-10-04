# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    s = sys.stdin.readline().strip()

    dp0 = dp1 = dp2 = 0

    for c in s:
        if c == 'a':
            dp0 += 1
            dp2 = max(dp1, dp2) + 1
        else:
            dp1 = max(dp0, dp1) + 1

    print(max(dp0, dp1, dp2))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
