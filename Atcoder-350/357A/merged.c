#include <stdio.h>

int count_aliens(int n, int m, int hands[]) { int count = 0, remaining = m; for(int i = 0; i < n; i++) { if(remaining >= hands[i]) { remaining -= hands[i]; count++; } else break; } return count; }

int main() { int m, h[105]; int n = read_input(&m, h); printf("%d\n", count_aliens(n, m, h)); return 0; }

int read_input(int *m, int hands[]) { int n; scanf("%d%d", &n, m); for(int i = 0; i < n; i++) scanf("%d", &hands[i]); return n; }

