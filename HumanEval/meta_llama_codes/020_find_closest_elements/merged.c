#include <stdio.h>

double abs_double(double value) {
    return value < 0 ? -value : value;
}

void print_number(double value) {
    long long integral = (long long)value;
    if (abs_double(value - (double)integral) < 1e-9) printf("%.1f", value);
    else printf("%g", value);
}

void find_closest(double *arr, int n, double *min_val, double *max_val) {
    double min_diff = abs_double(arr[1] - arr[0]);
    *min_val = arr[0] < arr[1] ? arr[0] : arr[1];
    *max_val = arr[0] > arr[1] ? arr[0] : arr[1];
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            double diff = abs_double(arr[i] - arr[j]);
            if (diff < min_diff) {
                min_diff = diff;
                *min_val = arr[i] < arr[j] ? arr[i] : arr[j];
                *max_val = arr[i] > arr[j] ? arr[i] : arr[j];
            }
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    double arr[n];
    for (int i = 0; i < n; i++) scanf("%lf", &arr[i]);
    double min_val, max_val;
    find_closest(arr, n, &min_val, &max_val);
    print_number(min_val);
    printf(" ");
    print_number(max_val);
    printf("\n");
    return 0;
}
