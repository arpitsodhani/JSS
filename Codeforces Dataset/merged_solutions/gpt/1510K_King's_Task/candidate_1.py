# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n = data[0]
p = data[1:]
m = 2 * n

def op_a(arr):
    res = arr[:]
    for i in range(0, m, 2):
        res[i], res[i + 1] = res[i + 1], res[i]
    return res

def op_b(arr):
    return arr[n:] + arr[:n]

cur = list(range(1, m + 1))
ans = None

for d in range(0, 2 * m + 5):
    if cur == p:
        ans = d
        break
    cur = op_a(cur) if d % 2 == 0 else op_b(cur)

cur = list(range(1, m + 1))
for d in range(0, 2 * m + 5):
    if cur == p:
        if ans is None or d < ans:
            ans = d
        break
    cur = op_b(cur) if d % 2 == 0 else op_a(cur)

print(-1 if ans is None else ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
