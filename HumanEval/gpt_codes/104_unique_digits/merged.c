#include <stdio.h>

void get_unique_sorted_digits(int *arr, int n, int *result, int *result_len) {
    int digits[10] = {0};
    for (int i = 0; i < n; i++) {
        int num = arr[i];
        if (num < 0) num = -num;
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 1) {
                digits[digit] = 1;
            }
            num /= 10;
        }
    }
    *result_len = 0;
    for (int i = 9; i >= 0; i--) {
        if (digits[i]) {
            result[(*result_len)++] = i;
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
