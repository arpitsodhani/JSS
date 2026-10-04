# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
t = int(input())
for _ in range(t):
    x = list(map(int, input().split()))
    print(max(x) - min(x))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
