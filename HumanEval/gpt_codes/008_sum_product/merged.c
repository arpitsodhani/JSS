#include <stdio.h>

void compute_sum_product(int *arr, int n, int *sum, int *product) {
    *sum = 0;
    *product = 1;
    for (int i = 0; i < n; i++) {
        *sum += arr[i];
        *product *= arr[i];
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int sum, product;
    compute_sum_product(arr, n, &sum, &product);
    printf("%d %d\n", sum, product);
    return 0;
}
