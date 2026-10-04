int compute_legendre_symbol(long long a, long long p) {
    long long result = 1, base = a % p, exp = (p - 1) / 2;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % p;
        base = (base * base) % p;
        exp >>= 1;
    }
    return result == 1 ? 1 : -1;
}

long long find_quadratic_nonresidue(long long p) {
    for (long long n = 2; n < p; n++) {
        if (compute_legendre_symbol(n, p) == -1) {
            return n;
        }
    }
    return -1;
}

long long tonelli_shanks_sqrt(long long n, long long p) {
    if (compute_legendre_symbol(n, p) != 1) return -1;
    
    long long q = p - 1, s = 0;
    while (q % 2 == 0) {
        q /= 2;
        s++;
    }
    
    if (s == 1) {
        long long result = 1, base = n, exp = (p + 1) / 4;
        while (exp > 0) {
            if (exp & 1) result = (result * base) % p;
            base = (base * base) % p;
            exp >>= 1;
        }
        return result;
    }
    
    long long z = find_quadratic_nonresidue(p);
    long long c = 1, base = z, exp = q;
    while (exp > 0) {
        if (exp & 1) c = (c * base) % p;
        base = (base * base) % p;
        exp >>= 1;
    }
    
    long long r = 1;
    base = n;
    exp = (q + 1) / 2;
    while (exp > 0) {
        if (exp & 1) r = (r * base) % p;
        base = (base * base) % p;
        exp >>= 1;
    }
    
    long long t = 1;
    base = n;
    exp = q;
    while (exp > 0) {
        if (exp & 1) t = (t * base) % p;
        base = (base * base) % p;
        exp >>= 1;
    }
    
    long long m = s;
    while (t != 1) {
        long long temp = t;
        int i;
        for (i = 1; i < m; i++) {
            temp = (temp * temp) % p;
            if (temp == 1) break;
        }
        
        long long b = c;
        for (int j = 0; j < m - i - 1; j++) {
            b = (b * b) % p;
        }
        
        r = (r * b) % p;
        c = (b * b) % p;
        t = (t * c) % p;
        m = i;
    }
    
    return r;
}

long long modular_power_fast(long long base, long long exp, long long p) {
    long long result = 1;
    base %= p;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % p;
        base = (base * base) % p;
        exp >>= 1;
    }
    return result;
}

int main() {
    long long n, p;
    scanf("%lld %lld", &n, &p);
    long long result = tonelli_shanks_sqrt(n, p);
    if (result == -1) {
        printf("No solution\n");
    } else {
        printf("%lld\n", result);
    }
    return 0;
}

