# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    import math

    n = int(sys.stdin.readline())

    r = math.isqrt(n)
    ans = -1

    for x in range(max(1, r - 200), r + 1):
        if x * x + sum(map(int, str(x))) * x == n:
            ans = x
            break

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
