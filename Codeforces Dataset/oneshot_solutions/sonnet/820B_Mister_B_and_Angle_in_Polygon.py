n, a = map(int, input().split())

m = round(a * n / 180)
m = max(1, min(n - 2, m))

v1 = 2
v2 = 1
v3 = m + 2

print(v1, v2, v3)
