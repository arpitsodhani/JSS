# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 998244353

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
out = []

for _ in range(t):
    n = data[idx]
    idx += 1
    dp1 = 0
    dp12 = 0
    ans = 0

    for x in data[idx:idx + n]:
        if x == 1:
            dp1 = (dp1 + 1) % MOD
        elif x == 2:
            dp12 = (dp12 * 2 + dp1) % MOD
        else:
            ans = (ans + dp12) % MOD

    idx += n
    out.append(str(ans))

sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
