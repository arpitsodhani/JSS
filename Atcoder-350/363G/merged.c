#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_jobs_and_queries(int *n, int *q, int *d, int *r, int *queries) {
    scanf("%d %d", n, q);
    for (int i = 0; i < *n; i++) scanf("%d %d", &d[i], &r[i]);
    for (int i = 0; i < *q; i++) scanf("%d", &queries[i]);
}

long long compute_optimal_schedule(int n, int *d, int *r, int day_limit) {
    int used[55] = {0};
    long long total = 0;
    for (int day = day_limit; day >= 1; day--) {
        int best = -1;
        long long best_reward = -1;
        for (int i = 0; i < n; i++) {
            if (used[i]) continue;
            if (d[i] >= day && r[i] > best_reward) {
                best_reward = r[i];
                best = i;
            }
        }
        if (best != -1) {
            used[best] = 1;
            total += best_reward;
        }
    }
    return total;
}

int main() {
    int n, q, d[55], r[55], queries[55];
    read_jobs_and_queries(&n, &q, d, r, queries);
    for (int i = 0; i < q; i++) {
        int job = queries[i] - 1;
        d[job]++;
        r[job]++;
        printf("%lld\n", compute_optimal_schedule(n, d, r, 50));
    }
    return 0;
}
