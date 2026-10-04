#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

void initialize_distance_matrix(int n, long long dist[505][505]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                dist[i][j] = 0;
            } else {
                dist[i][j] = 1000000000000LL;
            }
        }
    }
}

void relax_path_through_intermediate(int n, long long dist[505][505], int k) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (dist[i][k] + dist[k][j] < dist[i][j]) {
                dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }
}

void compute_all_pairs_shortest_paths(int n, long long dist[505][505]) {
    for (int k = 0; k < n; k++) {
        relax_path_through_intermediate(n, dist, k);
    }
}

int main() {
    int n, m;
    long long dist[505][505];
    scanf("%d %d", &n, &m);
    initialize_distance_matrix(n, dist);
    
    for (int i = 0; i < m; i++) {
        int u, v;
        long long w;
        scanf("%d %d %lld", &u, &v, &w);
        u--; v--;
        dist[u][v] = w;
    }
    
    compute_all_pairs_shortest_paths(n, dist);
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (dist[i][j] == 1000000000000LL) {
                printf("INF ");
            } else {
                printf("%lld ", dist[i][j]);
            }
        }
        printf("\n");
    }
    return 0;
}