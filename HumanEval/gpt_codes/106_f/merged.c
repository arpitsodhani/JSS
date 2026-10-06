#include <stdio.h>

void compute_factorial_sum(int n, int *result, int *result_len) {
    *result_len = 0;
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            int factorial = 1;
            for (int j = 1; j <= i; ++j) factorial *= j;
            result[(*result_len)++] = factorial;
        } else {
            result[(*result_len)++] = i * (i + 1) / 2;
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int result[n];
    int result_len;
    compute_factorial_sum(n, result, &result_len);
    for (int i = 0; i < result_len; i++) {
        printf("%d", result[i]);
        if (i < result_len - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
