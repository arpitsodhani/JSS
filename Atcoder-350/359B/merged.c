#include <stdio.h>

int read_colors(int n, int colors[]) { for(int i = 0; i < 2 * n; i++) scanf("%d", &colors[i]); return 2 * n; }

void find_positions(int n, int colors[], int first[], int second[]) { for(int i = 1; i <= n; i++) { first[i] = -1; second[i] = -1; } for(int i = 0; i < 2 * n; i++) { int c = colors[i]; if(first[c] == -1) first[c] = i; else second[c] = i; } }

int count_valid_colors(int n, int first[], int second[]) { int count = 0; for(int i = 1; i <= n; i++) { if(second[i] - first[i] == 2) count++; } return count; }

int main() { int n; scanf("%d", &n); int colors[205], first[105], second[105]; read_colors(n, colors); find_positions(n, colors, first, second); printf("%d\n", count_valid_colors(n, first, second)); return 0; }
