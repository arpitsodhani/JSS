#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

long long compute_modular_inverse_extended(long long a, long long m) {
    long long m0 = m, x0 = 0, x1 = 1;
    if (m == 1) return 0;
    
    while (a > 1) {
        long long q = a / m;
        long long t = m;
        m = a % m;
        a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }
    
    if (x1 < 0) x1 += m0;
    return x1;
}

long long solve_crt_pair(long long r1, long long m1, long long r2, long long m2) {
    long long x, y;
    long long g = m1, temp_m = m2;
    long long inv1 = 0, inv2 = 1;
    
    while (temp_m != 0) {
        long long q = g / temp_m;
        long long t = temp_m;
        temp_m = g % temp_m;
        g = t;
        t = inv1;
        inv1 = inv2 - q * inv1;
        inv2 = t;
    }
    
    if ((r2 - r1) % g != 0) return -1;
    
    long long lcm = m1 / g * m2;
    long long result = (r1 + m1 * (((r2 - r1) / g * inv2) % (m2 / g))) % lcm;
    if (result < 0) result += lcm;
    return result;
}

long long solve_crt_system(long long *remainders, long long *moduli, int n) {
    long long result = remainders[0];
    long long lcm = moduli[0];
    
    for (int i = 1; i < n; i++) {
        result = solve_crt_pair(result, lcm, remainders[i], moduli[i]);
        if (result == -1) return -1;
        
        long long g = lcm, temp = moduli[i];
        while (temp != 0) {
            long long t = temp;
            temp = g % temp;
            g = t;
        }
        lcm = lcm / g * moduli[i];
    }
    return result;
}

int main() {
    int n;
    long long remainders[105], moduli[105];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &remainders[i], &moduli[i]);
    }
    
    long long result = solve_crt_system(remainders, moduli, n);
    if (result == -1) {
        printf("No solution\n");
    } else {
        printf("%lld\n", result);
    }
    return 0;
}