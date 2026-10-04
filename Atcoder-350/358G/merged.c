#include <stdio.h>

void read_grid(int h, int w, int grid[][55], int *start_r, int *start_c) { scanf("%d%d%d", &h, &w, start_r); scanf("%d%d", start_r, start_c); (*start_r)--; (*start_c)--; for(int i = 0; i < h; i++) { for(int j = 0; j < w; j++) { scanf("%d", &grid[i][j]); } } }

long long simulate_movement(int h, int w, int grid[][55], int sr, int sc, long long k) { int dr[] = {-1, 1, 0, 0}; int dc[] = {0, 0, -1, 1}; int r = sr, c = sc; long long total = grid[r][c]; long long moves = 0; int visited[55][55] = {0}; while(moves < k) { int best_r = r, best_c = c, best_val = -1; for(int d = 0; d < 4; d++) { int nr = r + dr[d], nc = c + dc[d]; if(nr >= 0 && nr < h && nc >= 0 && nc < w && grid[nr][nc] > best_val) { best_val = grid[nr][nc]; best_r = nr; best_c = nc; } } if(best_val <= grid[r][c]) break; r = best_r; c = best_c; total += grid[r][c]; moves++; } return total; }

int main() { int h, w, grid[55][55], sr, sc; long long k; read_grid(h, w, grid, &sr, &sc); scanf("%lld", &k); printf("%lld\n", simulate_movement(h, w, grid, sr, sc, k)); return 0; }
