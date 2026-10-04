import sys

s = sys.stdin.read().strip()
n = int(s)

ans = 0
while n:
    if n % 8 == 1:
        ans += 1
    n //= 8

print(ans)
