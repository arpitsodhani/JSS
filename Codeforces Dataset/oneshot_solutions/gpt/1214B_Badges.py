b = int(input())
g = int(input())
n = int(input())

lo = max(0, n - g)
hi = min(b, n)

print(max(0, hi - lo + 1))
