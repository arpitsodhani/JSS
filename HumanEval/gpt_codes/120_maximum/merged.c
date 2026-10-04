#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int compare_int(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

void maximum(int n, int k, int arr[], int *result) {
    qsort(arr, n, sizeof(int), compare_int);
    for (int i = 0; i < k; i++) {
        result[i] = arr[n - k + i];
    }
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    int result[k];
    maximum(n, k, arr, result);
    for (int i = 0; i < k; i++) {
        printf("%d", result[i]);
        if (i < k - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
