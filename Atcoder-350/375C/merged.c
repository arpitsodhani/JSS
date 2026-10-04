int create_persistent_node(int left, int right, long long value) {
    persistent_tree[node_counter].left = left;
    persistent_tree[node_counter].right = right;
    persistent_tree[node_counter].sum = value;
    return node_counter++;
}

int update_persistent_tree(int node, int left, int right, int pos, long long val) {
    if (left == right) {
        return create_persistent_node(-1, -1, val);
    }
    int mid = (left + right) / 2;
    int new_left = persistent_tree[node].left;
    int new_right = persistent_tree[node].right;
    if (pos <= mid)
        new_left = update_persistent_tree(persistent_tree[node].left, left, mid, pos, val);
    else
        new_right = update_persistent_tree(persistent_tree[node].right, mid + 1, right, pos, val);
    long long new_sum = persistent_tree[new_left].sum + persistent_tree[new_right].sum;
    return create_persistent_node(new_left, new_right, new_sum);
}

long long query_persistent_range(int node, int left, int right, int qleft, int qright) {
    if (qleft > right || qright < left) return 0;
    if (qleft <= left && right <= qright) return persistent_tree[node].sum;
    int mid = (left + right) / 2;
    long long left_sum = query_persistent_range(persistent_tree[node].left, left, mid, qleft, qright);
    long long right_sum = query_persistent_range(persistent_tree[node].right, mid + 1, right, qleft, qright);
    return left_sum + right_sum;
}

long long get_tree_sum(int node) {
    if (node == -1) return 0;
    return persistent_tree[node].sum;
}

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    version_root[0] = create_persistent_node(-1, -1, 0);
    for (int i = 0; i < q; i++) {
        int type, ver, pos;
        scanf("%d %d %d", &type, &ver, &pos);
        if (type == 1) {
            long long val;
            scanf("%lld", &val);
            version_root[i + 1] = update_persistent_tree(version_root[ver], 0, n - 1, pos, val);
        } else {
            int qright;
            scanf("%d", &qright);
            printf("%lld\n", query_persistent_range(version_root[ver], 0, n - 1, pos, qright));
        }
    }
    return 0;
}

