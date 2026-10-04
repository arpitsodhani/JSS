import sys

n = int(sys.stdin.readline())

ans = []
cur = 1
while n >= cur:
    ans.append(cur)
    n -= cur
    cur += 1

if n:
    ans[-1] += n

print(len(ans))
print(*ans)
