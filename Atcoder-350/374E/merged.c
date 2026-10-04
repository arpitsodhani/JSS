int generate_primes_up_to(int n, int *primes) {
    int is_prime[100005];
    for (int i = 0; i <= n; i++) is_prime[i] = 1;
    is_prime[0] = is_prime[1] = 0;
    
    for (int i = 2; i * i <= n; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = 0;
            }
        }
    }
    
    int count = 0;
    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) primes[count++] = i;
    }
    return count;
}

long long compute_prime_exponent_factorial(long long n, long long p) {
    long long exponent = 0;
    long long power = p;
    while (power <= n) {
        exponent += n / power;
        power *= p;
    }
    return exponent;
}

void factorize_factorial(long long n, int *primes, int prime_count, long long *exponents) {
    for (int i = 0; i < prime_count && primes[i] <= n; i++) {
        exponents[i] = compute_prime_exponent_factorial(n, primes[i]);
    }
}

int sieve_primes_optimized(int limit, int *primes) {
    int is_prime[100005];
    for (int i = 0; i <= limit; i++) is_prime[i] = 1;
    is_prime[0] = is_prime[1] = 0;
    
    int count = 0;
    for (int i = 2; i <= limit; i++) {
        if (is_prime[i]) {
            primes[count++] = i;
            for (int j = i * 2; j <= limit; j += i) {
                is_prime[j] = 0;
            }
        }
    }
    return count;
}

int main() {
    long long n;
    int primes[100005];
    long long exponents[100005] = {0};
    scanf("%lld", &n);
    
    int prime_count = generate_primes_up_to(n, primes);
    factorize_factorial(n, primes, prime_count, exponents);
    
    for (int i = 0; i < prime_count && primes[i] <= n; i++) {
        if (exponents[i] > 0) {
            printf("%d^%lld ", primes[i], exponents[i]);
        }
    }
    return 0;
}

