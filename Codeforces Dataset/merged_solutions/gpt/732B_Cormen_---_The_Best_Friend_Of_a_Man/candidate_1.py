# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n, k = data[0], data[1]
a = data[2:2 + n]

added = 0
for i in range(n - 1):
    need = k - (a[i] + a[i + 1])
    if need > 0:
        a[i + 1] += need
        added += need

print(added)
print(*a)

# CLAUSE: finish_program
RESULT_SENTINEL = None
