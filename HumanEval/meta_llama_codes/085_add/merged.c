#include <stdio.h>

void add_arrays(int *arr1, int n1, int *arr2, int n2, int *result, int *result_len) {
    *result_len = 0;
    for (int i = 0; i < n1; i++) {
        result[(*result_len)++] = arr1[i];
    }
    for (int i = 0; i < n2; i++) {
        result[(*result_len)++] = arr2[i];
    }
}

int main(void) {
    int n1, n2;
    scanf("%d", &n1);
    int arr1[n1];
    for (int i = 0; i < n1; i++) scanf("%d", &arr1[i]);
    scanf("%d", &n2);
    int arr2[n2];
    for (int i = 0; i < n2; i++) scanf("%d", &arr2[i]);
    int result[n1 + n2];
    int result_len;
    add_arrays(arr1, n1, arr2, n2, result, &result_len);
    for (int i = 0; i < result_len; i++) {
        printf("%d", result[i]);
        if (i < result_len - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
