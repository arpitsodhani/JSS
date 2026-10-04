# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:1 + n]
s, f = (data[1 + n], data[2 + n])
length = f - s
arr = a + a
cur = sum(arr[s - 1:f - 1])
best = cur
ans = 1
for x in range(2, n + 1):
    left = (s - x) % n
    right = left + length - 1
    cur = sum(arr[left:right + 1])
    if cur > best:
        best = cur
        ans = x
print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
