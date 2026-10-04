#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int relax_edge_distance(long long *dist, int u, int v, int weight) {
    if (dist[u] != LLONG_MAX && dist[u] + weight < dist[v]) {
        dist[v] = dist[u] + weight;
        return 1;
    }
    return 0;
}

int detect_negative_cycle(int n, int m, int *u, int *v, int *weight, long long *dist) {
    for (int i = 0; i < m; i++) {
        if (relax_edge_distance(dist, u[i], v[i], weight[i])) {
            return 1;
        }
    }
    return 0;
}

int compute_shortest_paths_bellman_ford(int n, int m, int *u, int *v, int *weight, int source, long long *dist) {
    for (int i = 0; i < n; i++) {
        dist[i] = LLONG_MAX;
    }
    dist[source] = 0;
    
    for (int iter = 0; iter < n - 1; iter++) {
        for (int i = 0; i < m; i++) {
            relax_edge_distance(dist, u[i], v[i], weight[i]);
        }
    }
    
    return detect_negative_cycle(n, m, u, v, weight, dist);
}

int main() {
    int n, m, source, u[10005], v[10005], weight[10005];
    long long dist[1005];
    scanf("%d %d %d", &n, &m, &source);
    source--;
    for (int i = 0; i < m; i++) {
        scanf("%d %d %d", &u[i], &v[i], &weight[i]);
        u[i]--; v[i]--;
    }
    
    if (compute_shortest_paths_bellman_ford(n, m, u, v, weight, source, dist)) {
        printf("NEGATIVE CYCLE\n");
    } else {
        for (int i = 0; i < n; i++) {
            if (dist[i] == LLONG_MAX) {
                printf("INF\n");
            } else {
                printf("%lld\n", dist[i]);
            }
        }
    }
    return 0;
}