#include <stdio.h>

int is_multiply_prime(int n) {
    int factors[10];
    int count = 0;
    int temp = n;
    for (int i = 2; i * i <= temp && count < 10; i++) {
        while (temp % i == 0) {
            factors[count++] = i;
            temp /= i;
        }
    }
    if (temp > 1) {
        factors[count++] = temp;
    }
    return count == 3;
}

int main(void) {
    int n;
    scanf("%d", &n);
    if (is_multiply_prime(n)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    return 0;
}
