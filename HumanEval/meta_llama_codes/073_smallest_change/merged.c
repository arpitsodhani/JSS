#include <stdio.h>

int count_changes_needed(int *arr, int n) {
    int changes = 0;
    for (int i = 0; i < n / 2; i++) {
        if (arr[i] != arr[n - 1 - i]) {
            changes++;
        }
    }
    return changes;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    int result = count_changes_needed(arr, n);
    printf("%d\n", result);
    return 0;
}
