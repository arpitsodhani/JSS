#include <stdio.h>

int can_sort_by_rotation(int *arr, int n) {
    if (n <= 1) return 1;
    int sorted = 1;
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i-1]) {
            sorted = 0;
            break;
        }
    }
    if (sorted) return 1;
    for (int rotate = 1; rotate < n; rotate++) {
        int valid = 1;
        for (int i = 0; i < n - 1; i++) {
            int curr = (i + rotate) % n;
            int next = (i + rotate + 1) % n;
            if (arr[curr] > arr[next]) {
                valid = 0;
                break;
            }
        }
        if (valid) return 1;
    }
    return 0;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    if (can_sort_by_rotation(arr, n)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    return 0;
}
