n, p = map(int, input().split())

if n <= 2:
    print(1)
else:
    ans = (n * pow(2, n - 2, p)) % p
    print(ans)
