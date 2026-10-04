#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

void update_fenwick_tree(long long *tree, int n, int idx, long long delta) {
    idx++;
    while (idx <= n) {
        tree[idx] += delta;
        idx += idx & (-idx);
    }
}

long long query_prefix_sum(long long *tree, int idx) {
    idx++;
    long long sum = 0;
    while (idx > 0) {
        sum += tree[idx];
        idx -= idx & (-idx);
    }
    return sum;
}

long long compute_range_sum_fenwick(long long *tree, int left, int right) {
    if (left == 0) {
        return query_prefix_sum(tree, right);
    }
    return query_prefix_sum(tree, right) - query_prefix_sum(tree, left - 1);
}

int main() {
    int n, q;
    long long tree[100005] = {0}, array[100005];
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &array[i]);
        update_fenwick_tree(tree, n, i, array[i]);
    }
    
    for (int i = 0; i < q; i++) {
        int type, a, b;
        scanf("%d %d %d", &type, &a, &b);
        if (type == 1) {
            long long delta = b - array[a];
            array[a] = b;
            update_fenwick_tree(tree, n, a, delta);
        } else {
            printf("%lld\n", compute_range_sum_fenwick(tree, a, b));
        }
    }
    return 0;
}