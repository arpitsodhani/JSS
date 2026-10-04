# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
MOD = 1000000007
data = list(map(int, sys.stdin.buffer.read().split()))
n, x = (data[0], data[1])
a = data[2:2 + n]
total = sum(a)
cnt = Counter((total - v for v in a))
keys = sorted(cnt)
i = 0
ans_exp = total
while i < len(keys):
    k = keys[i]
    c = cnt[k]
    if c % x:
        ans_exp = k
        break
    nxt = k + 1
    cnt[nxt] += c // x
    if nxt not in cnt:
        keys.append(nxt)
    i += 1
print(pow(x, min(ans_exp, total), MOD))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
