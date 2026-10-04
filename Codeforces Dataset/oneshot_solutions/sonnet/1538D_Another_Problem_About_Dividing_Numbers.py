import sys

def count_prime_factors(n):
    """Count the number of prime factors of n with multiplicity."""
    if n == 1:
        return 0
    count = 0
    # Check for factor 2
    while n % 2 == 0:
        count += 1
        n //= 2
    # Check for odd factors from 3 onwards
    d = 3
    while d * d <= n:
        while n % d == 0:
            count += 1
            n //= d
        d += 2
    # If n > 1, then it's a prime factor
    if n > 1:
        count += 1
    return count

def solve(a, b, k):
    omega_a = count_prime_factors(a)
    omega_b = count_prime_factors(b)
    
    if a == b:
        min_steps = 0
    elif a % b == 0 or b % a == 0:
        min_steps = 1
    else:
        min_steps = 2
    
    max_steps = omega_a + omega_b
    
    # Check if k is in the valid range
    if min_steps <= k <= max_steps:
        # Special case: if a == b and k == 1, it's impossible
        if a == b and k == 1:
            return "NO"
        else:
            return "YES"
    else:
        return "NO"

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3
        print(solve(a, b, k))

if __name__ == "__main__":
    main()
