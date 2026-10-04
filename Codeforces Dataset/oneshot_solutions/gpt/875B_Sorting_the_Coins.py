import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
p = data[1:]

used = [False] * (n + 2)
right = n
ans = [1]

for i, x in enumerate(p, 1):
    used[x] = True
    while right > 0 and used[right]:
        right -= 1
    ans.append(i - (n - right) + 1)

print(*ans)
