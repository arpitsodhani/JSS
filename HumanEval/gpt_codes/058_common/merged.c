#include <stdio.h>
#include <string.h>

void find_common_elements(int *arr1, int n1, int *arr2, int n2, int *result, int *result_len) {
    *result_len = 0;
    for (int i = 0; i < n1; i++) {
        for (int j = 0; j < n2; j++) {
            if (arr1[i] == arr2[j]) {
                int found = 0;
                for (int k = 0; k < *result_len; k++) {
                    if (result[k] == arr1[i]) {
                        found = 1;
                        break;
                    }
                }
                if (!found) {
                    result[(*result_len)++] = arr1[i];
                }
                break;
            }
        }
    }
    for (int i = 0; i < *result_len - 1; i++) {
        for (int j = 0; j < *result_len - i - 1; j++) {
            if (result[j] > result[j + 1]) {
                int temp = result[j];
                result[j] = result[j + 1];
                result[j + 1] = temp;
            }
        }
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
    int result[n1 > n2 ? n1 : n2];
    int result_len;
    find_common_elements(arr1, n1, arr2, n2, result, &result_len);
    for (int i = 0; i < result_len; i++) {
        printf("%d", result[i]);
        if (i < result_len - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
