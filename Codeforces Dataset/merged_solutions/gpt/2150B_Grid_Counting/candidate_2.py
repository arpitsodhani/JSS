# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 998244353
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()
t = data[0]
idx = 1
tests = []
max_n = 0
for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n
    tests.append((n, a))
    if n > max_n:
        max_n = n
fact = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    fact[i] = fact[i - 1] * i % MOD
invfact = [1] * (max_n + 1)
invfact[max_n] = pow(fact[max_n], MOD - 2, MOD)
for i in range(max_n, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD
ans = []
for n, a in tests:
    if sum(a) != n:
        ans.append('0')
        continue
    max_h = (n + 1) // 2
    used_higher = 0
    cur = 1
    ok = True
    for r in range(n, max_h, -1):
        if a[r - 1] != 0:
            ok = False
            break
    if not ok:
        ans.append('0')
        continue
    for r in range(max_h, 0, -1):
        available = n - 2 * r + 2 - used_higher
        ways = comb(available, a[r - 1])
        cur = cur * ways % MOD
        used_higher += a[r - 1]
    ans.append(str(cur))
sys.stdout.write('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
