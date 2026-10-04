import sys

n, x, y = map(int, sys.stdin.read().split())

if y < n:
    print(-1)
else:
    a = y - n + 1
    if a * a + (n - 1) >= x:
        print(a)
        for _ in range(n - 1):
            print(1)
    else:
        print(-1)
