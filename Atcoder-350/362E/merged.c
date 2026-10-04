#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_sequence(int *n, long long *a) {
    scanf("%d", n);
    for (int i = 0; i < *n; i++) scanf("%lld", &a[i]);
}

void compute_arithmetic_subsequences(int n, long long *a, long long *result) {
    const long long MOD = 998244353;
    result[0] = 1;
    for (int k = 1; k <= n; k++) {
        if (k == 1) { result[k] = n; continue; }
        long long dp[85][85] = {};
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long long diff = a[j] - a[i];
                if (k == 2) dp[j][0] = (dp[j][0] + 1) % MOD;
                else {
                    for (int prev = 0; prev < i; prev++) {
                        if (a[i] - a[prev] == diff) dp[j][0] = (dp[j][0] + (k == 3 ? 1 : dp[i][0])) % MOD;
                    }
                }
            }
        }
        long long sum = 0;
        for (int i = 0; i < n; i++) sum = (sum + dp[i][0]) % MOD;
        result[k] = sum;
    }
}

int main() {
    int n;
    long long a[85], result[85];
    read_sequence(&n, a);
    compute_arithmetic_subsequences(n, a, result);
    for (int i = 1; i <= n; i++) printf("%lld%c", result[i], i == n ? '\n' : ' ');
    return 0;
}
