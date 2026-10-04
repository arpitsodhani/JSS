# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
a = data[1:1 + n]
best_time = 10 ** 30
answer = 1
for i, x in enumerate(a):
    first = i
    if x <= first:
        t = first
    else:
        t = first + (x - first + n - 1) // n * n
    if t < best_time:
        best_time = t
        answer = i + 1
print(answer)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
