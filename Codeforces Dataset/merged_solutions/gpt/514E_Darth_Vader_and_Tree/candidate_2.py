# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10 ** 9 + 7
data = list(map(int, sys.stdin.read().split()))
n, x = (data[0], data[1])
d = data[2:2 + n]
m = max(d)
cnt = [0] * (m + 1)
for v in d:
    cnt[v] += 1
size = m + 1
mat = [[0] * size for _ in range(size)]
mat[0][0] = 1
for i in range(1, m + 1):
    mat[0][i] = cnt[i] % MOD
    mat[1][i] = cnt[i] % MOD
for i in range(2, size):
    mat[i][i - 1] = 1
vec = [1, 1] + [0] * (m - 1)

def mat_mul(a, b):
    n = len(a)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        ri = res[i]
        ai = a[i]
        for k in range(n):
            if ai[k]:
                aik = ai[k]
                bk = b[k]
                for j in range(n):
                    ri[j] = (ri[j] + aik * bk[j]) % MOD
    return res

def mat_vec_mul(a, v):
    n = len(a)
    res = [0] * n
    for i in range(n):
        s = 0
        ai = a[i]
        for j in range(n):
            s += ai[j] * v[j]
        res[i] = s % MOD
    return res
while x:
    if x & 1:
        vec = mat_vec_mul(mat, vec)
    mat = mat_mul(mat, mat)
    x >>= 1
print(vec[0] % MOD)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
