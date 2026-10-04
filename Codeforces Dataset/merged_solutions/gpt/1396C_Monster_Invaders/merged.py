# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n, r1, r2, r3, d = data[:5]
a = data[5:]

full = a[0] * r1 + r3
part = min(r2, a[0] * r1 + r1)

dp0 = full
dp1 = part

for i in range(1, n):
    full = a[i] * r1 + r3
    part = min(r2, a[i] * r1 + r1)

    ndp0 = min(
        dp0 + d + full,
        dp1 + full + 3 * d + r1,
        dp1 + part + 3 * d + 2 * r1,
    )
    if i == n - 1:
        ndp0 = min(ndp0, dp1 + full + 2 * d + r1)

    ndp1 = min(
        dp0 + d + part,
        dp1 + part + 3 * d + r1,
    )

    dp0, dp1 = ndp0, ndp1

print(dp0)

# CLAUSE: finish_program
RESULT_SENTINEL = None
