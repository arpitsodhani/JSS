import sys

s = sys.stdin.read().strip()
if s:
    n = int(s)
    ans = 0
    while n:
        n //= 5
        ans += n
    print(ans)
