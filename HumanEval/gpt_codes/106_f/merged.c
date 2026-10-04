#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int factorial(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

int sum_to_n(int n) {
    return n * (n + 1) / 2;
}

void f(int n, int *result) {
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            result[i-1] = factorial(i);
        } else {
            result[i-1] = sum_to_n(i);
        }
    }
}

void run(void) {

    int n;
    scanf("%d", &n);
    int result[n];
    f(n, result);
    for (int i = 0; i < n; i++) {
        printf("%d", result[i]);
        if (i < n - 1) printf(" ");
    }
    printf("\n");
}

int main() {
    run();
    return 0;
}
