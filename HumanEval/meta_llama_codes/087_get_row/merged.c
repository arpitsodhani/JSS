#include <stdio.h>
#include <stdlib.h>

void find_coordinates(int** grid, int rows, int cols, int x, int* result, int* result_size) {
    *result_size = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == x) {
                result[(*result_size)++] = i;
                result[(*result_size)++] = j;
            }
        }
    }
    
    
    for (int i = 0; i < *result_size; i += 2) {
        for (int j = i + 2; j < *result_size; j += 2) {
            if (result[i] < result[j] || (result[i] == result[j] && result[i+1] < result[j+1])) {
                int tmp = result[i];
                result[i] = result[j];
                result[j] = tmp;
                tmp = result[i+1];
                result[i+1] = result[j+1];
                result[j+1] = tmp;
            }
        }
    }
}

int main() {
    int rows, cols, x;
    scanf("%d %d", &rows, &cols);
    
    int** grid = malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; i++) {
        grid[i] = malloc(cols * sizeof(int));
        for (int j = 0; j < cols; j++) {
            scanf("%d", &grid[i][j]);
        }
    }
    scanf("%d", &x);
    
    int result[1000];
    int result_size;
    find_coordinates(grid, rows, cols, x, result, &result_size);
    
    for (int i = 0; i < result_size; i += 2) {
        if (i > 0) printf("\n");
        printf("%d %d", result[i], result[i+1]);
    }
    if (result_size) printf("\n");
    
    for (int i = 0; i < rows; i++) free(grid[i]);
    free(grid);
    return 0;
}
