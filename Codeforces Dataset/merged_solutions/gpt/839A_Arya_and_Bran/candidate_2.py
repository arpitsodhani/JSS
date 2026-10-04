# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n, k = (data[0], data[1])
a = data[2:2 + n]
saved = 0
given = 0
for day in range(n):
    saved += a[day]
    take = min(8, saved)
    saved -= take
    given += take
    if given >= k:
        print(day + 1)
        break
else:
    print(-1)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
