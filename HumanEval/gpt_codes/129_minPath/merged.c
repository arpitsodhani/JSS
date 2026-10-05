#include <stdio.h>
#include <stdlib.h>

void find_min_path(int** grid, int n, int k, int* result) {
    int min_val = grid[0][0];
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] < min_val) {
                min_val = grid[i][j];
            }
        }
    }
    
    for (int i = 0; i < k; i++) {
        if (i % 2 == 0) {
            result[i] = 1;
        } else {
            result[i] = min_val;
        }
    }
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    
    int** grid = malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        grid[i] = malloc(n * sizeof(int));
        for (int j = 0; j < n; j++) {
            scanf("%d", &grid[i][j]);
        }
    }
    
    int result[1000];
    find_min_path(grid, n, k, result);
    
    printf("[");
    for (int i = 0; i < k; i++) {
        if (i > 0) printf(", ");
        printf("%d", result[i]);
    }
    printf("]\n");
    
    for (int i = 0; i < n; i++) free(grid[i]);
    free(grid);
    return 0;
}
