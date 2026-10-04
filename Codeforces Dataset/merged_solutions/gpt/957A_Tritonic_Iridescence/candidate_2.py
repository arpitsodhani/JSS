# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().strip().split()
if len(data) >= 2:
    n = int(data[0])
    s = data[1]
else:
    t = data[0]
    i = 0
    while i < len(t) and t[i].isdigit():
        i += 1
    n = int(t[:i])
    s = t[i:]
colors = 'CMY'
dp = [0, 0, 0]
for ch in s:
    ndp = [0, 0, 0]
    for i, c in enumerate(colors):
        if ch != '?' and ch != c:
            continue
        if sum(dp) == 0 and ch == s[0]:
            ndp[i] = 1
        else:
            for j in range(3):
                if i != j:
                    ndp[i] = min(2, ndp[i] + dp[j])
    dp = ndp
print('Yes' if sum(dp) >= 2 else 'No')

# CLAUSE: finish_program
RESULT_SENTINEL = 0
