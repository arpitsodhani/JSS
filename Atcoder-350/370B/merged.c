#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

void sort_edges_by_weight(int m, int *u, int *v, int *weight) {
    for (int i = 0; i < m - 1; i++) {
        for (int j = i + 1; j < m; j++) {
            if (weight[j] < weight[i]) {
                int tmp = weight[i]; weight[i] = weight[j]; weight[j] = tmp;
                tmp = u[i]; u[i] = u[j]; u[j] = tmp;
                tmp = v[i]; v[i] = v[j]; v[j] = tmp;
            }
        }
    }
}

int find_with_path_compression(int *parent, int x) {
    if (parent[x] != x) {
        parent[x] = find_with_path_compression(parent, parent[x]);
    }
    return parent[x];
}

long long compute_minimum_spanning_tree(int n, int m, int *u, int *v, int *weight) {
    int parent[1005];
    for (int i = 0; i < n; i++) parent[i] = i;
    
    sort_edges_by_weight(m, u, v, weight);
    long long mst_cost = 0;
    int edges_added = 0;
    
    for (int i = 0; i < m && edges_added < n - 1; i++) {
        int root_u = find_with_path_compression(parent, u[i]);
        int root_v = find_with_path_compression(parent, v[i]);
        if (root_u != root_v) {
            parent[root_u] = root_v;
            mst_cost += weight[i];
            edges_added++;
        }
    }
    return mst_cost;
}

int main() {
    int n, m, u[100005], v[100005], weight[100005];
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        scanf("%d %d %d", &u[i], &v[i], &weight[i]);
        u[i]--; v[i]--;
    }
    printf("%lld\n", compute_minimum_spanning_tree(n, m, u, v, weight));
    return 0;
}