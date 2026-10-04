#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void read_parameters(long long *n, long long *k) {
    scanf("%lld %lld", n, k);
}

long long compute_modular_inverse(long long a, long long m) {
    long long m0 = m, x0 = 0, x1 = 1;
    while (a > 1) {
        long long q = a / m;
        long long t = m;
        m = a % m;
        a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }
    return (x1 % m0 + m0) % m0;
}

long long compute_expected_position(long long n, long long k) {
    const long long MOD = 998244353;
    long long prob_stay = (n * n - n + 2) % MOD;
    prob_stay = (prob_stay * compute_modular_inverse(n * n % MOD, MOD)) % MOD;
    long long prob_move = (n - 1) % MOD;
    prob_move = (prob_move * compute_modular_inverse(n * n % MOD, MOD)) % MOD;
    long long power = 1;
    long long base = prob_stay;
    long long exp = k;
    while (exp > 0) {
        if (exp % 2) power = (power * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    long long ans = (1 + (n - 1) % MOD * ((1 - power + MOD) % MOD) % MOD * compute_modular_inverse((1 - prob_stay + MOD) % MOD, MOD) % MOD) % MOD;
    return ans;
}

int main() {
    long long n, k;
    read_parameters(&n, &k);
    printf("%lld\n", compute_expected_position(n, k));
    return 0;
}

