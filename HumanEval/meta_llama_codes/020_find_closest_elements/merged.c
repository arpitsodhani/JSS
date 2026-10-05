#include <math.h>
#include <stdio.h>

void print_number(double value) {
    if (fabs(value - round(value)) < 1e-9) printf("%.1f", value);
    else printf("%g", value);
}

void find_closest(double *arr, int n, double *min_val, double *max_val) {
    double min_diff = fabs(arr[1] - arr[0]);
    *min_val = arr[0] < arr[1] ? arr[0] : arr[1];
    *max_val = arr[0] > arr[1] ? arr[0] : arr[1];
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            double diff = fabs(arr[i] - arr[j]);
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
