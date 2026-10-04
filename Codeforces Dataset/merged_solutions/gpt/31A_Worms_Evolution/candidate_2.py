# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()
n = data[0]
a = data[1:1 + n]
for i in range(n):
    for j in range(n):
        if j == i:
            continue
        for k in range(j + 1, n):
            if k == i:
                continue
            if a[i] == a[j] + a[k]:
                print(i + 1, j + 1, k + 1)
                sys.exit()
print(-1)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
