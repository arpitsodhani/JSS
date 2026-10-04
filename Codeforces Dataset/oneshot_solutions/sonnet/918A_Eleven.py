n = int(input())

fib = set()
a, b = 1, 1
while a <= n:
    fib.add(a)
    a, b = b, a + b

result = []
for i in range(1, n + 1):
    result.append('O' if i in fib else 'o')

print(''.join(result))
