#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_tree(int *n, int *u, int *v) {
    scanf("%d", n);
    for (int i = 0; i < *n - 1; i++) {
        scanf("%d %d", &u[i], &v[i]);
        u[i]--; v[i]--;
    }
}

void compute_tree_distances(int n, int *u, int *v, int dist[][205]) {
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) dist[i][j] = (i == j) ? 0 : 1000000;
    for (int i = 0; i < n - 1; i++) {
        dist[u[i]][v[i]] = 1;
        dist[v[i]][u[i]] = 1;
    }
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
}

void find_maximum_matching(int n, int dist[][205], int *pairs) {
    int used[205] = {0};
    int count = 0;
    for (int total = 0; total < n / 2; total++) {
        int best_i = -1, best_j = -1, best_dist = -1;
        for (int i = 0; i < n; i++) {
            if (used[i]) continue;
            for (int j = i + 1; j < n; j++) {
                if (used[j]) continue;
                if (dist[i][j] > best_dist) {
                    best_dist = dist[i][j];
                    best_i = i;
                    best_j = j;
                }
            }
        }
        pairs[count++] = best_i + 1;
        pairs[count++] = best_j + 1;
        used[best_i] = 1;
        used[best_j] = 1;
    }
}

int main() {
    int n, u[205], v[205], dist[205][205], pairs[410];
    read_tree(&n, u, v);
    compute_tree_distances(n, u, v, dist);
    find_maximum_matching(n, dist, pairs);
    for (int i = 0; i < n; i++) printf("%d%c", pairs[i], i == n - 1 ? '\n' : ' ');
    return 0;
}
