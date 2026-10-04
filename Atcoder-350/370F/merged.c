#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

void push_lazy_updates(long long *tree, long long *lazy, int node, int start, int end) {
    if (lazy[node] != 0) {
        tree[node] += (end - start + 1) * lazy[node];
        if (start != end) {
            lazy[2*node] += lazy[node];
            lazy[2*node+1] += lazy[node];
        }
        lazy[node] = 0;
    }
}

void update_range_lazy(long long *tree, long long *lazy, int node, int start, int end, int left, int right, long long value) {
    push_lazy_updates(tree, lazy, node, start, end);
    if (start > right || end < left) return;
    
    if (left <= start && end <= right) {
        lazy[node] += value;
        push_lazy_updates(tree, lazy, node, start, end);
        return;
    }
    
    int mid = (start + end) / 2;
    update_range_lazy(tree, lazy, 2*node, start, mid, left, right, value);
    update_range_lazy(tree, lazy, 2*node+1, mid+1, end, left, right, value);
    
    push_lazy_updates(tree, lazy, 2*node, start, mid);
    push_lazy_updates(tree, lazy, 2*node+1, mid+1, end);
    tree[node] = tree[2*node] + tree[2*node+1];
}

long long query_range_sum_lazy(long long *tree, long long *lazy, int node, int start, int end, int left, int right) {
    if (start > right || end < left) return 0;
    push_lazy_updates(tree, lazy, node, start, end);
    
    if (left <= start && end <= right) {
        return tree[node];
    }
    
    int mid = (start + end) / 2;
    long long left_sum = query_range_sum_lazy(tree, lazy, 2*node, start, mid, left, right);
    long long right_sum = query_range_sum_lazy(tree, lazy, 2*node+1, mid+1, end, left, right);
    return left_sum + right_sum;
}

int main() {
    int n, q;
    long long tree[400005] = {0}, lazy[400005] = {0};
    scanf("%d %d", &n, &q);
    
    for (int i = 0; i < q; i++) {
        int type, left, right;
        scanf("%d %d %d", &type, &left, &right);
        if (type == 1) {
            long long value;
            scanf("%lld", &value);
            update_range_lazy(tree, lazy, 1, 0, n-1, left, right, value);
        } else {
            printf("%lld\n", query_range_sum_lazy(tree, lazy, 1, 0, n-1, left, right));
        }
    }
    return 0;
}