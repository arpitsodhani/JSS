#include <stdio.h>

int below_threshold(const int *arr, int n, int threshold) {
    for (int i = 0; i < n; i++) {
        if (arr[i] >= threshold) return 0;
    }
    return 1;
}

int main(void) {
    int n, threshold;
    scanf("%d %d", &n, &threshold);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    printf("%s\n", below_threshold(arr, n, threshold) ? "True" : "False");
    return 0;
}
