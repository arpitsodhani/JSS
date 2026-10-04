# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n, m = (data[0], data[1])
ans = 0
p = 2
for _ in range(n):
    t, T, x, c = (data[p], data[p + 1], data[p + 2], data[p + 3])
    p += 4
    z = T - t
    if z <= 0:
        ans += c + m * x
    elif z >= m:
        ans += c
    else:
        q = (m + z - 1) // z
        best = c + m * x
        if q > 1:
            best = min(best, (q - 1) * c + (m - (q - 2) * z) * x)
        best = min(best, q * c)
        ans += best
print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
