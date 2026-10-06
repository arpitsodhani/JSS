#include <stdio.h>
#include <stdlib.h>

void find_min_path(int** grid, int n, int k, int* result) {
    int min_row = 0, min_col = 0;
    int min_val = grid[0][0];
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] < min_val) {
                min_val = grid[i][j];
                min_row = i;
                min_col = j;
            }
        }
    }
    
    int row = min_row, col = min_col;
    for (int i = 0; i < k; i++) {
        result[i] = grid[row][col];
        if (i + 1 < k) {
            int next_row = row, next_col = col;
            int next_value = 2147483647;
            const int dr[] = {-1, 1, 0, 0};
            const int dc[] = {0, 0, -1, 1};
            for (int d = 0; d < 4; ++d) {
                int r = row + dr[d], c = col + dc[d];
                if (r >= 0 && r < n && c >= 0 && c < n && grid[r][c] < next_value) {
                    next_value = grid[r][c]; next_row = r; next_col = c;
                }
            }
            row = next_row; col = next_col;
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
    
    for (int i = 0; i < k; i++) {
        if (i > 0) printf(" ");
        printf("%d", result[i]);
    }
    printf("\n");
    
    for (int i = 0; i < n; i++) free(grid[i]);
    free(grid);
    return 0;
}
