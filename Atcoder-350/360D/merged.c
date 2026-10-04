#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

long long read_ants(int *n, long long **positions, char **directions, long long *t) {
    scanf("%d %lld", n, t);
    *positions = malloc(*n * sizeof(long long));
    *directions = malloc((*n + 1) * sizeof(char));
    for (int i = 0; i < *n; i++) scanf("%lld", &(*positions)[i]);
    scanf("%s", *directions);
    return 0;
}

long long count_passing_pairs(int n, long long *x, char *s, long long t) {
    long long count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (s[i] == '1' && s[j] == '0') {
                long long final_i = x[i] + t;
                long long final_j = x[j] - t;
                if (x[i] < x[j] && final_i > final_j) count++;
            }
        }
    }
    return count;
}

int main() {
    int n;
    long long *x, t;
    char *s;
    read_ants(&n, &x, &s, &t);
    printf("%lld\n", count_passing_pairs(n, x, s, t));
    free(x);
    free(s);
    return 0;
}

