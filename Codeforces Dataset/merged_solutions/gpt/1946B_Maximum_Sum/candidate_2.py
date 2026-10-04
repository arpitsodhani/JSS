# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10 ** 9 + 7
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
ans = []
for _ in range(t):
    n = data[idx]
    k = data[idx + 1]
    idx += 2
    a = data[idx:idx + n]
    idx += n
    total = sum(a)
    best = 0
    cur = 0
    for x in a:
        cur = max(0, cur + x)
        best = max(best, cur)
    res = (total + best * (pow(2, k, MOD) - 1)) % MOD
    ans.append(str(res))
sys.stdout.write('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
