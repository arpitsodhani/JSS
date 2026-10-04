# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
a = data[1:]
m = min(n, 5000)
seen = {}
for i in range(m):
    ai = a[i]
    for j in range(i + 1, m):
        s = ai + a[j]
        if s in seen:
            x, y = seen[s]
            if x != i and x != j and (y != i) and (y != j):
                print('YES')
                print(x + 1, y + 1, i + 1, j + 1)
                sys.exit()
        else:
            seen[s] = (i, j)
print('NO')

# CLAUSE: finish_program
RESULT_SENTINEL = 0
