#include <stdio.h>

void compute_rolling_max(int *arr, int n, int *result) {
    if (n == 0) return;
    int max_val = arr[0];
    for (int i = 0; i < n; i++) {
        if (arr[i] > max_val) max_val = arr[i];
        result[i] = max_val;
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    if (n == 0) {
        printf("\n");
        return 0;
    }
    int result[n];
    compute_rolling_max(arr, n, result);
    for (int i = 0; i < n; i++) {
        printf("%d", result[i]);
        if (i < n - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
