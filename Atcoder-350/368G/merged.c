#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>

void compute_node_indegrees(int n, int adj[1005][1005], int *adj_count, int *indegree) {
    for (int i = 0; i < n; i++) {
        indegree[i] = 0;
    }
    for (int u = 0; u < n; u++) {
        for (int i = 0; i < adj_count[u]; i++) {
            int v = adj[u][i];
            indegree[v]++;
        }
    }
}

int find_zero_indegree_node(int n, int *indegree, int *processed) {
    for (int i = 0; i < n; i++) {
        if (!processed[i] && indegree[i] == 0) {
            return i;
        }
    }
    return -1;
}

int generate_topological_order(int n, int adj[1005][1005], int *adj_count, int *order) {
    int indegree[1005], processed[1005] = {0};
    compute_node_indegrees(n, adj, adj_count, indegree);
    int count = 0;
    
    while (1) {
        int node = find_zero_indegree_node(n, indegree, processed);
        if (node == -1) break;
        processed[node] = 1;
        order[count++] = node;
        for (int i = 0; i < adj_count[node]; i++) {
            indegree[adj[node][i]]--;
        }
    }
    return count;
}

int main() {
    int n, m, adj[1005][1005], adj_count[1005] = {0}, order[1005];
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--; v--;
        adj[u][adj_count[u]++] = v;
    }
    int count = generate_topological_order(n, adj, adj_count, order);
    if (count != n) {
        printf("-1\n");
    } else {
        for (int i = 0; i < n; i++) {
            printf("%d ", order[i] + 1);
        }
    }
    return 0;
}