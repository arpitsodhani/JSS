#include <stdio.h>

int find_next_smallest(int *arr, int n) {
    int sorted[n];
    for (int i = 0; i < n; i++) sorted[i] = arr[i];
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (sorted[j] > sorted[j + 1]) {
                int temp = sorted[j];
                sorted[j] = sorted[j + 1];
                sorted[j + 1] = temp;
            }
        }
    }
    for (int i = 1; i < n; i++) {
        if (sorted[i] != sorted[0]) {
            return sorted[i];
        }
    }
    return -1;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result = find_next_smallest(arr, n);
    if (result == -1) {
        printf("None\n");
    } else {
        printf("%d\n", result);
    }
    return 0;
}
