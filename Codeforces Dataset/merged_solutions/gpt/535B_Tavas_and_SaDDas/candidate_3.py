# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    n = input().strip()

    ans = (1 << len(n)) - 1
    for c in n:
        ans = ans * 2 + (1 if c == '7' else 0)

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
