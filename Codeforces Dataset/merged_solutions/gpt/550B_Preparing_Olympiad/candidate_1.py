# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n, l, r, x = data[:4]
c = data[4:4 + n]

ans = 0

for mask in range(1 << n):
    total = 0
    cnt = 0
    mn = 10**18
    mx = -1

    for i in range(n):
        if mask & (1 << i):
            v = c[i]
            total += v
            cnt += 1
            if v < mn:
                mn = v
            if v > mx:
                mx = v

    if cnt >= 2 and l <= total <= r and mx - mn >= x:
        ans += 1

print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
