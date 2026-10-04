#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int validate_move_within_bounds(int h, int w, int next_i, int next_j) {
    if (next_i < 0 || next_i >= h || next_j < 0 || next_j >= w) {
        return 0;
    }
    return 1;
}

int check_obstacle_at_position(char grid[55][55], int i, int j) {
    if (grid[i][j] == '#') {
        return 1;
    }
    return 0;
}

void compute_next_position_from_direction(char dir, int curr_i, int curr_j, int *next_i, int *next_j) {
    *next_i = curr_i;
    *next_j = curr_j;
    if (dir == 'L') (*next_j)--;
    else if (dir == 'R') (*next_j)++;
    else if (dir == 'U') (*next_i)--;
    else if (dir == 'D') (*next_i)++;
}

void execute_navigation_sequence(int h, int w, char grid[55][55], int si, int sj, char *moves, int *final_i, int *final_j) {
    int curr_i = si, curr_j = sj;
    int n = strlen(moves);
    for (int i = 0; i < n; i++) {
        int next_i, next_j;
        compute_next_position_from_direction(moves[i], curr_i, curr_j, &next_i, &next_j);
        if (validate_move_within_bounds(h, w, next_i, next_j) && !check_obstacle_at_position(grid, next_i, next_j)) {
            curr_i = next_i;
            curr_j = next_j;
        }
    }
    *final_i = curr_i;
    *final_j = curr_j;
}

int main() {
    int h, w, si, sj;
    char grid[55][55], moves[1005];
    scanf("%d %d", &h, &w);
    scanf("%d %d", &si, &sj);
    si--; sj--;
    for (int i = 0; i < h; i++) scanf("%s", grid[i]);
    scanf("%s", moves);
    int final_i, final_j;
    execute_navigation_sequence(h, w, grid, si, sj, moves, &final_i, &final_j);
    printf("%d %d\n", final_i + 1, final_j + 1);
    return 0;
}