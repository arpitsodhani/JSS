#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int find_component_root(int node, int *parent) {
    while (parent[node] != node) {
        node = parent[node];
    }
    return node;
}

void merge_components(int u, int v, int *parent) {
    int root_u = find_component_root(u, parent);
    int root_v = find_component_root(v, parent);
    if (root_u != root_v) {
        parent[root_u] = root_v;
    }
}

int verify_single_component(int n, int *parent) {
    int global_root = find_component_root(0, parent);
    for (int i = 1; i < n; i++) {
        int node_root = find_component_root(i, parent);
        if (node_root != global_root) {
            return 0;
        }
    }
    return 1;
}

void process_graph_edges(int n, int m, int *u, int *v, int *parent) {
    for (int i = 0; i < n; i++) parent[i] = i;
    for (int i = 0; i < m; i++) {
        merge_components(u[i], v[i], parent);
    }
}

int main() {
    int n, m, u[100005], v[100005], parent[100005];
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &u[i], &v[i]);
        u[i]--; v[i]--;
    }
    process_graph_edges(n, m, u, v, parent);
    printf("%s\n", verify_single_component(n, parent) ? "Yes" : "No");
    return 0;
}