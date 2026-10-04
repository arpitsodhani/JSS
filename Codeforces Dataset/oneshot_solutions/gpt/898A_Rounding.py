n = int(input().strip())
r = n % 10

if r <= 5:
    print(n - r)
else:
    print(n + (10 - r))
