# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n, l, r = data[0], data[1], data[2]
a = data[3:3 + n]
p = data[3 + n:3 + 2 * n]

order = [0] * n
for i, rank in enumerate(p):
    order[rank - 1] = i

c = [0] * n
prev = -10**30

for i in order:
    low = l - a[i]
    high = r - a[i]
    x = max(low, prev + 1)
    if x > high:
        print(-1)
        sys.exit()
    c[i] = x
    prev = x

print(*[a[i] + c[i] for i in range(n)])

# CLAUSE: finish_program
RESULT_SENTINEL = None
