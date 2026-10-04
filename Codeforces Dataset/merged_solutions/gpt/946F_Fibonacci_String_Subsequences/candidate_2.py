# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10 ** 9 + 7
data = sys.stdin.read().split()
n = int(data[0])
x = int(data[1])
s = data[2]
pi = [0] * n
for i in range(1, n):
    j = pi[i - 1]
    while j and s[i] != s[j]:
        j = pi[j - 1]
    if s[i] == s[j]:
        j += 1
    pi[i] = j
go = [[0, 0] for _ in range(n)]
hit = [[0, 0] for _ in range(n)]
for q in range(n):
    for b, ch in enumerate('01'):
        j = q
        while j and ch != s[j]:
            j = pi[j - 1]
        if ch == s[j]:
            j += 1
        if j == n:
            hit[q][b] = 1
            j = pi[n - 1]
        go[q][b] = j
d = n + 1

def char_matrix(ch):
    b = ord(ch) - 48
    mat = [[0] * d for _ in range(d)]
    for q in range(n):
        mat[q][q] += 1
        mat[go[q][b]][q] += 1
        if hit[q][b]:
            mat[n][q] += 1
    mat[n][n] = 2
    return mat

def mul(a, b):
    res = [[0] * d for _ in range(d)]
    for i in range(d):
        ri = res[i]
        ai = a[i]
        for k in range(d):
            aik = ai[k]
            if aik:
                bk = b[k]
                for j in range(d):
                    ri[j] += aik * bk[j]
        for j in range(d):
            ri[j] %= MOD
    return res
m0 = char_matrix('0')
m1 = char_matrix('1')
if x == 0:
    ans = m0[n][0] % MOD
elif x == 1:
    ans = m1[n][0] % MOD
else:
    a, b = (m0, m1)
    for _ in range(2, x + 1):
        c = mul(a, b)
        a, b = (b, c)
    ans = b[n][0] % MOD
print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
