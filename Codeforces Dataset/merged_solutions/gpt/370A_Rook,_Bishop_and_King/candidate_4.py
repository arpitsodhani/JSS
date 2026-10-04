# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    r1, c1, r2, c2 = map(int, input().split())

    dr = abs(r1 - r2)
    dc = abs(c1 - c2)

    if dr == 0 and dc == 0:
        rook = 0
    elif r1 == r2 or c1 == c2:
        rook = 1
    else:
        rook = 2

    if dr == 0 and dc == 0:
        bishop = 0
    elif (r1 + c1) % 2 != (r2 + c2) % 2:
        bishop = 0
    elif dr == dc:
        bishop = 1
    else:
        bishop = 2

    king = max(dr, dc)

    print(rook, bishop, king)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
