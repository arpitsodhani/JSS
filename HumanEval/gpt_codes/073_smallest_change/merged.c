#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int smallest_change(int* arr, int n) {
    int changes = 0;
    for (int i = 0; i < n / 2; i++) {
        if (arr[i] != arr[n - 1 - i]) changes++;
    }
    return changes;
}

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    printf("%d\n", smallest_change(arr, n));
    return 0;
}

