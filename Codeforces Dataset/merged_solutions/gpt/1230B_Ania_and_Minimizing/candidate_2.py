# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n, k = map(int, input().split())
s = list(input().strip())
if n == 1:
    if k > 0:
        s[0] = '0'
else:
    if k > 0 and s[0] != '1':
        s[0] = '1'
        k -= 1
    for i in range(1, n):
        if k == 0:
            break
        if s[i] != '0':
            s[i] = '0'
            k -= 1
print(''.join(s))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
