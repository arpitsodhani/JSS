#include <stdio.h>
#include <stdlib.h>

int count_positive_digit_sums(int *arr, int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        int num = arr[i];
        int sum = 0;
        int is_negative = 0, leading = 0;
        if (num < 0) {
            is_negative = 1;
            num = -num;
        }
        int divisor = 1;
        while (num / divisor >= 10) divisor *= 10;
        leading = num / divisor;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        if (is_negative) sum -= 2 * leading;
        if (sum > 0) count++;
    }
    return count;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result = count_positive_digit_sums(arr, n);
    printf("%d\n", result);
    return 0;
}
