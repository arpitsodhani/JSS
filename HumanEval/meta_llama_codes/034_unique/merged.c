#include <stdio.h>

void get_unique_sorted(int *arr, int n, int *result, int *result_len) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    *result_len = 0;
    for (int i = 0; i < n; i++) {
        if (i == 0 || arr[i] != arr[i - 1]) {
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
    get_unique_sorted(arr, n, result, &result_len);
    for (int i = 0; i < result_len; i++) {
        printf("%d", result[i]);
        if (i < result_len - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
