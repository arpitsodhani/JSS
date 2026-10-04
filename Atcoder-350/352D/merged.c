#include <stdio.h>

void read_input(int *n, int *k, int *p) { scanf("%d%d", n, k); for(int i = 0; i < *n; i++) scanf("%d", &p[i]); }

void find_positions(int *p, int n, int *pos) { for(int i = 0; i < n; i++) pos[p[i]] = i; }

int check_range(int *pos, int start, int k) { int minp = pos[start], maxp = pos[start]; for(int i = start + 1; i < start + k; i++) { if(pos[i] < minp) minp = pos[i]; if(pos[i] > maxp) maxp = pos[i]; } return maxp - minp; }

int min_span(int *pos, int n, int k) { int ans = n; for(int i = 1; i <= n - k + 1; i++) { int span = check_range(pos, i, k); if(span < ans) ans = span; } return ans; }

int main() { int n, k, p[200000], pos[200001]; read_input(&n, &k, p); find_positions(p, n, pos); printf("%d\n", min_span(pos, n, k)); return 0; }
