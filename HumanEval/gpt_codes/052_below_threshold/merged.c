#include <stdio.h>

int count_below_threshold(int *arr, int n, int threshold) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] < threshold) {
            count++;
        }
    }
    return count;
}

int main(void) {
    int n, threshold;
    scanf("%d %d", &n, &threshold);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result = count_below_threshold(arr, n, threshold);
    printf("%d\n", result);
    return 0;
}
