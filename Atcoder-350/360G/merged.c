#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void read_sequence(int *n, int **a) {
    scanf("%d", n);
    *a = malloc(*n * sizeof(int));
    for (int i = 0; i < *n; i++) scanf("%d", &(*a)[i]);
}

void compute_lis_arrays(int n, int *a, int *lis_left, int *lis_right) {
    int dp[200005];
    for (int i = 0; i < n; i++) {
        int pos = 0, len = i;
        for (int j = 0; j < len; j++) {
            if (dp[j] < a[i]) pos = j + 1;
        }
        dp[pos] = a[i];
        lis_left[i] = pos + 1;
    }
    for (int i = n - 1; i >= 0; i--) {
        int pos = 0, len = n - 1 - i;
        for (int j = 0; j < len; j++) {
            if (dp[j] > a[i]) pos = j + 1;
        }
        dp[pos] = a[i];
        lis_right[i] = pos + 1;
    }
}

int find_maximum_lis(int n, int *lis_left, int *lis_right) {
    int max_lis = 0;
    for (int i = 0; i < n; i++) {
        int current = lis_left[i] + lis_right[i] - 1;
        if (current > max_lis) max_lis = current;
    }
    for (int i = 0; i < n; i++) {
        int replace = (i > 0 ? lis_left[i - 1] : 0) + (i < n - 1 ? lis_right[i + 1] : 0) + 1;
        if (replace > max_lis) max_lis = replace;
    }
    return max_lis;
}

int main() {
    int n, *a;
    read_sequence(&n, &a);
    int lis_left[200005], lis_right[200005];
    compute_lis_arrays(n, a, lis_left, lis_right);
    printf("%d\n", find_maximum_lis(n, lis_left, lis_right));
    free(a);
    return 0;
}

