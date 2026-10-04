import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = sorted(data[1:])

ans = 0
for i in range(n // 2):
    s = a[i] + a[n - 1 - i]
    ans += s * s

print(ans)
