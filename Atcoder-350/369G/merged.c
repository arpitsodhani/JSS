#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void build_segment_tree(int *array, int *tree, int node, int start, int end) {
    if (start == end) {
        tree[node] = array[start];
    } else {
        int mid = (start + end) / 2;
        build_segment_tree(array, tree, 2*node, start, mid);
        build_segment_tree(array, tree, 2*node+1, mid+1, end);
        tree[node] = tree[2*node] < tree[2*node+1] ? tree[2*node] : tree[2*node+1];
    }
}

int query_range_minimum(int *tree, int node, int start, int end, int left, int right) {
    if (right < start || end < left) return 1000000000;
    if (left <= start && end <= right) return tree[node];
    int mid = (start + end) / 2;
    int left_min = query_range_minimum(tree, 2*node, start, mid, left, right);
    int right_min = query_range_minimum(tree, 2*node+1, mid+1, end, left, right);
    return left_min < right_min ? left_min : right_min;
}

void update_segment_tree_point(int *tree, int node, int start, int end, int idx, int value) {
    if (start == end) {
        tree[node] = value;
    } else {
        int mid = (start + end) / 2;
        if (idx <= mid) {
            update_segment_tree_point(tree, 2*node, start, mid, idx, value);
        } else {
            update_segment_tree_point(tree, 2*node+1, mid+1, end, idx, value);
        }
        tree[node] = tree[2*node] < tree[2*node+1] ? tree[2*node] : tree[2*node+1];
    }
}

int main() {
    int n, q, array[100005], tree[400005];
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) scanf("%d", &array[i]);
    build_segment_tree(array, tree, 1, 0, n-1);
    
    for (int i = 0; i < q; i++) {
        int type, a, b;
        scanf("%d %d %d", &type, &a, &b);
        if (type == 1) {
            update_segment_tree_point(tree, 1, 0, n-1, a, b);
        } else {
            printf("%d\n", query_range_minimum(tree, 1, 0, n-1, a, b));
        }
    }
    return 0;
}