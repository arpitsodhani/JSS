# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []

for n in data[1:1 + t]:
    if n == 1:
        ans.append("1")
    elif n % 2:
        ans.append("-1")
    else:
        p = []
        for i in range(1, n + 1, 2):
            p.append(i + 1)
            p.append(i)
        ans.append(" ".join(map(str, p)))

print("\n".join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
