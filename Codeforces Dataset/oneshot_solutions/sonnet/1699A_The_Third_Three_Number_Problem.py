t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 1:
        print(-1)
    else:
        print(0, n // 2, 0)
