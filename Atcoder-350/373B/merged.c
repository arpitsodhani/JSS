#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void reduce_polynomial_by_recurrence(long long *poly, int deg, long long *rec, int k, long long mod) {
    for (int i = deg; i >= k; i--) {
        if (poly[i] == 0) continue;
        for (int j = 0; j < k; j++) {
            poly[i - k + j] = (poly[i - k + j] + poly[i] * rec[j]) % mod;
        }
        poly[i] = 0;
    }
}

void multiply_and_reduce_polynomial(long long *a, long long *b, int k, long long *rec, long long mod, long long *result) {
    long long temp[2005] = {0};
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            temp[i + j] = (temp[i + j] + a[i] * b[j]) % mod;
        }
    }
    reduce_polynomial_by_recurrence(temp, 2 * k - 2, rec, k, mod);
    for (int i = 0; i < k; i++) result[i] = temp[i];
}

long long compute_nth_term_kitamasa(long long *init, long long *rec, int k, long long n, long long mod) {
    long long result[1005] = {0}, base[1005] = {0};
    result[0] = 1;
    base[1] = 1;
    
    while (n > 0) {
        if (n & 1) {
            long long temp[1005];
            multiply_and_reduce_polynomial(result, base, k, rec, mod, temp);
            for (int i = 0; i < k; i++) result[i] = temp[i];
        }
        long long temp[1005];
        multiply_and_reduce_polynomial(base, base, k, rec, mod, temp);
        for (int i = 0; i < k; i++) base[i] = temp[i];
        n >>= 1;
    }
    
    long long answer = 0;
    for (int i = 0; i < k; i++) {
        answer = (answer + result[i] * init[i]) % mod;
    }
    return answer;
}

int main() {
    int k;
    long long n, init[1005], rec[1005], mod = 1000000007;
    scanf("%d %lld", &k, &n);
    for (int i = 0; i < k; i++) {
        scanf("%lld", &init[i]);
    }
    for (int i = 0; i < k; i++) {
        scanf("%lld", &rec[i]);
    }
    
    printf("%lld\n", compute_nth_term_kitamasa(init, rec, k, n, mod));
    return 0;
}