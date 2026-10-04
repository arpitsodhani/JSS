#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

long long modular_multiply_safe(long long a, long long b, long long mod) {
    return (__int128)a * b % mod;
}

long long modular_power_binary(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) result = modular_multiply_safe(result, base, mod);
        base = modular_multiply_safe(base, base, mod);
        exp >>= 1;
    }
    return result;
}

int check_composite_witness(long long n, long long a, long long d, int s) {
    long long x = modular_power_binary(a, d, n);
    if (x == 1 || x == n - 1) return 0;
    
    for (int r = 1; r < s; r++) {
        x = modular_multiply_safe(x, x, n);
        if (x == n - 1) return 0;
    }
    return 1;
}

int test_primality_miller_rabin(long long n) {
    if (n < 2) return 0;
    if (n == 2 || n == 3) return 1;
    if (n % 2 == 0) return 0;
    
    long long d = n - 1;
    int s = 0;
    while (d % 2 == 0) {
        d /= 2;
        s++;
    }
    
    long long witnesses[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (int i = 0; i < 12; i++) {
        if (witnesses[i] >= n) continue;
        if (check_composite_witness(n, witnesses[i], d, s)) return 0;
    }
    return 1;
}

int main() {
    long long n;
    scanf("%lld", &n);
    printf("%s\n", test_primality_miller_rabin(n) ? "PRIME" : "COMPOSITE");
    return 0;
}