#include <stdio.h>

void filter_positive(int *arr, int n, int *result, int *result_len) {
    *result_len = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > 0) {
            result[(*result_len)++] = arr[i];
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result[n];
    int result_len;
    filter_positive(arr, n, result, &result_len);
    for (int i = 0; i < result_len; i++) {
        printf("%d", result[i]);
        if (i < result_len - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
