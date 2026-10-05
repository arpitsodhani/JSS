#include <math.h>
#include <stdio.h>

int has_close_elements(double *arr, int n, double threshold) {
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (fabs(arr[i] - arr[j]) < threshold) {
                return 1;
            }
        }
    }
    return 0;
}

int main(void) {
    int n;
    double threshold;
    scanf("%d %lf", &n, &threshold);
    
    if (n < 2) {
        printf("False\n");
        return 0;
    }
    
    double arr[n];
    for (int i = 0; i < n; i++) scanf("%lf", &arr[i]);
    
    if (has_close_elements(arr, n, threshold)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    return 0;
}
