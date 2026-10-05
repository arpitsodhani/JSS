#include <math.h>
#include <stdio.h>

double compute_mad(double *arr, int n) {
    double sum = 0.0;
    for (int i = 0; i < n; i++) sum += arr[i];
    double mean = sum / n;
    double mad_sum = 0.0;
    for (int i = 0; i < n; i++) {
        mad_sum += fabs(arr[i] - mean);
    }
    return mad_sum / n;
}

int main(void) {
    int n;
    scanf("%d", &n);
    double arr[n];
    for (int i = 0; i < n; i++) scanf("%lf", &arr[i]);
    double result = compute_mad(arr, n);
    printf("%g\n", result);
    return 0;
}
