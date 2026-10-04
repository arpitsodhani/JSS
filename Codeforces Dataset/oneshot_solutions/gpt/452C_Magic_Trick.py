n, m = map(int, input().split())

if n == 1:
    ans = 1.0
else:
    ans = (2 * n * m - n - m) / (n * (n * m - 1))

print(f"{ans:.16f}")
