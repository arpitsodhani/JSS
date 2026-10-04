n, k = map(int, input().split())

min_x = float('inf')

# Find all divisors of n
i = 1
while i * i <= n:
    if n % i == 0:
        # i is a divisor
        q = i
        r = n // i
        if r < k:
            x = q * k + r
            min_x = min(min_x, x)
        
        # n // i is also a divisor
        if i != n // i:
            q = n // i
            r = i
            if r < k:
                x = q * k + r
                min_x = min(min_x, x)
    i += 1

print(min_x)
