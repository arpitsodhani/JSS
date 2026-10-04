#include <stdio.h>

int read_input(int *h) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%d", &h[i]); return n; }

int find_taller(int *h, int n, int ref) { for(int i = 1; i < n; i++) { if(h[i] > ref) return i; } return -1; }

int main() { int h[100]; int n = read_input(h); int pos = find_taller(h, n, h[0]); if(pos == -1) printf("-1\n"); else printf("%d\n", pos + 1); return 0; }
