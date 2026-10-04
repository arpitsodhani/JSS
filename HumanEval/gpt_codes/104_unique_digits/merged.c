#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int has_even_digit(int n) {
    while (n > 0) {
        if ((n % 10) % 2 == 0) return 1;
        n /= 10;
    }
    return 0;
}

int compare_int(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

void unique_digits(int n, int x[], int *result, int *result_size) {
    *result_size = 0;
    for (int i = 0; i < n; i++) {
        if (!has_even_digit(x[i])) {
            result[(*result_size)++] = x[i];
        }
    }
    qsort(result, *result_size, sizeof(int), compare_int);
}

void run(void) {

    int n;
    scanf("%d", &n);
    if (n == 0) {
        printf("\n");
        return 0;
    }
    int x[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &x[i]);
    }
    int result[n], result_size;
    unique_digits(n, x, result, &result_size);
    for (int i = 0; i < result_size; i++) {
        printf("%d", result[i]);
        if (i < result_size - 1) printf(" ");
    }
    printf("\n");
}

int main() {
    run();
    return 0;
}
