#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

long long extended_gcd_recursive(long long a, long long b, long long *x, long long *y) {
    if (b == 0) {
        *x = 1;
        *y = 0;
        return a;
    }
    long long x1, y1;
    long long gcd = extended_gcd_recursive(b, a % b, &x1, &y1);
    *x = y1;
    *y = x1 - (a / b) * y1;
    return gcd;
}

long long find_modular_inverse(long long a, long long m) {
    long long x, y;
    long long gcd = extended_gcd_recursive(a, m, &x, &y);
    if (gcd != 1) return -1;
    return (x % m + m) % m;
}

int solve_linear_diophantine(long long a, long long b, long long c, long long *x, long long *y) {
    long long gcd = extended_gcd_recursive(a, b, x, y);
    if (c % gcd != 0) return 0;
    *x *= c / gcd;
    *y *= c / gcd;
    return 1;
}

int main() {
    long long a, b, c, x, y;
    scanf("%lld %lld %lld", &a, &b, &c);
    
    if (solve_linear_diophantine(a, b, c, &x, &y)) {
        printf("%lld %lld\n", x, y);
    } else {
        printf("No solution\n");
    }
    return 0;
}