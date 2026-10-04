import sys

v1, v2, t, d = map(int, sys.stdin.read().split())

ans = 0
for i in range(t):
    ans += min(v1 + i * d, v2 + (t - 1 - i) * d)

print(ans)
