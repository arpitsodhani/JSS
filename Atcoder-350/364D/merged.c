#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void compute_distances_to_query_point(int n, long long *points, long long query_pos, long long *distances) {
    for (int i = 0; i < n; i++) {
        long long diff = points[i] - query_pos;
        distances[i] = diff >= 0 ? diff : -diff;
    }
}

void sort_distances_ascending(int n, long long *distances) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (distances[j] < distances[i]) {
                long long tmp = distances[i];
                distances[i] = distances[j];
                distances[j] = tmp;
            }
        }
    }
}

long long extract_kth_smallest_distance(long long *sorted_distances, int k) {
    return sorted_distances[k - 1];
}

void process_distance_queries(int n, int q, long long *points, long long *query_positions, int *k_values, long long *results) {
    for (int qi = 0; qi < q; qi++) {
        long long distances[200005];
        compute_distances_to_query_point(n, points, query_positions[qi], distances);
        sort_distances_ascending(n, distances);
        results[qi] = extract_kth_smallest_distance(distances, k_values[qi]);
    }
}

int main() {
    int n, q;
    long long points[200005], query_positions[200005], results[200005];
    int k_values[200005];
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) scanf("%lld", &points[i]);
    for (int i = 0; i < q; i++) scanf("%lld %d", &query_positions[i], &k_values[i]);
    process_distance_queries(n, q, points, query_positions, k_values, results);
    for (int i = 0; i < q; i++) printf("%lld\n", results[i]);
    return 0;
}