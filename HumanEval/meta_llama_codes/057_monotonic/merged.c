#include <stdio.h>

int is_monotonic(int *arr, int n) {
    int increasing = 1, decreasing = 1;
    for (int i = 1; i < n; i++) {
        if (arr[i] > arr[i-1]) decreasing = 0;
        if (arr[i] < arr[i-1]) increasing = 0;
    }
    return increasing || decreasing;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    if (is_monotonic(arr, n)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    return 0;
}
