# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
t = sys.stdin.readline().strip()
n = len(t)

pi = [0] * n
for i in range(1, n):
    j = pi[i - 1]
    while j > 0 and t[i] != t[j]:
        j = pi[j - 1]
    if t[i] == t[j]:
        j += 1
    pi[i] = j

m = pi[-1] if n else 0

if m > n // 2:
    print("YES")
    print(t[:m])
else:
    print("NO")

# CLAUSE: finish_program
RESULT_SENTINEL = None
