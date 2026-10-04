# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []

for n in data[1:1 + t]:
    ans.append(str((n // 15) * 3 + min(n % 15 + 1, 3)))

print("\n".join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
