long long compute_factorial_mod(int n, long long p) {
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result = (result * i) % p;
    }
    return result;
}

long long modular_inverse_fermat(long long a, long long p) {
    long long result = 1, base = a % p, exp = p - 2;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % p;
        base = (base * base) % p;
        exp >>= 1;
    }
    return result;
}

long long binomial_coefficient_lucas(long long n, long long k, long long p) {
    if (k > n) return 0;
    if (k == 0 || n == k) return 1;
    
    long long result = 1;
    while (n > 0 && k > 0) {
        long long ni = n % p, ki = k % p;
        if (ki > ni) return 0;
        
        long long num = compute_factorial_mod(ni, p);
        long long den = (compute_factorial_mod(ki, p) * compute_factorial_mod(ni - ki, p)) % p;
        result = (result * num % p * modular_inverse_fermat(den, p)) % p;
        
        n /= p;
        k /= p;
    }
    return result;
}

void precompute_small_factorials(long long *fact, int limit, long long p) {
    fact[0] = 1;
    for (int i = 1; i <= limit && i < p; i++) {
        fact[i] = (fact[i - 1] * i) % p;
    }
}

int main() {
    long long n, k, p;
    scanf("%lld %lld %lld", &n, &k, &p);
    printf("%lld\n", binomial_coefficient_lucas(n, k, p));
    return 0;
}

