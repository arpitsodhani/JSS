#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int count_ones(int n) {
    int count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
    return count;
}

int compare(const void *a, const void *b) {
    int x = *(int*)a, y = *(int*)b;
    int ones_x = count_ones(x), ones_y = count_ones(y);
    if (ones_x != ones_y) return ones_x - ones_y;
    return x - y;
}

void sort_array(int n, int arr[]) {
    if (n == 0) return;
    qsort(arr, n, sizeof(int), compare);
}

int main() {
    int n;
    scanf("%d", &n);
    if (n == 0) {
        printf("\n");
        return 0;
    }
    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    sort_array(n, arr);
    for (int i = 0; i < n; i++) {
        printf("%d", arr[i]);
        if (i < n - 1) printf(" ");
    }
    printf("\n");
    return 0;
}

