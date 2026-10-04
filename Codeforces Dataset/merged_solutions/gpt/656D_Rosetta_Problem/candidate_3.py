# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    s = sys.stdin.read().strip()
    n = int(s)

    ans = 0
    while n:
        if n % 8 == 1:
            ans += 1
        n //= 8

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
