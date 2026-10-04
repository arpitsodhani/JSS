#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int is_prime_check(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int is_multiply_prime(int a) {
    for (int i = 2; i * i * i <= a; i++) {
        if (is_prime_check(i) && a % i == 0) {
            int b = a / i;
            for (int j = i; j * j <= b; j++) {
                if (is_prime_check(j) && b % j == 0) {
                    int c = b / j;
                    if (is_prime_check(c)) return 1;
                }
            }
        }
    }
    return 0;
}

int main() {
    int a;
    scanf("%d", &a);
    printf("%s\n", is_multiply_prime(a) ? "True" : "False");
    return 0;
}

