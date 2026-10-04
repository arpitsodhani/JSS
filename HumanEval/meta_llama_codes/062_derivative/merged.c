#include <stdio.h>

void compute_derivative(int *coeffs, int n, int *result, int *result_len) {
    *result_len = 0;
    for (int i = 1; i < n; i++) {
        result[(*result_len)++] = coeffs[i] * i;
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int coeffs[n];
    for (int i = 0; i < n; i++) scanf("%d", &coeffs[i]);
    int result[n];
    int result_len;
    compute_derivative(coeffs, n, result, &result_len);
    for (int i = 0; i < result_len; i++) {
        printf("%d", result[i]);
        if (i < result_len - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
