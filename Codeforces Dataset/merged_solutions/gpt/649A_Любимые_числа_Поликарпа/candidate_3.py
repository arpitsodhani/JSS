# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:1 + n]

    r = 1
    for x in a:
        p = x & -x
        if p > r:
            r = p

    cnt = sum(1 for x in a if x % r == 0)
    print(r, cnt)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
