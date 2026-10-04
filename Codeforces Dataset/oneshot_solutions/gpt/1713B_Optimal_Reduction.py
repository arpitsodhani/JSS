import sys

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
ans = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n

    i = 1
    while i < n and a[i] >= a[i - 1]:
        i += 1
    while i < n and a[i] <= a[i - 1]:
        i += 1

    ans.append("YES" if i == n else "NO")

print("\n".join(ans))
