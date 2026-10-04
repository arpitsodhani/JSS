import sys
import math

def is_square(v):
    r = math.isqrt(v)
    return r * r == v

def solve_case(a):
    n = len(a)
    ans = 1
    candidates = set()

    for i in range(n):
        for j in range(i + 1, n):
            d = abs(a[j] - a[i])
            lo = min(a[i], a[j])
            r = 1
            while r * r <= d:
                if d % r == 0:
                    s = d // r
                    if (r + s) % 2 == 0:
                        p = (s - r) // 2
                        x = p * p - lo
                        if 0 <= x <= 10**18:
                            candidates.add(x)
                r += 1

    for x in candidates:
        cnt = 0
        for v in a:
            if is_square(v + x):
                cnt += 1
        if cnt > ans:
            ans = cnt

    return ans

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
out = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n
    out.append(str(solve_case(a)))

print("\n".join(out))
