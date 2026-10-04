#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int find_set_with_compression(int *parent, int x) {
    if (parent[x] != x) {
        parent[x] = find_set_with_compression(parent, parent[x]);
    }
    return parent[x];
}

void union_sets_by_rank(int *parent, int *rank, int x, int y) {
    int root_x = find_set_with_compression(parent, x);
    int root_y = find_set_with_compression(parent, y);
    
    if (root_x != root_y) {
        if (rank[root_x] < rank[root_y]) {
            parent[root_x] = root_y;
        } else if (rank[root_x] > rank[root_y]) {
            parent[root_y] = root_x;
        } else {
            parent[root_y] = root_x;
            rank[root_x]++;
        }
    }
}

int check_same_component(int *parent, int x, int y) {
    return find_set_with_compression(parent, x) == find_set_with_compression(parent, y);
}

int main() {
    int n, q, parent[100005], rank[100005];
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) {
        parent[i] = i;
        rank[i] = 0;
    }
    
    for (int i = 0; i < q; i++) {
        int type, x, y;
        scanf("%d %d %d", &type, &x, &y);
        x--; y--;
        if (type == 1) {
            union_sets_by_rank(parent, rank, x, y);
        } else {
            printf("%s\n", check_same_component(parent, x, y) ? "Yes" : "No");
        }
    }
    return 0;
}