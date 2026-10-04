# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n, m = map(int, sys.stdin.read().split())

if m % n != 0:
    print(-1)
else:
    x = m // n
    moves = 0

    while x % 2 == 0:
        x //= 2
        moves += 1

    while x % 3 == 0:
        x //= 3
        moves += 1

    print(moves if x == 1 else -1)

# CLAUSE: finish_program
RESULT_SENTINEL = None
