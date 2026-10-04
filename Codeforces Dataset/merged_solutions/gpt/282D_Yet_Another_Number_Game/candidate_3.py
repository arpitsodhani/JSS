# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    import math

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:1 + n]

    win = False

    if n == 1:
        win = a[0] != 0
    elif n == 2:
        x, y = sorted(a)
        d = y - x
        phi = (1 + math.sqrt(5)) / 2
        win = x != int(d * phi)
    else:
        s = 0
        for v in a:
            s ^= v
        win = s != 0

    print("BitLGM" if win else "BitAryo")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
