# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
p = 1
out = []
for _ in range(t):
    n = data[p]
    p += 1
    a = data[p:p + n]
    p += n
    cnt = [0] * (n + 2)
    for x in a:
        if 1 <= x <= n:
            cnt[x] += 1
    ans = ['0'] * n
    if cnt[1] > 0:
        ans[n - 1] = '1'
    if all((cnt[i] == 1 for i in range(1, n + 1))):
        ans[0] = '1'
    l, r = (0, n - 1)
    ok = True
    for x in range(1, n):
        if cnt[x] != 1:
            ok = False
        if ok:
            if a[l] == x:
                l += 1
            elif a[r] == x:
                r -= 1
            else:
                ok = False
        idx = n - x - 1
        if idx > 0 and ok and (cnt[x + 1] > 0):
            ans[idx] = '1'
    out.append(''.join(ans))
sys.stdout.write('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
