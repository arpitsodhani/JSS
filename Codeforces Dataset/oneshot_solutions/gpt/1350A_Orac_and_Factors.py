import sys
import math

def smallest_divisor(n):
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n

data = sys.stdin.read().strip().split()
t = int(data[0])
out = []
idx = 1

for _ in range(t):
    n = int(data[idx])
    k = int(data[idx + 1])
    idx += 2

    if n % 2 == 0:
        out.append(str(n + 2 * k))
    else:
        n += smallest_divisor(n)
        out.append(str(n + 2 * (k - 1)))

print("\n".join(out))
