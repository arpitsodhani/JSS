#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void pluck(int* arr, int n, int* result, int* result_n) {
    *result_n = 0;
    int min_even = -1;
    int min_idx = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            if (min_even == -1 || arr[i] < min_even) {
                min_even = arr[i];
                min_idx = i;
            }
        }
    }
    if (min_even != -1) {
        result[0] = min_even;
        result[1] = min_idx;
        *result_n = 2;
    }
}

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result[2], result_n;
    pluck(arr, n, result, &result_n);
    if (result_n == 0) {
        printf("\n");
    } else {
        for (int i = 0; i < result_n; i++) {
            if (i > 0) printf(" ");
            printf("%d", result[i]);
        }
        printf("\n");
    }
    return 0;
}

