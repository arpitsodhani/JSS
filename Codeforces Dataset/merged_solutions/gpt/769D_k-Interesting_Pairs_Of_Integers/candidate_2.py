# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n, k = (data[0], data[1])
a = data[2:]
m = 1 << 14
f = [0] * m
for x in a:
    f[x] += 1
h = 1
while h < m:
    step = h << 1
    for i in range(0, m, step):
        for j in range(i, i + h):
            x = f[j]
            y = f[j + h]
            f[j] = x + y
            f[j + h] = x - y
    h = step
for i in range(m):
    f[i] *= f[i]
h = 1
while h < m:
    step = h << 1
    for i in range(0, m, step):
        for j in range(i, i + h):
            x = f[j]
            y = f[j + h]
            f[j] = x + y
            f[j + h] = x - y
    h = step
ans = 0
for x in range(m):
    if x.bit_count() == k:
        ans += f[x] // m
if k == 0:
    ans -= n
print(ans // 2)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
