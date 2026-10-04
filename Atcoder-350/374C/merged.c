long long find_primitive_root(long long p) {
    long long phi = p - 1;
    long long factors[100], factor_count = 0;
    long long n = phi;
    
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            factors[factor_count++] = i;
            while (n % i == 0) n /= i;
        }
    }
    if (n > 1) factors[factor_count++] = n;
    
    for (long long g = 2; g < p; g++) {
        int is_root = 1;
        for (int i = 0; i < factor_count; i++) {
            long long exp = phi / factors[i];
            long long result = 1, base = g;
            while (exp > 0) {
                if (exp & 1) result = (result * base) % p;
                base = (base * base) % p;
                exp >>= 1;
            }
            if (result == 1) {
                is_root = 0;
                break;
            }
        }
        if (is_root) return g;
    }
    return -1;
}

void bit_reverse_copy(long long *a, long long *rev, int n) {
    for (int i = 0; i < n; i++) {
        int r = 0, k = i, logn = 0;
        int temp = n;
        while (temp > 1) {
            logn++;
            temp >>= 1;
        }
        for (int j = 0; j < logn; j++) {
            r = (r << 1) | (k & 1);
            k >>= 1;
        }
        rev[r] = a[i];
    }
}

void ntt_transform(long long *a, int n, long long root, long long mod, int inverse) {
    long long rev[100005];
    bit_reverse_copy(a, rev, n);
    for (int i = 0; i < n; i++) a[i] = rev[i];
    
    for (int len = 2; len <= n; len *= 2) {
        long long w = 1, wn = root;
        long long exp = (mod - 1) / len;
        if (inverse) exp = (mod - 1) - exp;
        
        long long base = root;
        while (exp > 0) {
            if (exp & 1) wn = (wn * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        
        for (int start = 0; start < n; start += len) {
            w = 1;
            for (int j = 0; j < len / 2; j++) {
                long long u = a[start + j];
                long long v = (a[start + j + len / 2] * w) % mod;
                a[start + j] = (u + v) % mod;
                a[start + j + len / 2] = (u - v + mod) % mod;
                w = (w * wn) % mod;
            }
        }
    }
    
    if (inverse) {
        long long n_inv = 1, base = n, exp = mod - 2;
        while (exp > 0) {
            if (exp & 1) n_inv = (n_inv * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        for (int i = 0; i < n; i++) {
            a[i] = (a[i] * n_inv) % mod;
        }
    }
}

long long compute_power_mod(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return result;
}

int main() {
    int n;
    long long a[100005], mod = 998244353;
    scanf("%d", &n);
    
    int size = 1;
    while (size < n) size *= 2;
    
    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
    }
    for (int i = n; i < size; i++) {
        a[i] = 0;
    }
    
    long long root = find_primitive_root(mod);
    ntt_transform(a, size, root, mod, 0);
    
    for (int i = 0; i < size; i++) {
        printf("%lld ", a[i]);
    }
    return 0;
}

