#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

long long read_tree(int *n, int **a, int **b, long long **c) {
    scanf("%d", n);
    *a = malloc((*n - 1) * sizeof(int));
    *b = malloc((*n - 1) * sizeof(int));
    *c = malloc((*n - 1) * sizeof(long long));
    for (int i = 0; i < *n - 1; i++) {
        scanf("%d %d %lld", &(*a)[i], &(*b)[i], &(*c)[i]);
    }
    return 0;
}

long long compute_total_edge_weight(int n, long long *c) {
    long long total = 0;
    for (int i = 0; i < n - 1; i++) total += c[i];
    return total;
}

long long find_maximum_edge(int n, long long *c) {
    long long max_edge = c[0];
    for (int i = 1; i < n - 1; i++) {
        if (c[i] > max_edge) max_edge = c[i];
    }
    return max_edge;
}

long long compute_minimum_travel(long long total, long long max_edge) {
    return 2 * total - max_edge;
}

int main() {
    int n, *a, *b;
    long long *c;
    read_tree(&n, &a, &b, &c);
    long long total = compute_total_edge_weight(n, c);
    long long max_edge = find_maximum_edge(n, c);
    printf("%lld\n", compute_minimum_travel(total, max_edge));
    free(a);
    free(b);
    free(c);
    return 0;
}

