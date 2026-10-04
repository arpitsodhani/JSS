# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n = int(input())
ans = 0
v = 1
while v <= n:
    v <<= 1
    ans += 1
print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
