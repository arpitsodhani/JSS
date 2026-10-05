#include <math.h>
#include <stdio.h>

int calculate_total_buckets(int **grid, int rows, int cols, int capacity) {
    int total = 0;
    for (int i = 0; i < rows; i++) {
        int max_in_row = 0;
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] > max_in_row) {
                max_in_row = grid[i][j];
            }
        }
        total += (max_in_row + capacity - 1) / capacity;
    }
    return total;
}

int main(void) {
    int rows, cols, capacity;
    scanf("%d %d %d", &rows, &cols, &capacity);
    int **grid = malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; i++) {
        grid[i] = malloc(cols * sizeof(int));
        for (int j = 0; j < cols; j++) {
            scanf("%d", &grid[i][j]);
        }
    }
    int result = calculate_total_buckets(grid, rows, cols, capacity);
    printf("%d\n", result);
    for (int i = 0; i < rows; i++) {
        free(grid[i]);
    }
    free(grid);
    return 0;
}
