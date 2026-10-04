# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n = int(input())

ans = (n * n + 1) // 2
print(ans)

for i in range(n):
    row = []
    for j in range(n):
        row.append('C' if (i + j) % 2 == 0 else '.')
    print(''.join(row))

# CLAUSE: finish_program
RESULT_SENTINEL = None
