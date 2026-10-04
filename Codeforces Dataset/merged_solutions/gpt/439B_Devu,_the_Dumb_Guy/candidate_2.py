# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n, x = (data[0], data[1])
chapters = data[2:2 + n]
chapters.sort()
total = 0
power = x
for c in chapters:
    total += c * power
    if power > 1:
        power -= 1
print(total)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
