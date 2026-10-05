#include <stdio.h>

void remove_duplicates(int *arr, int n, int *result, int *result_len) {
    *result_len = 0;
    for (int i = 0; i < n; i++) {
        int is_dup = 0;
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            if (arr[i] == arr[j]) {
                is_dup = 1;
                break;
            }
        }
        if (!is_dup) {
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
    remove_duplicates(arr, n, result, &result_len);
    for (int i = 0; i < result_len; i++) {
        printf("%d", result[i]);
        if (i < result_len - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
