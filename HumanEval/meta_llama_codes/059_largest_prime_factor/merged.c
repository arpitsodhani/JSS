#include <stdio.h>

int largest_prime_factor(int n) {
    int largest = -1;
    for (int i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            largest = i;
            n /= i;
        }
    }
    if (n > 1) {
        largest = n;
    }
    return largest;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int result = largest_prime_factor(n);
    printf("%d\n", result);
    return 0;
}
