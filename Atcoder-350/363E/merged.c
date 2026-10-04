#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_grid(int *h, int *w, int *y, char grid[][1005]) {
    scanf("%d %d %d", h, w, y);
    for (int i = 0; i < *h; i++) scanf("%s", grid[i]);
}

void simulate_sinking(int h, int w, int y, char grid[][1005], int *result) {
    for (int year = 0; year <= y; year++) {
        int count = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (grid[i][j] == '#') count++;
            }
        }
        result[year] = count;
        if (year == y) break;
        char temp[1005][1005];
        for (int i = 0; i < h; i++) strcpy(temp[i], grid[i]);
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (grid[i][j] == '#') {
                    int water_count = 0;
                    if (i > 0 && grid[i-1][j] == '.') water_count++;
                    if (i < h-1 && grid[i+1][j] == '.') water_count++;
                    if (j > 0 && grid[i][j-1] == '.') water_count++;
                    if (j < w-1 && grid[i][j+1] == '.') water_count++;
                    if (water_count >= 2) temp[i][j] = '.';
                }
            }
        }
        for (int i = 0; i < h; i++) strcpy(grid[i], temp[i]);
    }
}

int main() {
    int h, w, y;
    char grid[1005][1005];
    int result[100005];
    read_grid(&h, &w, &y, grid);
    simulate_sinking(h, w, y, grid, result);
    for (int i = 0; i <= y; i++) printf("%d\n", result[i]);
    return 0;
}
