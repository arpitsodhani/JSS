# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 998244353
n, m = map(int, sys.stdin.readline().split())
is_prime = [True] * (n + 1)
if n >= 0:
    is_prime[0] = False
if n >= 1:
    is_prime[1] = False
for i in range(2, n + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
need = 1
unique = 1
total = 0
bad = 0
power = 1
for length in range(1, n + 1):
    power = power * m % MOD
    total = (total + power) % MOD
    if is_prime[length]:
        need *= length
    unique = unique * (m // need) % MOD
    bad = (bad + unique) % MOD
print((total - bad) % MOD)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
