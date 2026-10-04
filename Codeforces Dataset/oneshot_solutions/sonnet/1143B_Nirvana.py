def product_of_digits(n):
    prod = 1
    while n > 0:
        prod *= n % 10
        n //= 10
    return prod

def solve(n):
    s = str(n)
    max_prod = product_of_digits(n)
    
    for i in range(len(s)):
        if int(s[i]) > 0:
            # Try reducing digit at position i and making all subsequent digits 9
            new_s = s[:i] + str(int(s[i]) - 1) + '9' * (len(s) - i - 1)
            new_n = int(new_s)
            max_prod = max(max_prod, product_of_digits(new_n))
    
    return max_prod

n = int(input())
print(solve(n))
