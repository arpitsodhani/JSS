#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void multiply_matrices_modulo(long long a[2][2], long long b[2][2], long long result[2][2], long long mod) {
    long long temp[2][2];
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            temp[i][j] = 0;
            for (int k = 0; k < 2; k++) {
                temp[i][j] = (temp[i][j] + a[i][k] * b[k][j]) % mod;
            }
        }
    }
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            result[i][j] = temp[i][j];
        }
    }
}

void compute_matrix_power_modulo(long long base[2][2], long long n, long long result[2][2], long long mod) {
    result[0][0] = result[1][1] = 1;
    result[0][1] = result[1][0] = 0;
    
    while (n > 0) {
        if (n % 2 == 1) {
            multiply_matrices_modulo(result, base, result, mod);
        }
        multiply_matrices_modulo(base, base, base, mod);
        n /= 2;
    }
}

long long compute_fibonacci_modulo(long long n, long long mod) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    long long base[2][2] = {{1, 1}, {1, 0}};
    long long result[2][2];
    compute_matrix_power_modulo(base, n - 1, result, mod);
    return result[0][0];
}

int main() {
    long long n, mod;
    scanf("%lld %lld", &n, &mod);
    printf("%lld\n", compute_fibonacci_modulo(n, mod));
    return 0;
}