#include <stdio.h>

int has_triple_sum_zero(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                if (arr[i] + arr[j] + arr[k] == 0) {
                    return 1;
                }
            }
        }
    }
    return 0;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    if (has_triple_sum_zero(arr, n)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    return 0;
}
