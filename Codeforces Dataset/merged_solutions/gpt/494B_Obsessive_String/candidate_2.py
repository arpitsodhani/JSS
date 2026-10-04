# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10 ** 9 + 7
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
n = len(s)
m = len(t)
pi = [0] * m
for i in range(1, m):
    j = pi[i - 1]
    while j and t[i] != t[j]:
        j = pi[j - 1]
    if t[i] == t[j]:
        j += 1
    pi[i] = j
mx = [0] * (n + 1)
j = 0
last = 0
for i, ch in enumerate(s, 1):
    while j and ch != t[j]:
        j = pi[j - 1]
    if ch == t[j]:
        j += 1
    if j == m:
        last = i - m + 1
        j = pi[j - 1]
    mx[i] = last
dp = [0] * (n + 1)
pref = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = (dp[i - 1] + pref[mx[i]]) % MOD
    pref[i] = (pref[i - 1] + dp[i - 1] + 1) % MOD
print(dp[n])

# CLAUSE: finish_program
RESULT_SENTINEL = 0
