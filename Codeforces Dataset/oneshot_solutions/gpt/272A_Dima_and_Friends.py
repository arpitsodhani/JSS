import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
s = sum(data[1:])

ans = 0
for x in range(1, 6):
    if (s + x - 1) % (n + 1) != 0:
        ans += 1

print(ans)
