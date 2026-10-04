#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void mark_node_as_visited(int *visited, int node) {
    visited[node] = 1;
}

int search_hamiltonian_path_dfs(int n, int adj[105][105], int *adj_count, int node, int *visited, int count) {
    mark_node_as_visited(visited, node);
    if (count == n) return 1;
    
    for (int i = 0; i < adj_count[node]; i++) {
        int neighbor = adj[node][i];
        if (!visited[neighbor]) {
            if (search_hamiltonian_path_dfs(n, adj, adj_count, neighbor, visited, count + 1)) {
                return 1;
            }
        }
    }
    visited[node] = 0;
    return 0;
}

int check_hamiltonian_path_exists(int n, int adj[105][105], int *adj_count) {
    for (int start = 0; start < n; start++) {
        int visited[105] = {0};
        if (search_hamiltonian_path_dfs(n, adj, adj_count, start, visited, 1)) {
            return 1;
        }
    }
    return 0;
}

int main() {
    int n, m, adj[105][105], adj_count[105] = {0};
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--; v--;
        adj[u][adj_count[u]++] = v;
        adj[v][adj_count[v]++] = u;
    }
    printf("%s\n", check_hamiltonian_path_exists(n, adj, adj_count) ? "Yes" : "No");
    return 0;
}