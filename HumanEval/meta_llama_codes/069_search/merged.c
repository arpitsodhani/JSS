#include <stdio.h>

int search_value(int *arr, int n) {
    int freq[101] = {0};
    for (int i = 0; i < n; i++) {
        if (arr[i] >= 0 && arr[i] <= 100) {
            freq[arr[i]]++;
        }
    }
    int result = -1;
    for (int i = 1; i <= 100; i++) {
        if (freq[i] >= i && i > result) {
            result = i;
        }
    }
    return result;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result = search_value(arr, n);
    printf("%d\n", result);
    return 0;
}
