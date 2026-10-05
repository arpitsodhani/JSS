#include <stdio.h>

void rescale_to_unit(double *arr, int n, double *result) {
    double min_val = arr[0];
    double max_val = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < min_val) min_val = arr[i];
        if (arr[i] > max_val) max_val = arr[i];
    }
    double range = max_val - min_val;
    for (int i = 0; i < n; i++) {
        result[i] = (arr[i] - min_val) / range;
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    double arr[n];
    for (int i = 0; i < n; i++) scanf("%lf", &arr[i]);
    double result[n];
    rescale_to_unit(arr, n, result);
    for (int i = 0; i < n; i++) {
        printf("%g", result[i]);
        if (i < n - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
