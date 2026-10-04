import sys
import math

x = int(sys.stdin.readline())

for k in range(1, 1000000):
    n2 = x + k * k
    n = math.isqrt(n2)
    if n * n == n2 and n // k >= 2:
        print(n, n // k)
        break
else:
    print(-1)
