def smallest_divisor(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    return n

n = int(input())
total = 0
c = n

while c > 1:
    total += c
    d = smallest_divisor(c)
    c = c // d

total += 1
print(total)
