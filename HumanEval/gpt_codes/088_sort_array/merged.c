#include <stdio.h>

void sort_by_binary_ones(int *arr, int n, int *result) {
    int count_ones(int x) {
        int count = 0;
        while (x > 0) {
            count += x & 1;
            x >>= 1;
        }
        return count;
    }
    for (int i = 0; i < n; i++) result[i] = arr[i];
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            int ones1 = count_ones(result[j]);
            int ones2 = count_ones(result[j + 1]);
            if (ones1 > ones2 || (ones1 == ones2 && result[j] > result[j + 1])) {
                int temp = result[j];
                result[j] = result[j + 1];
                result[j + 1] = temp;
            }
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result[n];
    sort_by_binary_ones(arr, n, result);
    for (int i = 0; i < n; i++) {
        printf("%d", result[i]);
        if (i < n - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
