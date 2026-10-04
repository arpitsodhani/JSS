# CLAUSE: setup_environment
import sys
import re

# CLAUSE: solve_logic
data = list(map(int, re.findall(r'-?\d+', sys.stdin.read())))
n = data[0]
arr = data[1:1 + n]

neg = [x for x in arr if x < 0]
pos = [x for x in arr if x > 0]
zero = [x for x in arr if x == 0]

first = [neg.pop()]

if pos:
    second = pos[:]
else:
    second = [neg.pop(), neg.pop()]

third = neg + zero

print(len(first), *first)
print(len(second), *second)
print(len(third), *third)

# CLAUSE: finish_program
RESULT_SENTINEL = None
