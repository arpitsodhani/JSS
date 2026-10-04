#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int find_pivot_row(int n, double matrix[105][105], int col, int start_row) {
    int pivot = start_row;
    for (int i = start_row + 1; i < n; i++) {
        if (fabs(matrix[i][col]) > fabs(matrix[pivot][col])) {
            pivot = i;
        }
    }
    return pivot;
}

void eliminate_column_below(int n, double matrix[105][105], int row, int col) {
    for (int i = row + 1; i < n; i++) {
        double factor = matrix[i][col] / matrix[row][col];
        for (int j = col; j <= n; j++) {
            matrix[i][j] -= factor * matrix[row][j];
        }
    }
}

void perform_back_substitution(int n, double matrix[105][105], double *solution) {
    for (int i = n - 1; i >= 0; i--) {
        solution[i] = matrix[i][n];
        for (int j = i + 1; j < n; j++) {
            solution[i] -= matrix[i][j] * solution[j];
        }
        solution[i] /= matrix[i][i];
    }
}

int solve_linear_system(int n, double matrix[105][105], double *solution) {
    for (int col = 0; col < n; col++) {
        int pivot = find_pivot_row(n, matrix, col, col);
        if (fabs(matrix[pivot][col]) < 1e-9) return 0;
        
        for (int j = 0; j <= n; j++) {
            double tmp = matrix[col][j];
            matrix[col][j] = matrix[pivot][j];
            matrix[pivot][j] = tmp;
        }
        
        eliminate_column_below(n, matrix, col, col);
    }
    
    perform_back_substitution(n, matrix, solution);
    return 1;
}

int main() {
    int n;
    double matrix[105][105], solution[105];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= n; j++) {
            scanf("%lf", &matrix[i][j]);
        }
    }
    
    if (solve_linear_system(n, matrix, solution)) {
        for (int i = 0; i < n; i++) {
            printf("%.6f\n", solution[i]);
        }
    } else {
        printf("No unique solution\n");
    }
    return 0;
}