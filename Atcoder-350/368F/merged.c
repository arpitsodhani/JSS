#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>

int compute_range_xor(int *array, int left, int right) {
    int xor_result = 0;
    for (int i = left; i <= right; i++) {
        xor_result ^= array[i];
    }
    return xor_result;
}

void update_array_element(int *array, int position, int value) {
    array[position] = value;
}

void process_xor_queries(int n, int *array, int q, int query_types[], int query_params[][2], int *results, int *result_count) {
    for (int i = 0; i < q; i++) {
        if (query_types[i] == 1) {
            update_array_element(array, query_params[i][0], query_params[i][1]);
        } else {
            results[*result_count] = compute_range_xor(array, query_params[i][0], query_params[i][1]);
            (*result_count)++;
        }
    }
}

int main() {
    int n, q, array[100005], query_types[100005], query_params[100005][2], results[100005], result_count = 0;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) scanf("%d", &array[i]);
    for (int i = 0; i < q; i++) {
        scanf("%d %d %d", &query_types[i], &query_params[i][0], &query_params[i][1]);
    }
    process_xor_queries(n, array, q, query_types, query_params, results, &result_count);
    for (int i = 0; i < result_count; i++) {
        printf("%d\n", results[i]);
    }
    return 0;
}