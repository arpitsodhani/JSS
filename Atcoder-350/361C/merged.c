#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void read_sequence(int *n, int *k, int *a) {
    scanf("%d %d", n, k);
    for (int i = 0; i < *n; i++) scanf("%d", &a[i]);
}

int sort_sequence(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}
void sort_sequence(int n, int *a) {
    qsort(a, n, sizeof(int), compare);
}

int find_minimum_range(int n, int k, int *a) {
    int remaining = n - k;
    int min_range = a[remaining - 1] - a[0];
    for (int i = 1; i + remaining - 1 < n; i++) {
        int range = a[i + remaining - 1] - a[i];
        if (range < min_range) min_range = range;
    }
    return min_range;
}

int main() {
    int n, k, a[200005];
    read_sequence(&n, &k, a);
    sort_sequence(n, a);
    printf("%d\n", find_minimum_range(n, k, a));
    return 0;
}

