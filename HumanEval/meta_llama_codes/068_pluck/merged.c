#include <stdio.h>

void find_smallest_even(int *arr, int n, int *min_val, int *min_idx) {
    *min_val = -1;
    *min_idx = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            if (*min_val == -1 || arr[i] < *min_val) {
                *min_val = arr[i];
                *min_idx = i;
            }
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int min_val, min_idx;
    find_smallest_even(arr, n, &min_val, &min_idx);
    if (min_val == -1) {
        printf("\n");
    } else {
        printf("[%d %d]\n", min_val, min_idx);
    }
    return 0;
}
