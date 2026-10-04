# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10 ** 9 + 7

data = list(map(int, sys.stdin.read().split()))
n, p = data[0], data[1]
c = data[2:2 + n]

pow2 = [1] * (n + 1)
for i in range(1, n + 1):
    pow2[i] = pow2[i - 1] * 2 % MOD

dp = [[0] * 3 for _ in range(3)]
dp[0][0] = 1

def add_state(x):
    if x == 0:
        return 1
    if x == 1:
        return 2
    return 1

for i in range(1, n + 1):
    ndp = [[0] * 3 for _ in range(3)]
    colors = (0, 1) if c[i - 1] == -1 else (c[i - 1],)

    for ob in range(3):
        for ow in range(3):
            cur = dp[ob][ow]
            if cur == 0:
                continue

            for color in colors:
                opp = ow if color == 0 else ob

                if opp == 0:
                    ways = pow2[i - 1]
                    nob, now = ob, ow
                    if color == 0:
                        nob = add_state(nob)
                    else:
                        now = add_state(now)
                    ndp[nob][now] = (ndp[nob][now] + cur * ways) % MOD
                else:
                    ways = pow2[i - 2]
                    ndp[ob][ow] = (ndp[ob][ow] + cur * ways) % MOD

                    nob, now = ob, ow
                    if color == 0:
                        nob = add_state(nob)
                    else:
                        now = add_state(now)
                    ndp[nob][now] = (ndp[nob][now] + cur * ways) % MOD

    dp = ndp

ans = 0
for ob in range(3):
    for ow in range(3):
        parity = (1 if ob == 1 else 0) ^ (1 if ow == 1 else 0)
        if parity == p:
            ans = (ans + dp[ob][ow]) % MOD

print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
