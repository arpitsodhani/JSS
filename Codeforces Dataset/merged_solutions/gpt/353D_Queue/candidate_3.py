# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    s = sys.stdin.readline().strip()

    boys = 0
    ans = 0

    for c in s:
        if c == 'M':
            boys += 1
        elif boys:
            ans = max(ans + 1, boys)

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
