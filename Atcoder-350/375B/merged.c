int compute_subtree_size_centroid(int node, int parent) {
    subtree_size[node] = 1;
    for (int i = 0; i < adj_count[node]; i++) {
        int child = adj[node][i];
        if (child == parent || removed[child]) continue;
        subtree_size[node] += compute_subtree_size_centroid(child, node);
    }
    return subtree_size[node];
}

int find_tree_centroid(int node, int parent, int tree_size) {
    for (int i = 0; i < adj_count[node]; i++) {
        int child = adj[node][i];
        if (child == parent || removed[child]) continue;
        if (subtree_size[child] * 2 > tree_size)
            return find_tree_centroid(child, node, tree_size);
    }
    return node;
}

void decompose_centroid_recursive(int node, int parent_centroid) {
    int tree_size = compute_subtree_size_centroid(node, -1);
    int centroid = find_tree_centroid(node, -1, tree_size);
    removed[centroid] = 1;
    centroid_parent[centroid] = parent_centroid;
    for (int i = 0; i < adj_count[centroid]; i++) {
        int child = adj[centroid][i];
        if (!removed[child])
            decompose_centroid_recursive(child, centroid);
    }
}

void mark_removed_subtree(int node) {
    removed[node] = 1;
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        adj[u][adj_count[u]++] = v;
        adj[v][adj_count[v]++] = u;
    }
    decompose_centroid_recursive(0, -1);
    printf("%d\n", centroid_parent[0]);
    return 0;
}

