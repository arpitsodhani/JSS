import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = data[1:]

if len(a) < n:
    sys.exit()

half = n // 2
ans = -1

for i in range(half):
    if a[i] == a[i + half]:
        ans = i + 1
        break

print(ans)
