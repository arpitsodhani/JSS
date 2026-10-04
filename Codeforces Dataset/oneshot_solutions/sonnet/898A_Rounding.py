n = int(input())

last = n % 10
if last <= 5:
    print(n - last)
else:
    print(n + (10 - last))
