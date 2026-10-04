#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void add_polynomial_mod(long long *a, long long *b, int len, long long mod, long long *result) {
    for (int i = 0; i < len; i++) {
        result[i] = (a[i] + b[i]) % mod;
    }
}

void multiply_polynomial_mod(long long *a, int len_a, long long *b, int len_b, long long mod, long long *result) {
    for (int i = 0; i < len_a + len_b - 1; i++) result[i] = 0;
    for (int i = 0; i < len_a; i++) {
        for (int j = 0; j < len_b; j++) {
            result[i + j] = (result[i + j] + a[i] * b[j]) % mod;
        }
    }
}

int berlekamp_massey_recurrence(long long *sequence, int n, long long mod, long long *coeffs) {
    long long cur[1005] = {0}, ls[1005] = {0};
    int lf = 0, ld = 0;
    cur[0] = ls[0] = 1;
    
    for (int i = 0; i < n; i++) {
        long long delta = sequence[i];
        for (int j = 1; j <= lf; j++) {
            delta = (delta + cur[j] * sequence[i - j]) % mod;
        }
        
        if (delta == 0) continue;
        
        if (lf == 0) {
            lf = i + 1;
            ld = delta;
            continue;
        }
        
        long long temp[1005];
        for (int j = 0; j <= lf; j++) temp[j] = cur[j];
        
        long long c = delta * (ld % mod == 0 ? 1 : mod / ld) % mod;
        for (int j = 0; j <= i - lf; j++) {
            cur[j + i - lf + 1] = (cur[j + i - lf + 1] - c * ls[j] % mod + mod) % mod;
        }
        
        if (i + 1 - lf > lf) {
            lf = i + 1 - lf;
            ld = delta;
            for (int j = 0; j <= lf; j++) ls[j] = temp[j];
        }
    }
    
    for (int i = 0; i <= lf; i++) coeffs[i] = cur[i];
    return lf;
}

int main() {
    int n;
    long long sequence[1005], coeffs[1005], mod = 1000000007;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &sequence[i]);
    }
    
    int len = berlekamp_massey_recurrence(sequence, n, mod, coeffs);
    printf("%d\n", len);
    for (int i = 0; i <= len; i++) {
        printf("%lld ", coeffs[i]);
    }
    return 0;
}