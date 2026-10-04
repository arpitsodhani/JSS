#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>

long long compute_gcd_euclidean(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

long long compute_array_gcd(int n, long long *array) {
    long long result = array[0];
    for (int i = 1; i < n; i++) {
        result = compute_gcd_euclidean(result, array[i]);
    }
    return result;
}

void process_gcd_queries(int q, int *query_lengths, long long queries[105][105], long long *results) {
    for (int i = 0; i < q; i++) {
        results[i] = compute_array_gcd(query_lengths[i], queries[i]);
    }
}

int main() {
    int q, query_lengths[105];
    long long queries[105][105], results[105];
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        scanf("%d", &query_lengths[i]);
        for (int j = 0; j < query_lengths[i]; j++) {
            scanf("%lld", &queries[i][j]);
        }
    }
    process_gcd_queries(q, query_lengths, queries, results);
    for (int i = 0; i < q; i++) {
        printf("%lld\n", results[i]);
    }
    return 0;
}