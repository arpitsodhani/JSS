# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
out = []
for _ in range(t):
    n = data[idx]
    k = data[idx + 1]
    idx += 2
    gold = 0
    ans = 0
    for _ in range(n):
        a = data[idx]
        idx += 1
        if a >= k:
            gold += a
        elif a == 0 and gold > 0:
            gold -= 1
            ans += 1
    out.append(str(ans))
print('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
