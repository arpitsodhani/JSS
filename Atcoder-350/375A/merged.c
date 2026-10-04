void perform_dfs_heavy_light(int node, int parent) {
    int max_subtree = -1;
    subtree_size[node] = 1;
    for (int i = 0; i < adj_count[node]; i++) {
        int child = adj[node][i];
        if (child == parent) continue;
        perform_dfs_heavy_light(child, node);
        subtree_size[node] += subtree_size[child];
        if (max_subtree == -1 || subtree_size[child] > subtree_size[max_subtree])
            max_subtree = child;
    }
    heavy_child[node] = max_subtree;
}

void decompose_tree_chains(int node, int parent, int chain_head) {
    chain_top[node] = chain_head;
    chain_pos[node] = chain_counter++;
    if (heavy_child[node] != -1)
        decompose_tree_chains(heavy_child[node], node, chain_head);
    for (int i = 0; i < adj_count[node]; i++) {
        int child = adj[node][i];
        if (child == parent || child == heavy_child[node]) continue;
        decompose_tree_chains(child, node, child);
    }
}

long long query_path_heavy_light(int u, int v) {
    long long result = 0;
    while (chain_top[u] != chain_top[v]) {
        if (depth[chain_top[u]] < depth[chain_top[v]]) {
            int temp = u; u = v; v = temp;
        }
        result += segment_tree_query(chain_pos[chain_top[u]], chain_pos[u]);
        u = parent[chain_top[u]];
    }
    if (depth[u] > depth[v]) {
        int temp = u; u = v; v = temp;
    }
    result += segment_tree_query(chain_pos[u], chain_pos[v]);
    return result;
}

void initialize_hld_arrays(int n) {
    for (int i = 0; i < n; i++) {
        heavy_child[i] = -1;
        subtree_size[i] = 0;
        chain_top[i] = i;
        chain_pos[i] = 0;
    }
}

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        adj[u][adj_count[u]++] = v;
        adj[v][adj_count[v]++] = u;
    }
    perform_dfs_heavy_light(0, -1);
    decompose_tree_chains(0, -1, 0);
    for (int i = 0; i < q; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        printf("%lld\n", query_path_heavy_light(u, v));
    }
    return 0;
}

