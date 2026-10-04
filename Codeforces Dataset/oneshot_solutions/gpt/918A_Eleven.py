n = int(input())
fib = {1}
a, b = 1, 1
while b <= n:
    fib.add(b)
    a, b = b, a + b

print(''.join('O' if i in fib else 'o' for i in range(1, n + 1)))
