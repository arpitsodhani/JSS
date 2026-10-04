#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check_value_in_range(int value, int min_val, int max_val) {
    return value > min_val && value < max_val;
}

int validate_bst_subtree(int *tree, int *left, int *right, int node, int min_val, int max_val) {
    if (node == -1) return 1;
    if (!check_value_in_range(tree[node], min_val, max_val)) return 0;
    return validate_bst_subtree(tree, left, right, left[node], min_val, tree[node]) &&
           validate_bst_subtree(tree, left, right, right[node], tree[node], max_val);
}

int verify_binary_search_tree(int *tree, int *left, int *right, int root) {
    return validate_bst_subtree(tree, left, right, root, -1000000000, 1000000000);
}

int main() {
    int n, root, tree[10005], left[10005], right[10005];
    scanf("%d %d", &n, &root);
    for (int i = 0; i < n; i++) {
        scanf("%d %d %d", &tree[i], &left[i], &right[i]);
    }
    printf("%s\n", verify_binary_search_tree(tree, left, right, root) ? "Yes" : "No");
    return 0;
}