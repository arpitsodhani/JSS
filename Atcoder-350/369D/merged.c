#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int find_augmenting_path_bfs(int n, int capacity[105][105], int *parent, int source, int sink) {
    int visited[105] = {0};
    int queue[105], front = 0, rear = 0;
    queue[rear++] = source;
    visited[source] = 1;
    parent[source] = -1;
    
    while (front < rear) {
        int u = queue[front++];
        for (int v = 0; v < n; v++) {
            if (!visited[v] && capacity[u][v] > 0) {
                parent[v] = u;
                visited[v] = 1;
                if (v == sink) return 1;
                queue[rear++] = v;
            }
        }
    }
    return 0;
}

int compute_path_bottleneck(int capacity[105][105], int *parent, int sink) {
    int min_capacity = 1000000000;
    for (int v = sink; parent[v] != -1; v = parent[v]) {
        int u = parent[v];
        if (capacity[u][v] < min_capacity) {
            min_capacity = capacity[u][v];
        }
    }
    return min_capacity;
}

int compute_maximum_flow(int n, int capacity[105][105], int source, int sink) {
    int max_flow = 0;
    int parent[105];
    
    while (find_augmenting_path_bfs(n, capacity, parent, source, sink)) {
        int flow = compute_path_bottleneck(capacity, parent, sink);
        for (int v = sink; parent[v] != -1; v = parent[v]) {
            int u = parent[v];
            capacity[u][v] -= flow;
            capacity[v][u] += flow;
        }
        max_flow += flow;
    }
    return max_flow;
}

int main() {
    int n, m, source, sink, capacity[105][105] = {{0}};
    scanf("%d %d %d %d", &n, &m, &source, &sink);
    source--; sink--;
    for (int i = 0; i < m; i++) {
        int u, v, cap;
        scanf("%d %d %d", &u, &v, &cap);
        u--; v--;
        capacity[u][v] = cap;
    }
    printf("%d\n", compute_maximum_flow(n, capacity, source, sink));
    return 0;
}