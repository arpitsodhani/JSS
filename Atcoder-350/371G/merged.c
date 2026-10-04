#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int create_treap_node(int value, int *keys, int *priority, int *size, int *left, int *right, int *node_count) {
    int node = (*node_count)++;
    keys[node] = value;
    priority[node] = rand();
    size[node] = 1;
    left[node] = right[node] = -1;
    return node;
}

void update_treap_size(int node, int *size, int *left, int *right) {
    if (node == -1) return;
    size[node] = 1;
    if (left[node] != -1) size[node] += size[left[node]];
    if (right[node] != -1) size[node] += size[right[node]];
}

void split_treap_by_position(int node, int pos, int *left_tree, int *right_tree, int *size, int *left, int *right) {
    if (node == -1) {
        *left_tree = *right_tree = -1;
        return;
    }
    
    int left_size = (left[node] == -1) ? 0 : size[left[node]];
    if (pos <= left_size) {
        split_treap_by_position(left[node], pos, left_tree, &left[node], size, left, right);
        *right_tree = node;
    } else {
        split_treap_by_position(right[node], pos - left_size - 1, &right[node], right_tree, size, left, right);
        *left_tree = node;
    }
    update_treap_size(node, size, left, right);
}

int merge_treap_nodes(int left_tree, int right_tree, int *priority, int *size, int *left, int *right) {
    if (left_tree == -1) return right_tree;
    if (right_tree == -1) return left_tree;
    
    if (priority[left_tree] > priority[right_tree]) {
        right[left_tree] = merge_treap_nodes(right[left_tree], right_tree, priority, size, left, right);
        update_treap_size(left_tree, size, left, right);
        return left_tree;
    } else {
        left[right_tree] = merge_treap_nodes(left_tree, left[right_tree], priority, size, left, right);
        update_treap_size(right_tree, size, left, right);
        return right_tree;
    }
}

int main() {
    int n, q, keys[100005], priority[100005], size[100005], left[100005], right[100005], node_count = 0;
    int root = -1;
    scanf("%d %d", &n, &q);
    
    for (int i = 0; i < n; i++) {
        int value;
        scanf("%d", &value);
        int node = create_treap_node(value, keys, priority, size, left, right, &node_count);
        root = merge_treap_nodes(root, node, priority, size, left, right);
    }
    
    for (int i = 0; i < q; i++) {
        int l, r, left_part, mid_part, right_part;
        scanf("%d %d", &l, &r);
        split_treap_by_position(root, l, &left_part, &right_part, size, left, right);
        split_treap_by_position(right_part, r - l + 1, &mid_part, &right_part, size, left, right);
        root = merge_treap_nodes(merge_treap_nodes(left_part, right_part, priority, size, left, right), mid_part, priority, size, left, right);
    }
    
    printf("%d\n", (root == -1) ? 0 : size[root]);
    return 0;
}