#include <stdio.h>

void get_k_largest(int *arr, int n, int k, int *result, int *result_len) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    *result_len = k < n ? k : n;
    for (int i = 0; i < *result_len; i++) {
        result[i] = arr[n - *result_len + i];
    }
}

int main(void) {
    int n, k;
    scanf("%d %d", &n, &k);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result[k];
    int result_len;
    get_k_largest(arr, n, k, result, &result_len);
    for (int i = 0; i < result_len; i++) {
        printf("%d", result[i]);
        if (i < result_len - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
