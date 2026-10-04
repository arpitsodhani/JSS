#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

void compute_subtree_sizes(int node, int parent, int adj[1005][1005], int *adj_count, int *subtree_size) {
    subtree_size[node] = 1;
    for (int i = 0; i < adj_count[node]; i++) {
        int child = adj[node][i];
        if (child != parent) {
            compute_subtree_sizes(child, node, adj, adj_count, subtree_size);
            subtree_size[node] += subtree_size[child];
        }
    }
}

void decompose_into_heavy_chains(int node, int parent, int adj[1005][1005], int *adj_count, int *subtree_size, int *chain_id, int *current_chain, int *chain_head) {
    if (chain_head[*current_chain] == -1) {
        chain_head[*current_chain] = node;
    }
    chain_id[node] = *current_chain;
    
    int heavy_child = -1, max_size = 0;
    for (int i = 0; i < adj_count[node]; i++) {
        int child = adj[node][i];
        if (child != parent && subtree_size[child] > max_size) {
            max_size = subtree_size[child];
            heavy_child = child;
        }
    }
    
    if (heavy_child != -1) {
        decompose_into_heavy_chains(heavy_child, node, adj, adj_count, subtree_size, chain_id, current_chain, chain_head);
    }
    
    for (int i = 0; i < adj_count[node]; i++) {
        int child = adj[node][i];
        if (child != parent && child != heavy_child) {
            (*current_chain)++;
            decompose_into_heavy_chains(child, node, adj, adj_count, subtree_size, chain_id, current_chain, chain_head);
        }
    }
}

int query_path_in_tree(int u, int v, int *chain_id, int *parent) {
    int result = 0;
    while (chain_id[u] != chain_id[v]) {
        if (chain_id[u] < chain_id[v]) {
            int tmp = u; u = v; v = tmp;
        }
        result++;
        u = parent[u];
    }
    return result;
}

int main() {
    int n, q, adj[1005][1005], adj_count[1005] = {0}, subtree_size[1005], chain_id[1005], parent[1005];
    int current_chain = 0, chain_head[1005];
    for (int i = 0; i < 1005; i++) chain_head[i] = -1;
    
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--; v--;
        adj[u][adj_count[u]++] = v;
        adj[v][adj_count[v]++] = u;
        parent[v] = u;
    }
    
    compute_subtree_sizes(0, -1, adj, adj_count, subtree_size);
    decompose_into_heavy_chains(0, -1, adj, adj_count, subtree_size, chain_id, &current_chain, chain_head);
    
    for (int i = 0; i < q; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--; v--;
        printf("%d\n", query_path_in_tree(u, v, chain_id, parent));
    }
    return 0;
}