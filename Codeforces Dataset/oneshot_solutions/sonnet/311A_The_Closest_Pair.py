n, k = map(int, input().split())

if n * (n - 1) // 2 > k:
    for i in range(n):
        print(0, i)
else:
    print("no solution")
