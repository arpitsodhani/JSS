#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void initialize_hungarian_state(int n, int cost[105][105], int *u, int *v, int *match_x, int *match_y) {
    for (int i = 0; i < n; i++) {
        u[i] = 0;
        v[i] = 0;
        match_x[i] = -1;
        match_y[i] = -1;
        for (int j = 0; j < n; j++) {
            if (cost[i][j] > u[i]) u[i] = cost[i][j];
        }
    }
}

int find_augmenting_path_hungarian(int x, int n, int cost[105][105], int *u, int *v, int *match_y, int *visited, int *slack, int *slack_x) {
    visited[x] = 1;
    
    for (int y = 0; y < n; y++) {
        int gap = u[x] + v[y] - cost[x][y];
        if (gap == 0) {
            if (match_y[y] == -1) {
                match_y[y] = x;
                return 1;
            }
            if (find_augmenting_path_hungarian(match_y[y], n, cost, u, v, match_y, visited, slack, slack_x)) {
                match_y[y] = x;
                return 1;
            }
        } else if (gap < slack[y]) {
            slack[y] = gap;
            slack_x[y] = x;
        }
    }
    return 0;
}

int compute_maximum_weighted_matching(int n, int cost[105][105]) {
    int u[105], v[105], match_x[105], match_y[105];
    initialize_hungarian_state(n, cost, u, v, match_x, match_y);
    
    for (int x = 0; x < n; x++) {
        int slack[105], slack_x[105], visited[105];
        for (int y = 0; y < n; y++) {
            slack[y] = 1e9;
            visited[y] = 0;
        }
        
        while (1) {
            for (int i = 0; i < n; i++) visited[i] = 0;
            if (find_augmenting_path_hungarian(x, n, cost, u, v, match_y, visited, slack, slack_x)) break;
            
            int delta = 1e9;
            for (int y = 0; y < n; y++) {
                if (!visited[y] && slack[y] < delta) delta = slack[y];
            }
            
            for (int i = 0; i < n; i++) {
                if (visited[i]) u[i] -= delta;
            }
            for (int y = 0; y < n; y++) {
                if (visited[y]) v[y] += delta;
                else slack[y] -= delta;
            }
        }
    }
    
    int total = 0;
    for (int y = 0; y < n; y++) {
        if (match_y[y] != -1) total += cost[match_y[y]][y];
    }
    return total;
}

int main() {
    int n, cost[105][105];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &cost[i][j]);
        }
    }
    printf("%d\n", compute_maximum_weighted_matching(n, cost));
    return 0;
}