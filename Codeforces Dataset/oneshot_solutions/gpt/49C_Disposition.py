import sys

n = int(sys.stdin.readline())
ans = list(range(2, n + 1)) + [1]
print(*ans)
