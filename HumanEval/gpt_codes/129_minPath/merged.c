#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

void minPath(int n, int k, int grid[][100], int *result) {
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
    int grid[100][100];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &grid[i][j]);
        }
    }
    int result[k];
    minPath(n, k, grid, result);
    for (int i = 0; i < k; i++) {
        printf("%d", result[i]);
        if (i < k - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
