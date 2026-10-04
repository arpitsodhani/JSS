import sys

n = int(sys.stdin.readline())

p = -1
i = 2
while i * i <= n:
    if n % i == 0:
        p = i
        break
    i += 1

if p == -1:
    print("NO")
    sys.exit()

x = 1
m = n
while m % p == 0:
    x *= p
    m //= p

y = n // x

if y == 1:
    print("NO")
    sys.exit()

if x > y:
    x, y = y, x

for c in range(1, x):
    if (c * y + 1) % x == 0:
        d = (n - 1 - c * y) // x
        print("YES")
        print(2)
        print(c, x)
        print(d, y)
        break
