from math import isqrt

n = int(input())
M = []
for _ in range(n):
    row = list(map(int, input().split()))
    M.append(row)

# Calculate a[0] using indices 0, 1, 2
a0_squared = M[0][1] * M[0][2] // M[1][2]
a0 = isqrt(a0_squared)

# Calculate remaining elements
a = [a0]
for i in range(1, n):
    a.append(M[0][i] // a0)

print(' '.join(map(str, a)))
