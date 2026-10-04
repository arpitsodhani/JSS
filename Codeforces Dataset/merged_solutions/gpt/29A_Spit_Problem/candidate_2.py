# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n = data[0]
camels = []
for i in range(n):
    x = data[1 + 2 * i]
    d = data[2 + 2 * i]
    camels.append((x, d))
seen = set(camels)
for x, d in camels:
    if (x + d, -d) in seen:
        print('YES')
        sys.exit()
print('NO')

# CLAUSE: finish_program
RESULT_SENTINEL = 0
