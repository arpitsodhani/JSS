# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
p = 0
n = data[p]
p += 1
xs = [0] * n
ys = [0] * n
for i in range(n):
    xs[i] = data[p]
    ys[i] = data[p + 1]
    p += 2
t = data[p]
p += 1
total = n * (n - 1) * (n - 2) // 6
ans = []
for _ in range(t):
    qx = data[p]
    qy = data[p + 1]
    p += 2
    inside = True
    for i in range(n):
        j = i + 1
        if j == n:
            j = 0
        if (xs[j] - xs[i]) * (qy - ys[i]) - (ys[j] - ys[i]) * (qx - xs[i]) > 0:
            inside = False
            break
    if not inside:
        ans.append('0')
        continue
    vx = [xs[i] - qx for i in range(n)]
    vy = [ys[i] - qy for i in range(n)]
    vx += vx
    vy += vy
    bad = 0
    r = 1
    for l in range(n):
        if r < l + 1:
            r = l + 1
        while r < l + n and vx[l] * vy[r] - vy[l] * vx[r] < 0:
            r += 1
        cnt = r - l - 1
        bad += cnt * (cnt - 1) // 2
    ans.append(str(total - bad))
sys.stdout.write('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
