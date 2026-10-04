# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def is_leap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
y = int(sys.stdin.readline())
target = is_leap(y)
shift = 0
x = y
while True:
    shift = (shift + (366 if is_leap(x) else 365)) % 7
    x += 1
    if shift == 0 and is_leap(x) == target:
        print(x)
        break

# CLAUSE: finish_program
RESULT_SENTINEL = 0
