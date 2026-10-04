#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

void get_row(int rows, int cols, int lst[][100], int x, int *result, int *result_size) {
    *result_size = 0;
    for (int i = rows - 1; i >= 0; i--) {
        for (int j = cols - 1; j >= 0; j--) {
            if (lst[i][j] == x) {
                result[(*result_size)++] = i;
                result[(*result_size)++] = j;
            }
        }
    }
}

int main() {
    int rows, cols, x;
    scanf("%d %d", &rows, &cols);
    int lst[100][100];
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &lst[i][j]);
        }
    }
    scanf("%d", &x);
    int result[10000], result_size;
    get_row(rows, cols, lst, x, result, &result_size);
    for (int i = 0; i < result_size; i += 2) {
        printf("(%d, %d)", result[i], result[i+1]);
        if (i + 2 < result_size) printf(" ");
    }
    printf("\n");
    return 0;
}

