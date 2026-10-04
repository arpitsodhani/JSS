#include <stdio.h>

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n", gcd(a, b));
    return 0;
}

int compute_gcd(int x, int y) {
    while (y) {
        int r = x % y;
        x = y;
        y = r;
    }
    return x;
}

int euclid_gcd(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

int find_gcd(int x, int y) {
    int r;
    while (y != 0) { r = x % y; x = y; y = r; }
    return x;
}

int greatest_divisor(int m, int n) {
    while (n > 0) {
        int rem = m % n;
        m = n;
        n = rem;
    }
    return m;
}
