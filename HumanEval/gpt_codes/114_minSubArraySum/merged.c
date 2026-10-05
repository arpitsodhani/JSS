#include <stdio.h>

int find_min_subarray_sum(int *arr, int n) {
    int min_sum = arr[0];
    int current_sum = arr[0];
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
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result = find_min_subarray_sum(arr, n);
    printf("%d\n", result);
    return 0;
}
