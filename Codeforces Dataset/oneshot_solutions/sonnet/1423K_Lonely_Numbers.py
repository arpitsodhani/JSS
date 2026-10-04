import sys

def sieve_of_eratosthenes(limit):
    if limit < 2:
        return [False, False]
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def count_lonely(n, is_prime):
    if n == 1:
        return 1
    
    sqrt_n = int(n**0.5)
    
    # Count primes > sqrt_n and <= n
    lonely_primes = sum(is_prime[sqrt_n + 1:n + 1])
    
    return 1 + lonely_primes

def main():
    input_data = sys.stdin.buffer.read().decode('utf-8').strip()
    tokens = input_data.split()
    t = int(tokens[0])
    ns = [int(tokens[i]) for i in range(1, t + 1)]
    
    max_n = max(ns)
    is_prime = sieve_of_eratosthenes(max_n)
    
    for n in ns:
        print(count_lonely(n, is_prime))

if __name__ == "__main__":
    main()
