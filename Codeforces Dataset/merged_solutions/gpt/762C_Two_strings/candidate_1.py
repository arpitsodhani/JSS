# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

n = len(a)
m = len(b)

left = [n] * m
p = 0
for i in range(m):
    while p < n and a[p] != b[i]:
        p += 1
    if p < n:
        left[i] = p
        p += 1
    else:
        break

right = [-1] * m
p = n - 1
for i in range(m - 1, -1, -1):
    while p >= 0 and a[p] != b[i]:
        p -= 1
    if p >= 0:
        right[i] = p
        p -= 1
    else:
        break

best_l, best_r = 0, m
j = 0

for i in range(m + 1):
    if i > 0 and left[i - 1] == n:
        break

    if j < i:
        j = i

    prev_pos = -1 if i == 0 else left[i - 1]

    while j < m and right[j] <= prev_pos:
        j += 1

    if j - i < best_r - best_l:
        best_l, best_r = i, j

ans = b[:best_l] + b[best_r:]
print(ans if ans else "-")

# CLAUSE: finish_program
RESULT_SENTINEL = None
