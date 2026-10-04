#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int build_level_graph_bfs(int n1, int adj[1005][1005], int *deg, int *pair_u, int *pair_v, int *dist) {
    int queue[1005], front = 0, rear = 0;
    
    for (int u = 0; u < n1; u++) {
        if (pair_u[u] == -1) {
            dist[u] = 0;
            queue[rear++] = u;
        } else {
            dist[u] = 1e9;
        }
    }
    dist[n1] = 1e9;
    
    while (front < rear) {
        int u = queue[front++];
        if (dist[u] < dist[n1]) {
            for (int i = 0; i < deg[u]; i++) {
                int v = adj[u][i];
                if (dist[pair_v[v]] == 1e9) {
                    dist[pair_v[v]] = dist[u] + 1;
                    queue[rear++] = pair_v[v];
                }
            }
        }
    }
    return dist[n1] != 1e9;
}

int find_augmenting_path_dfs(int u, int n1, int adj[1005][1005], int *deg, int *pair_u, int *pair_v, int *dist) {
    if (u == n1) return 1;
    
    for (int i = 0; i < deg[u]; i++) {
        int v = adj[u][i];
        if (dist[pair_v[v]] == dist[u] + 1) {
            if (find_augmenting_path_dfs(pair_v[v], n1, adj, deg, pair_u, pair_v, dist)) {
                pair_v[v] = u;
                pair_u[u] = v;
                return 1;
            }
        }
    }
    dist[u] = 1e9;
    return 0;
}

int compute_maximum_bipartite_matching(int n1, int n2, int adj[1005][1005], int *deg) {
    int pair_u[1005], pair_v[1005], dist[1005];
    for (int i = 0; i < n1; i++) pair_u[i] = -1;
    for (int i = 0; i < n2; i++) pair_v[i] = n1;
    
    int matching = 0;
    while (build_level_graph_bfs(n1, adj, deg, pair_u, pair_v, dist)) {
        for (int u = 0; u < n1; u++) {
            if (pair_u[u] == -1 && find_augmenting_path_dfs(u, n1, adj, deg, pair_u, pair_v, dist)) {
                matching++;
            }
        }
    }
    return matching;
}

int main() {
    int n1, n2, m, adj[1005][1005], deg[1005] = {0};
    scanf("%d %d %d", &n1, &n2, &m);
    
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        adj[u][deg[u]++] = v;
    }
    
    printf("%d\n", compute_maximum_bipartite_matching(n1, n2, adj, deg));
    return 0;
}