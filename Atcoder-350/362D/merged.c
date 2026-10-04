#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void read_graph(int *n, int *m, long long *a, int *u, int *v, long long *b) {
    scanf("%d %d", n, m);
    for (int i = 0; i < *n; i++) scanf("%lld", &a[i]);
    for (int i = 0; i < *m; i++) {
        scanf("%d %d %lld", &u[i], &v[i], &b[i]);
        u[i]--;
        v[i]--;
    }
}

void build_adjacency_list(int n, int m, int *u, int *v, long long *b, int *head, int *next_edge, int *to, long long *weight) {
    for (int i = 0; i < n; i++) head[i] = -1;
    for (int i = 0; i < m; i++) {
        next_edge[2 * i] = head[u[i]];
        to[2 * i] = v[i];
        weight[2 * i] = b[i];
        head[u[i]] = 2 * i;
        next_edge[2 * i + 1] = head[v[i]];
        to[2 * i + 1] = u[i];
        weight[2 * i + 1] = b[i];
        head[v[i]] = 2 * i + 1;
    }
}

void dijkstra_shortest_paths(int n, long long *a, int *head, int *next_edge, int *to, long long *weight, long long *dist) {
    for (int i = 0; i < n; i++) dist[i] = 1e18;
    dist[0] = a[0];
    int visited[200005] = {0};
    for (int iter = 0; iter < n; iter++) {
        int u = -1;
        for (int i = 0; i < n; i++) {
            if (!visited[i] && (u == -1 || dist[i] < dist[u])) u = i;
        }
        if (u == -1 || dist[u] == 1e18) break;
        visited[u] = 1;
        for (int e = head[u]; e != -1; e = next_edge[e]) {
            int v = to[e];
            long long new_dist = dist[u] + weight[e] + a[v];
            if (new_dist < dist[v]) dist[v] = new_dist;
        }
    }
}

int main() {
    int n, m;
    long long a[200005], b[400005];
    int u[400005], v[400005];
    read_graph(&n, &m, a, u, v, b);
    int head[200005], next_edge[800005], to[800005];
    long long weight[800005];
    build_adjacency_list(n, m, u, v, b, head, next_edge, to, weight);
    long long dist[200005];
    dijkstra_shortest_paths(n, a, head, next_edge, to, weight, dist);
    for (int i = 1; i < n; i++) printf("%lld%c", dist[i], i == n - 1 ? '\n' : ' ');
    return 0;
}

