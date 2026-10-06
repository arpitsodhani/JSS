#include <stdio.h>

long long find_min_subarray_sum(long long *arr, int n) {
    long long min_sum = arr[0];
    long long current_sum = arr[0];
    for (int i = 1; i < n; i++) {
        current_sum = arr[i] < current_sum + arr[i] ? arr[i] : current_sum + arr[i];
        if (current_sum < min_sum) {
            min_sum = current_sum;
        }
    }
    return min_sum;
}

int main(void) {
    int n;
    scanf("%d", &n);
    long long arr[n];
    for (int i = 0; i < n; i++) scanf("%lld", &arr[i]);
    long long result = find_min_subarray_sum(arr, n);
    printf("%lld\n", result);
    return 0;
}
