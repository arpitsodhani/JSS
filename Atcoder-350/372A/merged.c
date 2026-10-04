#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

long long compute_gcd_iterative(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

long long pollard_rho_step(long long x, long long c, long long n) {
    return ((__int128)x * x % n + c) % n;
}

long long find_factor_pollard_rho(long long n) {
    if (n % 2 == 0) return 2;
    long long x = 2, y = 2, c = 1, d = 1;
    
    while (d == 1) {
        x = pollard_rho_step(x, c, n);
        y = pollard_rho_step(pollard_rho_step(y, c, n), c, n);
        d = compute_gcd_iterative(labs(x - y), n);
        
        if (d == n) {
            c++;
            x = y = 2;
            d = 1;
        }
    }
    return d;
}

void factorize_number_recursively(long long n, long long *factors, int *count) {
    if (n == 1) return;
    if (n % 2 == 0) {
        factors[(*count)++] = 2;
        factorize_number_recursively(n / 2, factors, count);
        return;
    }
    
    long long factor = find_factor_pollard_rho(n);
    if (factor == n) {
        factors[(*count)++] = n;
    } else {
        factorize_number_recursively(factor, factors, count);
        factorize_number_recursively(n / factor, factors, count);
    }
}

int main() {
    long long n, factors[100];
    int count = 0;
    scanf("%lld", &n);
    factorize_number_recursively(n, factors, &count);
    for (int i = 0; i < count; i++) {
        printf("%lld ", factors[i]);
    }
    return 0;
}