# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10 ** 9 + 7
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
cases = []
max_n = 0
for _ in range(t):
    n = data[idx]
    k = data[idx + 1]
    idx += 2
    ones = sum(data[idx:idx + n])
    idx += n
    cases.append((n, k, ones))
    if n > max_n:
        max_n = n
fact = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    fact[i] = fact[i - 1] * i % MOD
invfact = [1] * (max_n + 1)
invfact[max_n] = pow(fact[max_n], MOD - 2, MOD)
for i in range(max_n, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD

def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD
out = []
for n, k, ones in cases:
    zeros = n - ones
    need = k // 2 + 1
    ans = 0
    for take_ones in range(need, min(k, ones) + 1):
        ans = (ans + comb(ones, take_ones) * comb(zeros, k - take_ones)) % MOD
    out.append(str(ans))
sys.stdout.write('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
