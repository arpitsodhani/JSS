#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void read_input(int *n, int *k, int *x, int *a) {
    scanf("%d %d %d", n, k, x);
    for (int i = 0; i < *n; i++) scanf("%d", &a[i]);
}

void insert_and_print(int n, int k, int x, int *a) {
    for (int i = 0; i < k; i++) printf("%d ", a[i]);
    printf("%d ", x);
    for (int i = k; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main() {
    int n, k, x, a[105];
    read_input(&n, &k, &x, a);
    insert_and_print(n, k, x, a);
    return 0;
}

