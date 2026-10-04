# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]
    b = data[1 + n:1 + 2 * n]

    top = bottom = none = 0

    for x, y in zip(a, b):
        ntop = x + max(bottom, none)
        nbottom = y + max(top, none)
        nnone = max(none, top, bottom)
        top, bottom, none = ntop, nbottom, nnone

    print(max(top, bottom, none))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
