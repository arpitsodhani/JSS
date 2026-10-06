#include <stdio.h>

void get_unique_sorted_digits(int *arr, int n, int *result, int *result_len) {
    *result_len = 0;
    for (int i = 0; i < n; i++) {
        int num = arr[i];
        if (num < 0) num = -num;
        int all_odd = 1;
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) all_odd = 0;
            num /= 10;
        }
        if (all_odd) result[(*result_len)++] = arr[i];
    }
    for (int i = 0; i < *result_len; ++i) {
        for (int j = i + 1; j < *result_len; ++j) {
            if (result[j] < result[i]) { int t = result[i]; result[i] = result[j]; result[j] = t; }
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result[10];
    int result_len;
    get_unique_sorted_digits(arr, n, result, &result_len);
    for (int i = 0; i < result_len; i++) {
        printf("%d", result[i]);
        if (i < result_len - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
