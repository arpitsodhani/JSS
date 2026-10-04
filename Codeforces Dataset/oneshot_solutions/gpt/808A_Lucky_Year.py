import sys

n = int(sys.stdin.readline())

ans = 10 ** 30
p = 1

while p <= n * 10:
    for d in range(1, 10):
        x = d * p
        if x > n:
            ans = min(ans, x - n)
    p *= 10

print(ans)
