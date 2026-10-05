#include <stdio.h>

void strange_sort(int *arr, int n, int *result) {
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
    int left = 0, right = n - 1;
    int idx = 0;
    while (left <= right) {
        if (idx % 2 == 0) {
            result[idx++] = sorted[left++];
        } else {
            result[idx++] = sorted[right--];
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result[n];
    strange_sort(arr, n, result);
    for (int i = 0; i < n; i++) {
        printf("%d", result[i]);
        if (i < n - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
