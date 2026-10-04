#include <stdio.h>

int read_input(int *a, int *c) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%d%d", &a[i], &c[i]); return n; }

int is_dominated(int ax, int cx, int ay, int cy) { return ay > ax && cy < cx; }

int filter(int *a, int *c, int n, int *keep) { for(int i = 0; i < n; i++) keep[i] = 1; int changed = 1; while(changed) { changed = 0; for(int i = 0; i < n; i++) { if(!keep[i]) continue; for(int j = 0; j < n; j++) { if(i == j || !keep[j]) continue; if(is_dominated(a[j], c[j], a[i], c[i])) { keep[j] = 0; changed = 1; } } } } int cnt = 0; for(int i = 0; i < n; i++) if(keep[i]) cnt++; return cnt; }

void output(int *keep, int n) { for(int i = 0; i < n; i++) if(keep[i]) printf("%d ", i + 1); printf("\n"); }

int main() { int a[200000], c[200000], keep[200000]; int n = read_input(a, c); int cnt = filter(a, c, n, keep); printf("%d\n", cnt); output(keep, n); return 0; }
